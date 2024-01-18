from .general_controller import GeneralController
from ..service import order_days_service

class OrderDaysController(GeneralController):
    _service = order_days_service

    def find_all_order_days(self):
        return self.find_all()

    def find_order_days_by_id(self, key):
        return self.find_by_id(key)

    def create_order_days(self, order_days):
        return self.create(order_days)

    def create_all_order_days(self, order_days_list):
        return self.create_all(order_days_list)

    def update_order_days(self, key, new_order_days):
        return self.update(key, new_order_days)

    def patch_order_days(self, key, value_dict):
        return self.patch(key, value_dict)

    def delete_order_days(self, key):
        return self.delete(key)

    def delete_all_order_days(self):
        return self.delete_all()
