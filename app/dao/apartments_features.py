from app.dao.models.apartments_features import ApartmentFeatures
from app.dao.models.features import Features


class ApartmentFeaturesDAO:
    def __init__(self, session):
        self.session = session

    def get_on(self, aid):
        return self.session.query(
            ApartmentFeatures.apartment_id,
            Features.feature,
            ApartmentFeatures.is_on
        ).join(Features).filter(
            ApartmentFeatures.apartment_id == aid,
            ApartmentFeatures.is_on == 1
        ).all()

    def get_off(self, aid):
        return self.session.query(
            ApartmentFeatures.apartment_id,
            Features.feature,
            ApartmentFeatures.is_on
        ).join(Features).filter(
            ApartmentFeatures.apartment_id == aid,
            ApartmentFeatures.is_on == 0
        ).all()

    def get_one(self, afid):
        return self.session.query(ApartmentFeatures).filter(
            ApartmentFeatures.id == afid
        ).one()

    def get_all(self):
        return self.session.query(ApartmentFeatures).all()
