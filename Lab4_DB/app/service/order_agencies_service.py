from .general_service import GeneralService
from ..dao import order_agencies_dao

class OrderAgenciesService(GeneralService):
    _dao = order_agencies_dao

    def find_all(self):
        return self._dao.find_all_order_agencies()

    def find_order_agency_by_id(self, order_agency_id):
        return self._dao.find_order_agency_by_id(order_agency_id)

    def create_order_agency(self, order_agency):
        return self._dao.create_order_agency(order_agency)

    def create_all_order_agencies(self, order_agency_list):
        return self._dao.create_all_order_agencies(order_agency_list)

    def update_order_agency(self, order_agency_id, updated_order_agency):
        return self._dao.update_order_agency(order_agency_id, updated_order_agency)

    def patch_order_agency(self, order_agency_id, field_name, value):
        return self._dao.patch_order_agency(order_agency_id, field_name, value)

    def delete_order_agency(self, order_agency_id):
        return self._dao.delete_order_agency(order_agency_id)

    def delete_all_order_agencies(self):
        return self._dao.delete_all_order_agencies()
