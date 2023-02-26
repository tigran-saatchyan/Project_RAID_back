"""FeaturesDAO module"""

from main.dao.models.features import Features
from main.log_handler import dao_logger


class FeaturesDAO:
    """
    Features Data Access Object
    """

    def __init__(self, session):
        self.session = session
        self.logger = dao_logger

    def get_one(self, fid):
        """
        Get one feature
        :param fid:     -   feature id
        :return:        -   FeaturesDAO object
        """
        self.logger.info("Getting feature with ID %s", fid)
        return self.session.query(Features).filter(
            Features.id == fid
        ).one()

    def get_all(self):
        """
        Get all Features
        :return:        -   FeaturesDAO object
        """
        self.logger.info("Getting all features")
        return self.session.query(Features).all()
