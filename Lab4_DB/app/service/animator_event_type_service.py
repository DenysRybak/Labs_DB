from .general_service import GeneralService
from ..dao import animator_event_type_dao

class AnimatorEventTypeService(GeneralService):
    _dao = animator_event_type_dao

    def find_all(self):
        return self._dao.find_all_animator_event_types()

    def find_animator_event_type_by_id(self, animator_event_type_id):
        return self._dao.find_by_id(animator_event_type_id)

    def create_animator_event_type(self, animator_event_type):
        return self._dao.create(animator_event_type)

    def create_all_animator_event_types(self, animator_event_type_list):
        return self._dao.create_all(animator_event_type_list)

    def update_animator_event_type(self, animator_event_type_id, updated_animator_event_type):
        return self._dao.update(animator_event_type_id, updated_animator_event_type)

    def patch_animator_event_type(self, animator_event_type_id, field_name, value):
        return self._dao.patch(animator_event_type_id, field_name, value)

    def delete_animator_event_type(self, animator_event_type_id):
        return self._dao.delete(animator_event_type_id)

    def delete_all_animator_event_types(self):
        return self._dao.delete_all()
