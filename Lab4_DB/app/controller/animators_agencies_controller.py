from .general_controller import GeneralController
from ..service import animators_agencies_service

class AnimatorsAgenciesController(GeneralController):
    _service = animators_agencies_service

    def find_all_animators_agencies(self):
        return self.find_all()

    def find_animators_agency_by_id(self, key):
        return self.find_by_id(key)

    def create_animators_agency(self, animators_agency):
        return self.create(animators_agency)

    def create_all_animators_agencies(self, animators_agency_list):
        return self.create_all(animators_agency_list)

    def update_animators_agency(self, key, new_animators_agency):
        return self.update(key, new_animators_agency)

    def patch_animators_agency(self, key, value_dict):
        return self.patch(key, value_dict)

    def delete_animators_agency(self, key):
        return self.delete(key)

    def delete_all_animators_agencies(self):
        return self.delete_all()
