from .general_controller import GeneralController
from ..service import agency_region_service

class AgencyRegionController(GeneralController):
    _service = agency_region_service

    def find_all_agency_regions(self):
        return self.find_all()

    def find_agency_region_by_id(self, key):
        return self.find_by_id(key)

    def create_agency_region(self, agency_region):
        return self.create(agency_region)

    def create_all_agency_regions(self, agency_region_list):
        return self.create_all(agency_region_list)

    def update_agency_region(self, key, new_agency_region):
        return self.update(key, new_agency_region)

    def patch_agency_region(self, key, value_dict):
        return self.patch(key, value_dict)

    def delete_agency_region(self, key):
        return self.delete(key)

    def delete_all_agency_regions(self):
        return self.delete_all()
