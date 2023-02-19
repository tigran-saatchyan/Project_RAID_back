from main.setup_db import db


class ApartmentFeatures(db.Model):
    __tablename__ = 'apartment_features'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartments.pk'))
    feature_id = db.Column(db.Integer, db.ForeignKey('features.id'))
    is_on = db.Column(db.Boolean)

    apartment = db.relationship("Apartments")

    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }

    def __repr__(self):
        return f'ApartmentFeatures: {self.apartment_id} - ' \
               f'{self.feature_id} - ' \
               f'{self.is_on}'