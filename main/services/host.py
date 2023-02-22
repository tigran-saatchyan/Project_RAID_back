"""HostService module"""

from main.dao.host import HostDAO


class HostService:
    """
    Host service
    """
    def __init__(self, dao: HostDAO):
        self.dao = dao

    def get_one(self, hid):
        """
        Get one host by host id
        :param hid:     -   host id
        :return:        -   HostService object
        """
        return self.dao.get_one(hid)

    def get_all(self):
        """
        Get all hosts
        :return:        -   HostService object
        """
        return self.dao.get_all()
