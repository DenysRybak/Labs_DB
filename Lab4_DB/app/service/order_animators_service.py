from .general_service import GeneralService
from ..dao import order_animators_dao

class OrderAnimatorsService(GeneralService):
    _dao = order_animators_dao

    def find_all(self):
        return self._dao.find_all_order_animators()

    def find_order_animator_by_id(self, order_animator_id):
        return self._dao.find_order_animator_by_id(order_animator_id)

    def create_order_animator(self, order_animator):
        return self._dao.create_order_animator(order_animator)

    def create_all_order_animators(self, order_animator_list):
        return self._dao.create_all_order_animators(order_animator_list)

    def update_order_animator(self, order_animator_id, updated_order_animator):
        return self._dao.update_order_animator(order_animator_id, updated_order_animator)

    def patch_order_animator(self, order_animator_id, field_name, value):
        return self._dao.patch_order_animator(order_animator_id, field_name, value)

    def delete_order_animator(self, order_animator_id):
        return self._dao.delete_order_animator(order_animator_id)

    def delete_all_order_animators(self):
        return self._dao.delete_all_order_animators()
