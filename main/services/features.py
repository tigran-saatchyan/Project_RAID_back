from main.dao.features import FeaturesDAO


class FeaturesService:
    def __init__(self, dao: FeaturesDAO):
        self.dao = dao

    def get_one(self, fid):
        return self.dao.get_one(fid)

    def get_all(self):
        return self.dao.get_all()
