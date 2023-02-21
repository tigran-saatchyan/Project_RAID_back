"""Places view module"""
from flask import request
from flask_restx import Api, Namespace, Resource, reqparse

from main.container import apartment_service, apartments_features_service
from main.dao.models.apartments import ApartmentsSchema

places_ns = Namespace('places', 'Places namespace')

apartment_schema = ApartmentsSchema()
apartments_schema = ApartmentsSchema(many=True)

api = Api()

places_parser = reqparse.RequestParser()
places_parser.add_argument('city', type=str, help='Filter by selected City')
places_parser.add_argument('from', type=int, help='Price From:')
places_parser.add_argument('to', type=int, help='Price To')


@api.response(200, 'Success')
@places_ns.route('/')
# @cross_origin()
class PlacesView(Resource):
    """
    Places Class Based View
    """
    @staticmethod
    @api.doc(parser=places_parser)
    def get():
        """
        Get all apartments ordered by pk with or without filters
        response   -   all_apartment JSON
        """

        # arguments prepared for filter
        filter_city = request.args.get('city')
        price_from = request.args.get('from')
        price_to = request.args.get('to')

        all_apartment = apartment_service.get_all(
            filter_city,
            price_from,
            price_to
        )

        return apartments_schema.dump(all_apartment), 200


@api.response(200, 'Success')
@api.response(404, 'Not Found')
@places_ns.route('/<int:apk>')
class PlaceView(Resource):
    """
    Place Class Based View
    """

    @staticmethod
    def get(apk):
        """
        Get detailed data for one apartment by PK
        :return:    -   apartment dictionary
        """

        apartment = apartment_service.get_one(apk)
        features_on, features_off = \
            apartments_features_service.get_by_apartment_id(apk)

        print(features_on)
        print(features_off)
        # if apartment is None or not apartment:
        #     return "", 404
        # return apartments_schema.dump(apartment), 200
