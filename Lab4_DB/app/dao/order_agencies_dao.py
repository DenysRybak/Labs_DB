from .general_dao import GeneralDAO
from ..domain import OrderAgencies

class OrderAgenciesDAO(GeneralDAO):
    _domain_type = OrderAgencies

    def find_all_order_agencies(self):
        order_agencies = self.find_all()
        print(f"Found order_agencies: {order_agencies}")
        return order_agencies

    def find_order_agencies_by_id(self, order_agencies_id):
        return self.find_by_id(order_agencies_id)

    def create_order_agencies(self, order_agencies):
        return self.create(order_agencies)

    def create_all_order_agencies(self, order_agencies_list):
        return self.create_all(order_agencies_list)

    def update_order_agencies(self, order_agencies_id, updated_order_agencies):
        return self.update(order_agencies_id, updated_order_agencies)

    def patch_order_agencies(self, order_agencies_id, field_name, value):
        return self.patch(order_agencies_id, field_name, value)

    def delete_order_agencies(self, order_agencies_id):
        return self.delete(order_agencies_id)

    def delete_all_order_agencies(self):
        return self.delete_all()
