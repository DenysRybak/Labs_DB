from .general_service import GeneralService
from ..dao import type_events_dao

class TypeEventsService(GeneralService):
    _dao = type_events_dao

    def find_all(self):
        return self._dao.find_all_type_events()

    def find_type_event_by_id(self, key):
        return self._dao.find_type_event_by_id(key)

    def create_type_event(self, type_event):
        return self._dao.create_type_event(type_event)

    def create_all_type_events(self, type_event_list):
        return self._dao.create_all_type_events(type_event_list)

    def update_type_event(self, key, new_type_event):
        return self._dao.update_type_event(key, new_type_event)

    def patch_type_event(self, key, value_dict):
        return self._dao.patch_type_event(key, value_dict)

    def delete_type_event(self, key):
        return self._dao.delete_type_event(key)

    def delete_all_type_events(self):
        return self._dao.delete_all_type_events()
