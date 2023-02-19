from app.dao.models.features import Features


class FeaturesDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, fid):
        return self.session.query(Features).filter(
            Features.id == fid
        ).one()

    def get_all(self):
        return self.session.query(Features).all()
