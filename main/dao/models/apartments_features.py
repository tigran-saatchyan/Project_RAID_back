"""ApartmentFeatures model"""

import dataclasses

from main.setup_db import db


@dataclasses.dataclass
class ApartmentFeatures(db.Model):
    """
    ApartmentFeatures model
    """
    __tablename__ = 'apartment_features'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartments.pk'))
    feature_id = db.Column(db.Integer, db.ForeignKey('features.id'))
    is_on = db.Column(db.Boolean)

    apartment = db.relationship("Apartments")

    def to_dict(self):
        """
        ApartmentFeatures object to dictionary conversion method
        :return:  - apartment-features dictionary
        """
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }

    def __repr__(self):
        return f'ApartmentFeatures: {self.apartment_id} - ' \
               f'{self.feature_id} - ' \
               f'{self.is_on}'
