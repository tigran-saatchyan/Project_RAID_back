"""FeaturesService module"""

from main.dao.features import FeaturesDAO
from main.log_handler import services_logger


class FeaturesService:
    """
    Features service
    """

    def __init__(self, dao: FeaturesDAO):
        self.dao = dao
        self.logger = services_logger

    def get_one(self, fid):
        """
        Get one feature
        :param fid:     -   feature id
        :return:        -   FeaturesService object
        """
        feature = self.dao.get_one(fid)
        self.logger.info("Retrieved feature %d: %d", feature.id, feature.name)
        return feature

    def get_all(self):
        """
        Get all Features
        :return:        -   FeaturesService object
        """
        features = self.dao.get_all()
        self.logger.info("Retrieved %d features", len(features))
        return features
