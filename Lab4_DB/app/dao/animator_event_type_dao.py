from .general_dao import GeneralDAO
from ..domain import AnimatorEventType

class AnimatorEventTypeDAO(GeneralDAO):
    _domain_type = AnimatorEventType

    def find_all_animator_event_types(self):
        animator_event_types = self.find_all()
        print(f"Found animator_event_types: {animator_event_types}")
        return animator_event_types

    def find_animator_event_type_by_id(self, animator_event_type_id):
        return self.find_by_id(animator_event_type_id)

    def create_animator_event_type(self, animator_event_type):
        return self.create(animator_event_type)

    def create_all_animator_event_types(self, animator_event_type_list):
        return self.create_all(animator_event_type_list)

    def update_animator_event_type(self, animator_event_type_id, updated_animator_event_type):
        return self.update(animator_event_type_id, updated_animator_event_type)

    def patch_animator_event_type(self, animator_event_type_id, field_name, value):
        return self.patch(animator_event_type_id, field_name, value)

    def delete_animator_event_type(self, animator_event_type_id):
        return self.delete(animator_event_type_id)

    def delete_all_animator_event_types(self):
        return self.delete_all()
