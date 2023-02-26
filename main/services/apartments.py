"""ApartmentsService module"""

from main.dao.apartments import ApartmentsDAO
from main.log_handler import services_logger


class ApartmentsService:
    """
    Apartments service
    """

    def __init__(self, dao: ApartmentsDAO):
        self.dao = dao
        self.logger = services_logger

    def get_one(self, aid: int) -> dict:
        """
        Get one apartment
        :param aid:     -   apartment id (pk)
        :return:        -   ApartmentsService object
        """
        self.logger.info("Retrieving apartment with ID %d", aid)
        apartment_info = self.dao.get_one(aid)
        apartment, location, host = apartment_info
        result = {
            **apartment.to_dict(), **location.to_dict(), **host.to_dict()
        }
        self.logger.info("Retrieved apartment with ID %d: %s", aid, result)
        return result

    def get_all(self, city: str, price_from: int, pare_to: int) -> list:
        """
        Get all apartments including location
        :return:  - apartments dictionary
        """
        self.logger.info(
            "Retrieving all apartments for city '%s' with price range %d - "
            "%d", city, price_from, pare_to
        )
        all_apartment = self.dao.get_all(city, price_from, pare_to)
        result = [
            {**apartment.to_dict(), **location.to_dict()}
            for apartment, location in all_apartment
        ]
        self.logger.info(
            "Retrieved %d apartments for city '%s' with price range %d - "
            "%d", len(result), city, price_from, pare_to
        )
        return result
