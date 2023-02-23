"""ApartmentsService module"""

from main.dao.apartments import ApartmentsDAO


class ApartmentsService:
    """
    Apartments service
    """
    def __init__(self, dao: ApartmentsDAO):
        self.dao = dao

    def get_one(self, aid: int) -> dict:
        """
        Get one apartment
        :param aid:     -   apartment id (pk)
        :return:        -   ApartmentsService object
        """
        apartment_info = self.dao.get_one(aid)
        apartment, location, host = apartment_info
        return {**apartment.to_dict(), **location.to_dict(), **host.to_dict()}

    def get_all(self, city: str, price_from: int, pare_to: int) -> list:
        """
        Get all apartments including location
        :return:  - apartments dictionary
        """
        all_apartment = self.dao.get_all(city, price_from, pare_to)

        return [
            {**apartment.to_dict(), **location.to_dict()}
            for apartment, location in all_apartment]
