"""Apartments model and schema"""
import dataclasses

from marshmallow import Schema, fields

from main.setup_db import db


class Apartments(db.Model):
    """
    Apartments model
    """
    __tablename__ = 'apartments'
    pk = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    picture_url = db.Column(db.Text)
    price = db.Column(db.BigInteger)
    city_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    host_id = db.Column(db.Integer, db.ForeignKey('hosts.id'))

    city = db.relationship('Location')
    host = db.relationship('Host')

    def to_dict(self):
        """
        Apartments object to dictionary conversion method
        :return:  - apartments dictionary
        """
        return {
            col.name: getattr(self, col.name) for col in self.__table__.columns
        }

    def __repr__(self):
        return f'Apartments: {self.title} {self.price}'


class ApartmentsSchema(Schema):
    """
    Apartments Schema
    """
    pk = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    picture_url = fields.Str()
    price = fields.Int()

    country = fields.Str()
    city = fields.Str()

    @dataclasses.dataclass
    class Meta:
        """
        Metaclass for ApartmentsSchema to make schema ordered
        """
        ordered = True


class ApartmentSchema(Schema):
    """
    Apartment Schema
    """
    pk = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    picture_url = fields.Url()
    price = fields.Int()

    country = fields.Str()
    city = fields.Str()

    features_on = fields.List(fields.Str)
    features_off = fields.List(fields.Str)

    host_name = fields.Str()
    host_phone = fields.Str()
    host_location = fields.Str()

    @dataclasses.dataclass
    class Meta:
        """
        Metaclass for ApartmentSchema to make schema ordered
        """
        ordered = True
