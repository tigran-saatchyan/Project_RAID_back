"""ApartmentFeaturesService module"""

from main.dao.apartments_features import ApartmentFeaturesDAO


class ApartmentFeaturesService:
    """
    Apartment Features service
    """
    def __init__(self, dao: ApartmentFeaturesDAO):
        self.dao = dao

    def get_by_apartment_id(self, aid):
        """
        Get all features "ON" by apartment id
        :param aid:     -   apartment id {pk)
        :return:        -   ApartmentFeaturesService object
        """
        return self.dao.get_by_apartment_id(aid)

    def get_one(self, afid):
        """
        Get one apartment_feature
        :param afid:    -   apartment_feature id
        :return:        -   ApartmentFeaturesService object
        """
        return self.dao.get_one(afid)

    def get_all(self):
        """
        Get all apartment_feature
        :return:        -   ApartmentFeaturesService object
        """
        return self.dao.get_all()
