"""ApartmentFeatures Data Access Object module"""

from main.dao.models.apartments_features import ApartmentFeatures
from main.dao.models.features import Features


class ApartmentFeaturesDAO:
    """
    ApartmentFeatures Data Access Object
    """
    def __init__(self, session):
        self.session = session

    def get_by_apartment_id(self, aid):
        """
        Get all features "ON" by apartment id
        :param aid:     -   apartment id {pk)
        :return:        -   ApartmentFeaturesDAO object
        """
        features_on = self.session.query(
            Features.feature,
            ApartmentFeatures.is_on
        ).join(Features).filter(
            ApartmentFeatures.apartment_id == aid,
            ApartmentFeatures.is_on == 1
        ).all()

        features_off = self.session.query(
            Features.feature,
            ApartmentFeatures.is_on
        ).join(Features).filter(
            ApartmentFeatures.apartment_id == aid,
            ApartmentFeatures.is_on == 0
        ).all()

        return features_on, features_off

    def get_one(self, afid):
        """
        Get one apartment_feature
        :param afid:    -   apartment_feature id
        :return:        -   ApartmentFeaturesDAO object
        """
        return self.session.query(ApartmentFeatures).filter(
            ApartmentFeatures.id == afid
        ).one()

    def get_all(self):
        """
        Get all apartment_feature
        :return:        -   ApartmentFeaturesDAO object
        """
        return self.session.query(ApartmentFeatures).all()
