from marshmallow import Schema, fields

from app.setup_db import db


class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String)
    country = db.Column(db.String)

    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }

    def __repr__(self):
        return f'Location: {self.country} -> {self.city}'


class LocationSchema(Schema):
    id = fields.Int()
    city = fields.Str()
    country = fields.Str()
