"""Apartments Data Access Object module"""

from sqlalchemy import func

from main.dao.models.apartments import Apartments
from main.dao.models.host import Host
from main.dao.models.location import Location


class ApartmentsDAO:
    """
    Apartments Data Access Object
    """
    def __init__(self, session):
        self.session = session

    def get_one(self, aid: int):
        """
        Get one apartment
        :param aid:     -   apartment id (pk)
        :return:        -   ApartmentsDAO object
        """
        apartment_info = self.session.query(
            Apartments,
            Location,
            Host
        ).select_from(Apartments).join(Location).join(Host).filter(
            Apartments.pk == aid
        ).one()
        return apartment_info

    def get_all(self, city: str, price_from: int, pare_to: int):
        """
        Get all apartments filtered by city
        :return:  - ApartmentsDAO object
        """
        apartments_by_city = self.session.query(
            Apartments,
            Location
        ).select_from(Apartments).join(Location)

        if city:
            apartments_by_city = apartments_by_city.filter(
                func.lower(Location.city) == func.lower(city)
            )

        if price_from:
            apartments_by_city = apartments_by_city.filter(
                Apartments.price >= price_from
            )

        if pare_to:
            apartments_by_city = apartments_by_city.filter(
                Apartments.price <= pare_to
            )

        apartments_by_city = apartments_by_city.order_by(
            Location.country
        ).all()
        return apartments_by_city
