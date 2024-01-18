from .general_service import GeneralService
from ..dao import order_days_dao

class OrderDaysService(GeneralService):
    _dao = order_days_dao

    def find_all(self):
        return self._dao.find_all_order_days()

    def find_order_day_by_id(self, order_day_id):
        return self._dao.find_order_day_by_id(order_day_id)

    def create_order_day(self, order_day):
        return self._dao.create_order_day(order_day)

    def create_all_order_days(self, order_day_list):
        return self._dao.create_all_order_days(order_day_list)

    def update_order_day(self, order_day_id, updated_order_day):
        return self._dao.update_order_day(order_day_id, updated_order_day)

    def patch_order_day(self, order_day_id, field_name, value):
        return self._dao.patch_order_day(order_day_id, field_name, value)

    def delete_order_day(self, order_day_id):
        return self._dao.delete_order_day(order_day_id)

    def delete_all_order_days(self):
        return self._dao.delete_all_order_days()
