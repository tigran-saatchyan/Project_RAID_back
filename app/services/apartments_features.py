from app.dao.apartments_features import ApartmentFeaturesDAO


class ApartmentFeaturesService:
    def __init__(self, dao: ApartmentFeaturesDAO):
        self.dao = dao

    def get_on(self, aid):
        return self.dao.get_on(aid)

    def get_off(self, aid):
        return self.dao.get_off(aid)

    def get_one(self, afid):
        return self.dao.get_one(afid)

    def get_all(self):
        return self.dao.get_all()
