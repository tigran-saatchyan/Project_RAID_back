from app.dao.apartments import ApartmentsDAO
from app.dao.apartments_features import ApartmentFeaturesDAO
from app.dao.host import HostDAO
from app.services.apartments import ApartmentsService
from app.services.apartments_features import ApartmentFeaturesService
from app.services.host import HostService
from app.setup_db import db

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
