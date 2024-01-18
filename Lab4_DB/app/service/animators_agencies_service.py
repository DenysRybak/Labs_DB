from .general_service import GeneralService
from ..dao import animators_agencies_dao

class AnimatorsAgenciesService(GeneralService):
    _dao = animators_agencies_dao

    def find_all(self):
        return self._dao.find_all_animators_agencies()

    def find_animator_agency_by_id(self, animator_id, agency_id):
        return self._dao.find_animator_agency_by_id(animator_id, agency_id)

    def create_animator_agency(self, animator_agency):
        return self._dao.create_animator_agency(animator_agency)

    def create_all_animators_agencies(self, animator_agency_list):
        return self._dao.create_all_animators_agencies(animator_agency_list)

    def update_animator_agency(self, animator_id, agency_id, updated_animator_agency):
        return self._dao.update_animator_agency(animator_id, agency_id, updated_animator_agency)

    def patch_animator_agency(self, animator_id, agency_id, field_name, value):
        return self._dao.patch_animator_agency(animator_id, agency_id, field_name, value)

    def delete_animator_agency(self, animator_id, agency_id):
        return self._dao.delete_animator_agency(animator_id, agency_id)

    def delete_all_animators_agencies(self):
        return self._dao.delete_all_animators_agencies()
