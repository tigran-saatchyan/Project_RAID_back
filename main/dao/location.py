"""LocationDAO module"""

from main.dao.models.location import Location
from main.log_handler import dao_logger


class LocationDAO:
    """
    Apartments Data Access Object
    """

    def __init__(self, session):
        self.session = session
        self.logger = dao_logger

    def get_one(self, lid):
        """
        Get one location
        :param lid:     -   location id
        :return:        -   LocationDAO object
        """
        self.logger.info("Getting location with ID %s", lid)
        return self.session.query(Location).filter(
            Location.id == lid
        ).one()

    def get_all(self):
        """
        Get all locations
        :return:        -   LocationDAO object
        """
        self.logger.info("Getting all locations")
        return self.session.query(Location).all()
