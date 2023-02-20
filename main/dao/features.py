"""Features Data Access Object module"""

from main.dao.models.features import Features


class FeaturesDAO:
    """
    Features Data Access Object
    """
    def __init__(self, session):
        self.session = session

    def get_one(self, fid):
        """
        Get one feature
        :param fid:     -   feature id
        :return:        -   FeaturesDAO object
        """
        return self.session.query(Features).filter(
            Features.id == fid
        ).one()

    def get_all(self):
        """
        Get all Features
        :return:        -   FeaturesDAO object
        """
        return self.session.query(Features).all()
