"""Apartments Data Access Object module"""

from main.dao.models.apartments import Apartments
from main.dao.models.location import Location


class ApartmentsDAO:
    """
    Apartments Data Access Object
    """

    def __init__(self, session):
        self.session = session

    def get_one(self, aid):
        """
        Get one apartment
        :param aid:     -   apartment id (pk)
        :return:        -   ApartmentsDAO object
        """
        return self.session.query(Apartments).filter(
            Apartments.pk == aid
        ).one()

    def get_all(self):
        """
        Get one apartments
        :return:  - ApartmentsDAO object
        """
        return self.session.query(
            Apartments,
            Location
        ).select_from(Apartments).join(Location).all()
