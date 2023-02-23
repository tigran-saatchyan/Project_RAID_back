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
        Get all features by apartment id
        :param aid:     -   apartment id {pk)
        :return:        -   ApartmentFeaturesDAO object
        """
        features = self.session.query(
            Features.feature, ApartmentFeatures.is_on
        ).join(Features).filter(
            ApartmentFeatures.apartment_id == aid
        ).all()

        features_on = [feature for feature in features if feature[1] == 1]
        features_off = [feature for feature in features if feature[1] == 0]

        return features_on, features_off

    def get_one(self, afid):
        """
        Get one apartment_feature
        :param afid:    -   apartment_feature id
        :return:        -   ApartmentFeaturesDAO object
        """
        return self.session.query(ApartmentFeatures).filter(id == afid).one()

    def get_all(self):
        """
        Get all apartment_feature
        :return:        -   ApartmentFeaturesDAO object
        """
        return self.session.query(ApartmentFeatures).all()
