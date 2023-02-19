from app.dao.apartments import ApartmentsDAO


class ApartmentsService:
    def __init__(self, dao: ApartmentsDAO):
        self.dao = dao

    def get_one(self, aid):
        return self.dao.get_one(aid)

    def get_all(self):
        result = []
        all_apartment = self.dao.get_all()
        for apartment, host, location in all_apartment:
            apartment = apartment.to_dict()
            host = host.to_dict()
            location = location.to_dict()
            apartment.update(host)
            apartment.update(location)
            #
            # features_on = apartments_features_service.get_on(apartment['pk'])
            # features_off = apartments_features_service.get_off(
            #     apartment['pk']
            # )
            #
            # features_on = [feature[1] for feature in features_on]
            # features_off = [feature[1] for feature in features_off]
            # apartment['features_on'] = features_on
            # apartment['features_off'] = features_off
            result.append(apartment)

        return result
