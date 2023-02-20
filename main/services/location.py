"""LocationService module"""

from main.dao.location import LocationDAO


class LocationService:
    """
    Location service
    """
    def __init__(self, dao: LocationDAO):
        self.dao = dao

    def get_one(self, lid):
        """
        Get one location
        :param lid:     -   location id
        :return:        -   LocationDAO object
        """
        return self.dao.get_one(lid)

    def get_all(self):
        """
        Get all locations
        :return:        -   LocationDAO object
        """
        return self.dao.get_all()
