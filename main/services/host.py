"""HostService module"""

from main.dao.host import HostDAO
from main.log_handler import services_logger


class HostService:
    """
    Host service
    """

    def __init__(self, dao: HostDAO):
        self.dao = dao
        self.logger = services_logger

    def get_one(self, hid):
        """
        Get one host by host id
        :param hid:     -   host id
        :return:        -   HostService object
        """
        self.logger.info("Getting host with id %d", hid)
        return self.dao.get_one(hid)

    def get_all(self):
        """
        Get all hosts
        :return:        -   HostService object
        """
        self.logger.info("Getting all hosts")
        return self.dao.get_all()
