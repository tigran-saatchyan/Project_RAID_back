"""Container module"""

from main.dao.apartments import ApartmentsDAO
from main.dao.apartments_features import ApartmentFeaturesDAO
from main.dao.host import HostDAO
from main.services.apartments import ApartmentsService
from main.services.apartments_features import ApartmentFeaturesService
from main.services.host import HostService
from main.setup_db import db

apartment_dao = ApartmentsDAO(db.session)
apartment_service = ApartmentsService(apartment_dao)

host_dao = HostDAO(db.session)
host_service = HostService(host_dao)

apartments_features_dao = ApartmentFeaturesDAO(db.session)
apartments_features_service = ApartmentFeaturesService(
    apartments_features_dao
)

# apartment_dao = ApartmentsDAO(db.session)
# apartment_service = ApartmentsService(apartment_dao)
#
# apartment_dao = ApartmentsDAO(db.session)
# apartment_service = ApartmentsService(apartment_dao)
