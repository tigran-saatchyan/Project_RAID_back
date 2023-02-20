"""FeaturesService module"""

from main.dao.features import FeaturesDAO


class FeaturesService:
    """
    Features service
    """
    def __init__(self, dao: FeaturesDAO):
        self.dao = dao

    def get_one(self, fid):
        """
        Get one feature
        :param fid:     -   feature id
        :return:        -   FeaturesService object
        """
        return self.dao.get_one(fid)

    def get_all(self):
        """
        Get all Features
        :return:        -   FeaturesService object
        """
        return self.dao.get_all()
