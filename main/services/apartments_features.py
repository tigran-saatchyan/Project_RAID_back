"""ApartmentFeaturesService module"""

from main.dao.apartments_features import ApartmentFeaturesDAO
from main.log_handler import services_logger


class ApartmentFeaturesService:
    """
    Apartment Features service
    """

    def __init__(self, dao: ApartmentFeaturesDAO):
        self.dao = dao
        self.logger = services_logger

    def get_by_apartment_id(self, aid):
        """
        Get all features "ON" by apartment id
        :param aid:     -   apartment id {pk)
        :return:        -   ApartmentFeaturesService object
        """
        features = self.dao.get_by_apartment_id(aid)
        self.logger.info(
            "Got %d features for apartment %d", len(features),
            aid
            )
        return features

    def get_one(self, afid):
        """
        Get one apartment_feature
        :param afid:    -   apartment_feature id
        :return:        -   ApartmentFeaturesService object
        """
        feature = self.dao.get_one(afid)
        if feature is None:
            self.logger.info("No feature found with id %d", afid)
        else:
            self.logger.info("Got feature with id %d", afid)
        return feature

    def get_all(self):
        """
        Get all apartment_feature
        :return:        -   ApartmentFeaturesService object
        """
        features = self.dao.get_all()
        self.logger.info("Got %d features in total", len(features))
        return features
