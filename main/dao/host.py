"""HostDAO module"""

from main.dao.models.host import Host
from main.log_handler import dao_logger


class HostDAO:
    """
    Host Data Access Object
    """

    def __init__(self, session):
        self.session = session
        self.logger = dao_logger

    def get_one(self, hid):
        """
        Get one feature
        :param hid:     -   host id
        :return:        -   HostDAO object
        """
        self.logger.info("Getting host with ID %s", hid)
        return self.session.query(Host).filter(
            Host.id == hid
        ).one()

    def get_all(self):
        """
        Get all hosts
        :return:        -   HostDAO object
        """
        self.logger.info("Getting all hosts")
        return self.session.query(Host).all()
