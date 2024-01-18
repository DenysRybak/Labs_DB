from .general_dao import GeneralDAO
from ..domain import AnimatorsAgencies

class AnimatorsAgenciesDAO(GeneralDAO):
    _domain_type = AnimatorsAgencies

    def find_all_animators_agencies(self):
        animators_agencies = self.find_all()
        print(f"Found animators_agencies: {animators_agencies}")
        return animators_agencies

    def find_animators_agencies_by_id(self, animators_agencies_id):
        return self.find_by_id(animators_agencies_id)

    def create_animators_agencies(self, animators_agencies):
        return self.create(animators_agencies)

    def create_all_animators_agencies(self, animators_agencies_list):
        return self.create_all(animators_agencies_list)

    def update_animators_agencies(self, animators_agencies_id, updated_animators_agencies):
        return self.update(animators_agencies_id, updated_animators_agencies)

    def patch_animators_agencies(self, animators_agencies_id, field_name, value):
        return self.patch(animators_agencies_id, field_name, value)

    def delete_animators_agencies(self, animators_agencies_id):
        return self.delete(animators_agencies_id)

    def delete_all_animators_agencies(self):
        return self.delete_all()
