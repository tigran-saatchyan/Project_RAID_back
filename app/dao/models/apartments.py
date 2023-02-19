from marshmallow import Schema, fields

from app.dao.models.host import HostSchema
from app.dao.models.location import LocationSchema
from app.setup_db import db


class Apartments(db.Model):
    __tablename__ = 'apartments'
    pk = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    picture_url = db.Column(db.Text)
    price = db.Column(db.Integer)
    city_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    host_id = db.Column(db.Integer, db.ForeignKey('hosts.id'))

    city = db.relationship('Location')
    host = db.relationship('Host')

    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }

    def __repr__(self):
        return f'Apartments: {self.title} {self.price}'


class ApartmentsSchema(Schema):

    pk = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    picture_url = fields.Url()
    price = fields.Int()

    country = fields.Str()
    city = fields.Str()

    # features_on = fields.List(fields.Str)
    # features_off = fields.List(fields.Str)
    #
    # host_name = fields.Str()
    # host_phone = fields.Str()
    # host_location = fields.Str()

    class Meta:
        ordered = True


#
# class ApartmentsSchema(Schema):
#     pk = fields.Int(dump_only=True)
#     title = fields.Str()
#     description = fields.Str()
#     picture_url = fields.Url()
#     price = fields.Int()
#
#     country = fields.Pluck(LocationSchema, "country")
#     city = fields.Pluck(LocationSchema, "city")
    #
    # features_on = fields.List(fields.Str)
    # features_off = fields.List(fields.Str)
    #
    # host_name = fields.Pluck(HostSchema, "host_name")
    # host_phone = fields.Pluck(HostSchema, "host_phone")
    # host_location = fields.Pluck(HostSchema, "host_location")
    #


    class Meta:
        ordered = True
