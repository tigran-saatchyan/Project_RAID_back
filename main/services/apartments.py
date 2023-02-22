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
        apartment = apartment.to_dict()
        apartment.update(location.to_dict())
        apartment.update(host.to_dict())

        return apartment

    def get_all(self, city: str, price_from: int, pare_to: int) -> list:
        """
        Get all apartments including location
        :return:  - apartments dictionary
        """
        result = []
        all_apartment = self.dao.get_all(city, price_from, pare_to)

        for apartment, location in all_apartment:
            apartment = apartment.to_dict()
            location = location.to_dict()
            apartment.update(location)

            result.append(apartment)

        return result
