from main.dao.models.host import Host


class HostDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, hid):
        return self.session.query(Host).filter(
            Host.id == hid
        ).one()

    def get_all(self):
        return self.session.query(Host).all()
