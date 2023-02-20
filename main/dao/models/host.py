"""Host model"""
import dataclasses

from marshmallow import Schema, fields

from main.setup_db import db


@dataclasses.dataclass
class Host(db.Model):
    """
    Host model
    """
    __tablename__ = 'hosts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    host_name = db.Column(db.String)
    host_phone = db.Column(db.String)
    host_location = db.Column(db.String)

    def to_dict(self):
        """
        Host object to dictionary conversion method
        :return:  - host dictionary
        """
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }

    def __repr__(self):
        return f'Host: {self.host_name} - {self.host_location}'


class HostSchema(Schema):
    """
    Host Schema
    """
    id = fields.Int()
    host_name = fields.Str()
    host_phone = fields.Str()
    host_location = fields.Str()
