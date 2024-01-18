from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import order_agencies_controller
from ..domain.order_agencies import OrderAgencies

order_agencies_bp = Blueprint('order_agencies', __name__, url_prefix='/order_agencies')

@order_agencies_bp.route('', methods=['GET'])
def get_all_order_agencies() -> Response:
    order_agencies = order_agencies_controller.find_all_order_agencies()
    order_agencies_dtos = [oa.to_dict() for oa in order_agencies if isinstance(oa, OrderAgencies)]
    return make_response(jsonify(order_agencies_dtos), HTTPStatus.OK)

@order_agencies_bp.route('', methods=['POST'])
def create_order_agencies() -> Response:
    content = request.get_json()
    order_agencies = OrderAgencies.from_dict(content)
    order_agencies_controller.create_order_agencies(order_agencies)
    return make_response(jsonify(order_agencies.to_dict()), HTTPStatus.CREATED)

@order_agencies_bp.route('/<int:order_id>/<int:agency_id>', methods=['GET'])
def get_order_agencies(order_id: int, agency_id: int) -> Response:
    return make_response(jsonify(order_agencies_controller.find_order_agencies(order_id, agency_id)), HTTPStatus.OK)

@order_agencies_bp.route('/<int:order_id>/<int:agency_id>', methods=['PUT'])
def update_order_agencies(order_id: int, agency_id: int) -> Response:
    content = request.get_json()
    order_agencies = OrderAgencies.from_dict(content)
    order_agencies_controller.update_order_agencies(order_id, agency_id, order_agencies)
    return make_response("Order Agencies updated", HTTPStatus.OK)

@order_agencies_bp.route('/<int:order_id>/<int:agency_id>', methods=['DELETE'])
def delete_order_agencies(order_id: int, agency_id: int) -> Response:
    order_agencies_controller.delete_order_agencies(order_id, agency_id)
    return make_response("Order Agencies deleted", HTTPStatus.OK)
