from .general_dao import GeneralDAO
from ..domain import AgencyRegion

class AgencyRegionDAO(GeneralDAO):
    _domain_type = AgencyRegion

    def find_all_agency_regions(self):
        agency_regions = self.find_all()
        print(f"Found agency_regions: {agency_regions}")
        return agency_regions

    def find_agency_region_by_id(self, agency_region_id):
        return self.find_by_id(agency_region_id)

    def create_agency_region(self, agency_region):
        return self.create(agency_region)

    def create_all_agency_regions(self, agency_region_list):
        return self.create_all(agency_region_list)

    def update_agency_region(self, agency_region_id, updated_agency_region):
        return self.update(agency_region_id, updated_agency_region)

    def patch_agency_region(self, agency_region_id, field_name, value):
        return self.patch(agency_region_id, field_name, value)

    def delete_agency_region(self, agency_region_id):
        return self.delete(agency_region_id)

    def delete_all_agency_regions(self):
        return self.delete_all()
