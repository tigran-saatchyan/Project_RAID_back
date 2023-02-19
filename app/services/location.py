from app.dao.location import LocationDAO


class LocationService:
    def __init__(self, dao: LocationDAO):
        self.dao = dao

    def get_one(self, lid):
        return self.dao.get_one(lid)

    def get_all(self):
        return self.dao.get_all()
