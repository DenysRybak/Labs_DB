# animator_service.py
from .general_service import GeneralService
from ..dao import animators_dao

class AnimatorsService(GeneralService):
    _dao = animators_dao

    def find_all(self):
        return self._dao.find_all_animators()

    def find_animator_by_id(self, key):
        return self._dao.find_animator_by_id(key)

    def create_animator(self, animator):
        return self._dao.create_animator(animator)

    def create_all_animators(self, animator_list):
        return self._dao.create_all_animators(animator_list)

    def update_animator(self, key, new_animator):
        return self._dao.update_animator(key, new_animator)

    def patch_animator(self, key, value_dict):
        return self._dao.patch_animator(key, value_dict)

    def delete_animator(self, key):
        return self._dao.delete_animator(key)

    def delete_all_animators(self):
        return self._dao.delete_all_animators()
