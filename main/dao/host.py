"""Host Data Access Object module"""

from main.dao.models.host import Host


class HostDAO:
    """
    Host Data Access Object
    """
    def __init__(self, session):
        self.session = session

    def get_one(self, hid):
        """
        Get one feature
        :param hid:     -   host id
        :return:        -   HostDAO object
        """
        return self.session.query(Host).filter(
            Host.id == hid
        ).one()

    def get_all(self):
        """
        Get all hosts
        :return:        -   HostDAO object
        """
        return self.session.query(Host).all()
