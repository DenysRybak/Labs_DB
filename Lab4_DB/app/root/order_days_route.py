from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import order_days_controller
from ..domain.order_days import OrderDays

order_days_bp = Blueprint('order_days', __name__, url_prefix='/order_days')

@order_days_bp.route('', methods=['GET'])
def get_all_order_days() -> Response:
    order_days = order_days_controller.find_all_order_days()
    order_days_dtos = [od.to_dict() for od in order_days if isinstance(od, OrderDays)]
    return make_response(jsonify(order_days_dtos), HTTPStatus.OK)

@order_days_bp.route('', methods=['POST'])
def create_order_days() -> Response:
    content = request.get_json()
    order_days = OrderDays.from_dict(content)
    order_days_controller.create_order_days(order_days)
    return make_response(jsonify(order_days.to_dict()), HTTPStatus.CREATED)

@order_days_bp.route('/<int:order_id>/<int:animator_id>', methods=['GET'])
def get_order_days(order_id: int, animator_id: int) -> Response:
    return make_response(jsonify(order_days_controller.find_order_days(order_id, animator_id)), HTTPStatus.OK)

@order_days_bp.route('/<int:order_id>/<int:animator_id>', methods=['PUT'])
def update_order_days(order_id: int, animator_id: int) -> Response:
    content = request.get_json()
    order_days = OrderDays.from_dict(content)
    order_days_controller.update_order_days(order_id, animator_id, order_days)
    return make_response("Order Days updated", HTTPStatus.OK)

@order_days_bp.route('/<int:order_id>/<int:animator_id>', methods=['DELETE'])
def delete_order_days(order_id: int, animator_id: int) -> Response:
    order_days_controller.delete_order_days(order_id, animator_id)
    return make_response("Order Days deleted", HTTPStatus.OK)
