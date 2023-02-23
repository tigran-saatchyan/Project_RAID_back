"""Places view module"""
from flask import jsonify, request
from flask_restx import Api, Namespace, Resource, reqparse
from sqlalchemy.orm.exc import NoResultFound

from main.constants import CORS_HEADER
from main.container import apartment_service, apartments_features_service
from main.dao.models.apartments import ApartmentSchema, ApartmentsSchema

places_ns = Namespace('places', 'Returns apartments sorted by country')

apartment_schema = ApartmentSchema()
apartments_schema = ApartmentsSchema(many=True)

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
        filter_city = request.args.get('city')
        price_from = request.args.get('from')
        price_to = request.args.get('to')

        try:
            if not filter_city or (filter_city.isalpha() and len(
                    filter_city
            ) <= 255):
                pass
            else:
                raise TypeError

            price_from = int(price_from) if price_from else 0
            price_to = int(price_to) if price_to else 0
        except ValueError:
            return {"ValueError": "Wrong parameter value."}, 400, CORS_HEADER
        except TypeError :
            return {"TypeError": "Wrong parameter type."}, 400, CORS_HEADER

        all_apartment = apartment_service.get_all(
            filter_city,
            price_from,
            price_to
        )

        return apartments_schema.dump(all_apartment), 200, CORS_HEADER


place_parser = reqparse.RequestParser()
place_parser.add_argument(
    'pk',
    type=str,
    help='Apartment primary key'
)


@places_ns.route('/<int:pk>')
class PlaceView(Resource):
    """
    Place Class Based View
    """
    @staticmethod
    @places_ns.response(200, 'Success')
    @places_ns.response(404, 'Apartment not found')
    def get(pk):
        """
        Get detailed data for one apartment by apartments PK

        """
        try:
            apartment = apartment_service.get_one(pk)
        except NoResultFound:
            return {"error": "Apartment not found"}, 404, CORS_HEADER

        features_on, features_off = \
            apartments_features_service.get_by_apartment_id(pk)

        apartment['features_on'] = [
            feature[0]
            for feature in features_on
        ]

        apartment['features_off'] = [
            feature[0]
            for feature in features_off
        ]

        return apartment_schema.dump(apartment), 200, CORS_HEADER
