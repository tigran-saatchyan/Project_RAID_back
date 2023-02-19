from main.dao.models.apartments import Apartments
from main.dao.models.host import Host
from main.dao.models.location import Location


class ApartmentsDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, aid):
        return self.session.query(Apartments).filter(
            Apartments.pk == aid
        ).one()

    def get_all(self):
        return self.session.query(
            Apartments,
            Location
        ).select_from(Apartments).join(Location).all()
