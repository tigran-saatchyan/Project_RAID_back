"""Location model"""
import dataclasses

from marshmallow import Schema, fields

from main.setup_db import db


@dataclasses.dataclass
class Location(db.Model):
    """
    Host model
    """
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String)
    country = db.Column(db.String)

    def to_dict(self):
        """
        Location object to dictionary conversion method
        :return:  - location dictionary
        """
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }

    def __repr__(self):
        return f'Location: {self.country} -> {self.city}'


class LocationSchema(Schema):
    """
    Location Schema
    """
    id = fields.Int()
    city = fields.Str()
    country = fields.Str()
