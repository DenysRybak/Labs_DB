from .general_service import GeneralService
from ..dao import agency_region_dao

class AgencyRegionService(GeneralService):
    _dao = agency_region_dao

    def find_all(self):
        return self._dao.find_all_agency_regions()

    def find_agency_region_by_id(self, agency_region_id):
        return self._dao.find_by_id(agency_region_id)

    def create_agency_region(self, agency_region):
        return self._dao.create(agency_region)

    def create_all_agency_regions(self, agency_region_list):
        return self._dao.create_all(agency_region_list)

    def update_agency_region(self, agency_region_id, updated_agency_region):
        return self._dao.update(agency_region_id, updated_agency_region)

    def patch_agency_region(self, agency_region_id, field_name, value):
        return self._dao.patch(agency_region_id, field_name, value)

    def delete_agency_region(self, agency_region_id):
        return self._dao.delete(agency_region_id)

    def delete_all_agency_regions(self):
        return self._dao.delete_all()
