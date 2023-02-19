from flask import request
from flask_restx import Api, Namespace, Resource, reqparse

from main.container import apartment_service
from main.dao.models.apartments import ApartmentsSchema

places_ns = Namespace('places', 'Places namespace')

apartment_schema = ApartmentsSchema()
apartments_schema = ApartmentsSchema(many=True)

api = Api()

places_parser = reqparse.RequestParser()
places_parser.add_argument('city', type=str, help='Filter by selected City')
places_parser.add_argument('from', type=int, help='Price From:')
places_parser.add_argument('to', type=int, help='Price To')


@places_ns.route('/')
class PlacesView(Resource):
    @staticmethod
    @api.doc(parser=places_parser)
    def get():
        filter_city = request.args.get('city')
        price_from = request.args.get('from')
        price_to = request.args.get('to')

        all_apartment = apartment_service.get_all()

        return apartments_schema.dump(all_apartment), 200


place_parser = reqparse.RequestParser()
place_parser.add_argument('pk', type=str, help='Apartment primary key')


@places_ns.route('/<int:pk>')
class PlaceView(Resource):
    @api.doc(parser=place_parser)
    def get(self, pk):
        apartment = apartment_service.get_one(pk)
        apartment = apartment.to_dict()
        print(apartment)
        return apartments_schema.dump(apartment), 200
