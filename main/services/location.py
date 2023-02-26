"""LocationService module"""

from main.dao.location import LocationDAO
from main.log_handler import services_logger


class LocationService:
    """
    Location service
    """

    def __init__(self, dao: LocationDAO):
        self.dao = dao
        self.logger = services_logger

    def get_one(self, lid):
        """
        Get one location
        :param lid:     -   location id
        :return:        -   LocationDAO object
        """
        self.logger.info("Getting location with id: %s", lid)
        return self.dao.get_one(lid)

    def get_all(self):
        """
        Get all locations
        :return:        -   LocationDAO object
        """
        self.logger.info("Getting all locations")
        return self.dao.get_all()
