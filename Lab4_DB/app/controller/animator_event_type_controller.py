from .general_controller import GeneralController
from ..service import animator_event_type_service

class AnimatorEventTypeController(GeneralController):
    _service = animator_event_type_service

    def find_all_animator_event_types(self):
        return self.find_all()

    def find_animator_event_type_by_id(self, key):
        return self.find_by_id(key)

    def create_animator_event_type(self, animator_event_type):
        return self.create(animator_event_type)

    def create_all_animator_event_types(self, animator_event_type_list):
        return self.create_all(animator_event_type_list)

    def update_animator_event_type(self, key, new_animator_event_type):
        return self.update(key, new_animator_event_type)

    def patch_animator_event_type(self, key, value_dict):
        return self.patch(key, value_dict)

    def delete_animator_event_type(self, key):
        return self.delete(key)

    def delete_all_animator_event_types(self):
        return self.delete_all()
