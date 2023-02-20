"""Features model"""
import dataclasses

from main.setup_db import db


@dataclasses.dataclass
class Features(db.Model):
    """
    ApartmentFeatures model
    """
    __tablename__ = 'features'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    feature = db.Column(db.String)

    def to_dict(self):
        """
        Features object to dictionary conversion method
        :return:  - features dictionary
        """
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }

    def __repr__(self):
        return f'Feature: {self.feature}'
