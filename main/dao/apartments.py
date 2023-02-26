"""ApartmentsDAO module"""

from sqlalchemy import func

from main.dao.models.apartments import Apartments
from main.dao.models.host import Host
from main.dao.models.location import Location
from main.log_handler import dao_logger


class ApartmentsDAO:
    """
    Apartments Data Access Object
    """

    def __init__(self, session):
        self.session = session
        self.logger = dao_logger

    def get_one(self, aid: int):
        """
        Get one apartment
        :param aid:     -   apartment id (pk)
        :return:        -   ApartmentsDAO object
        """
        self.logger.info("Getting apartment with id=%d", aid)
        query = self.session.query(
            Apartments,
            Location,
            Host
        ).select_from(Apartments).join(Location).join(Host).filter(
            Apartments.pk == aid
        ).one()
        return query

    def get_all(self, city: str, price_from: int, pare_to: int):
        """
        Get all apartments filtered by city
        :return:  - ApartmentsDAO object
        """
        self.logger.info(
            "Getting all apartments in city=%s, price from=%d, price to=%d",
            city, price_from, pare_to
        )
        query = self.session.query(
            Apartments,
            Location
        ).select_from(Apartments).join(Location)

        if city:
            query = query.filter(func.lower(Location.city) == func.lower(city))
            self.logger.info("Filtering by city=%s", city)

        if price_from:
            query = query.filter(Apartments.price >= price_from)
            self.logger.info("Filtering by price from=%s", price_from)

        if pare_to:
            query = query.filter(Apartments.price <= pare_to)
            self.logger.info("Filtering by price to=%s", pare_to)

        query = query.order_by(Location.country).all()
        return query
