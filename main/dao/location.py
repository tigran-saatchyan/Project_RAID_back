"""Location Data Access Object module"""

from main.dao.models.location import Location


class LocationDAO:
    """
    Apartments Data Access Object
    """
    def __init__(self, session):
        self.session = session

    def get_one(self, lid):
        """
        Get one location
        :param lid:     -   location id
        :return:        -   LocationDAO object
        """
        return self.session.query(Location).filter(
            Location.id == lid
        ).one()

    def get_all(self):
        """
        Get all locations
        :return:        -   LocationDAO object
        """
        return self.session.query(Location).all()
