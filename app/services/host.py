from app.dao.host import HostDAO


class HostService:
    def __init__(self, dao: HostDAO):
        self.dao = dao

    def get_one(self, hid):
        return self.dao.get_one(hid)

    def get_all(self):
        return self.dao.get_all()
