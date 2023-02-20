"""ApartmentsService module"""

from main.dao.apartments import ApartmentsDAO


class ApartmentsService:
    """
    Apartments service
    """
    def __init__(self, dao: ApartmentsDAO):
        self.dao = dao

    def get_one(self, aid):
        """
        Get one apartment
        :param aid:     -   apartment id (pk)
        :return:        -   ApartmentsService object
        """
        apartment = self.dao.get_one(aid)

        return

    def get_all(self, city, price_from, pare_to):
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
