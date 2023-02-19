from marshmallow import Schema, fields

from app.setup_db import db


class Host(db.Model):
    __tablename__ = 'hosts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    host_name = db.Column(db.String)
    host_phone = db.Column(db.String)
    host_location = db.Column(db.String)

    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }

    def __repr__(self):
        return f'Host: {self.host_name} - {self.host_location}'


class HostSchema(Schema):
    id = fields.Int()
    host_name = fields.Str()
    host_phone = fields.Str()
    host_location = fields.Str()
