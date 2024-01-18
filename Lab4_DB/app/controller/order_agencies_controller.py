from .general_controller import GeneralController
from ..service import order_agencies_service

class OrderAgenciesController(GeneralController):
    _service = order_agencies_service

    def find_all_order_agencies(self):
        return self.find_all()

    def find_order_agency_by_id(self, key):
        return self.find_by_id(key)

    def create_order_agency(self, order_agency):
        return self.create(order_agency)

    def create_all_order_agencies(self, order_agency_list):
        return self.create_all(order_agency_list)

    def update_order_agency(self, key, new_order_agency):
        return self.update(key, new_order_agency)

    def patch_order_agency(self, key, value_dict):
        return self.patch(key, value_dict)

    def delete_order_agency(self, key):
        return self.delete(key)

    def delete_all_order_agencies(self):
        return self.delete_all()
