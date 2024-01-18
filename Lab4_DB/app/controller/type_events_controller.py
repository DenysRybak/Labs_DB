from .general_controller import GeneralController
from ..service import type_events_service

class TypeEventController(GeneralController):
    _service = type_events_service

    def find_all_type_events(self):
        return self.find_all()

    def find_type_event_by_id(self, key):
        return self.find_by_id(key)

    def create_type_event(self, type_event):
        return self.create(type_event)

    def create_all_type_events(self, type_event_list):
        return self.create_all(type_event_list)

    def update_type_event(self, key, new_type_event):
        return self.update(key, new_type_event)

    def patch_type_event(self, key, value_dict):
        return self.patch(key, value_dict)

    def delete_type_event(self, key):
        return self.delete(key)

    def delete_all_type_events(self):
        return self.delete_all()
