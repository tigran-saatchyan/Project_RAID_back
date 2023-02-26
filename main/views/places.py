"""Places view module"""

from flask import request
from flask_restx import Api, Namespace, Resource, reqparse
from sqlalchemy.orm.exc import NoResultFound

from main.constants import CORS_HEADER
from main.container import apartment_service, apartments_features_service
from main.dao.models.apartments import ApartmentSchema, ApartmentsSchema
from main.log_handler import views_logger

places_ns = Namespace('places', 'Returns apartments sorted by country')

apartments_schema = ApartmentsSchema(many=True)
apartment_schema = ApartmentSchema()

api = Api()

places_parser = reqparse.RequestParser()
places_parser.add_argument(
    'city',
    type=str,
    help='(optional) Filter by selected City (max 255 char)'
)

places_parser.add_argument(
    'from',
    type=int,
    help='(optional) Price From:'
)

places_parser.add_argument(
    'to',
    type=int,
    help='(optional) Price To'
)


@places_ns.route('/')
class PlacesView(Resource):
    """
    Places Class Based View
    """

    @staticmethod
    @api.doc(parser=places_parser)
    @places_ns.response(200, 'Success')
    @places_ns.response(400, 'Bad Request')
    @places_ns.response(404, 'Not Found')
    def get():
        """
        Get all apartments ordered by pk with or without filters
        """
        max_int = 9223372036854775807
        try:
            filter_city = request.args.get('city', '', str)

            price_from = int(request.args.get('from', 0, int))
            price_to = request.args.get('to', 0, int)
            try:
                price_to = int(request.args.get('to', 0))
            except ValueError:
                raise ValueError(
                    "Invalid value for 'to' parameter: must be an integer"
                    )

            if not filter_city or (
                    filter_city.isalpha() and len(filter_city) <= 255
            ):
                pass
            else:
                raise TypeError

            if not 0 <= int(price_from) <= int(price_to) <= max_int:
                raise ValueError

            price_from = int(price_from) if price_from else 0
            price_to = int(price_to) if price_to else 0
        except (ValueError, TypeError) as err:
            views_logger.error("Error: %s", err)
            return {"Error": str(err)}, 400, CORS_HEADER

        all_apartment = apartment_service.get_all(
            filter_city,
            price_from,
            price_to
        )

        views_logger.info("All apartments fetched successfully")
        return apartments_schema.dump(all_apartment), 200, CORS_HEADER


place_parser = reqparse.RequestParser()
place_parser.add_argument(
    'pk',
    type=str,
    help='Apartment primary key'
)


@places_ns.route('/<int:apk>')
class PlaceView(Resource):
    """
    Place Class Based View
    """

    @staticmethod
    @places_ns.response(200, 'Success')
    @places_ns.response(404, 'Apartment not found')
    def get(apk):
        """
        Get detailed data for one apartment by apartments PK
        """
        try:
            apartment = apartment_service.get_one(apk)

            features_on, features_off = \
                apartments_features_service.get_by_apartment_id(apk)

            apartment['features_on'] = [
                feature[0]
                for feature in features_on
            ]

            apartment['features_off'] = [
                feature[0]
                for feature in features_off
            ]

            views_logger.info("Retrieved apartment details for PK %d", apk)

            return apartment_schema.dump(apartment), 200, CORS_HEADER
        except NoResultFound:
            views_logger.info("Apartment not found for PK %d", apk)
            return {"error": "Apartment not found"}, 404, CORS_HEADER
