from .general_dao import GeneralDAO
from ..domain import TypeEvent


class TypeEventDAO(GeneralDAO):
    _domain_type = TypeEvent

    def find_all_type_events(self):
        type_events = self.find_all()
        print(f"Found type events: {type_events}")
        return type_events

    def find_type_event_by_id(self, type_event_id):
        return self.find_by_id(type_event_id)

    def create_type_event(self, type_event):
        return self.create(type_event)

    def create_all_type_events(self, type_event_list):
        return self.create_all(type_event_list)

    def update_type_event(self, type_event_id, updated_type_event):
        return self.update(type_event_id, updated_type_event)

    def patch_type_event(self, type_event_id, field_name, value):
        return self.patch(type_event_id, field_name, value)

    def delete_type_event(self, type_event_id):
        return self.delete(type_event_id)

    def delete_all_type_events(self):
        return self.delete_all()
