from main.dao.models.location import Location


class LocationDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, lid):
        return self.session.query(Location).filter(
            Location.id == lid
        ).one()

    def get_all(self):
        return self.session.query(Location).all()
