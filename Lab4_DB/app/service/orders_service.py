from .general_service import GeneralService
from ..dao import orders_dao

class OrderService(GeneralService):
    _dao = orders_dao

    def find_all(self):
        return self._dao.find_all_orders()

    def find_order_by_id(self, order_id):
        return self._dao.find_by_id(order_id)

    def create_order(self, order):
        return self._dao.create(order)

    def create_all_orders(self, order_list):
        return self._dao.create_all(order_list)

    def update_order(self, order_id, updated_order):
        return self._dao.update(order_id, updated_order)

    def patch_order(self, order_id, field_name, value):
        return self._dao.patch(order_id, field_name, value)

    def delete_order(self, order_id):
        return self._dao.delete(order_id)

    def delete_all_orders(self):
        return self._dao.delete_all()
