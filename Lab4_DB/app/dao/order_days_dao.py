from .general_dao import GeneralDAO
from ..domain import OrderDays

class OrderDaysDAO(GeneralDAO):
    _domain_type = OrderDays

    def find_all_order_days(self):
        order_days = self.find_all()
        print(f"Found order_days: {order_days}")
        return order_days

    def find_order_day_by_id(self, order_day_id):
        return self.find_by_id(order_day_id)

    def create_order_day(self, order_day):
        return self.create(order_day)

    def create_all_order_days(self, order_day_list):
        return self.create_all(order_day_list)

    def update_order_day(self, order_day_id, updated_order_day):
        return self.update(order_day_id, updated_order_day)

    def patch_order_day(self, order_day_id, field_name, value):
        return self.patch(order_day_id, field_name, value)

    def delete_order_day(self, order_day_id):
        return self.delete(order_day_id)

    def delete_all_order_days(self):
        return self.delete_all()
