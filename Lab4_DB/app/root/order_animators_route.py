from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import order_animators_controller
from ..domain.order_animators import OrderAnimators

order_animators_bp = Blueprint('order_animators', __name__, url_prefix='/order_animators')

@order_animators_bp.route('', methods=['GET'])
def get_all_order_animators() -> Response:
    order_animators = order_animators_controller.find_all_order_animators()
    order_animators_dtos = [oa.to_dict() for oa in order_animators if isinstance(oa, OrderAnimators)]
    return make_response(jsonify(order_animators_dtos), HTTPStatus.OK)

@order_animators_bp.route('', methods=['POST'])
def create_order_animators() -> Response:
    content = request.get_json()
    order_animators = OrderAnimators.from_dict(content)
    order_animators_controller.create_order_animators(order_animators)
    return make_response(jsonify(order_animators.to_dict()), HTTPStatus.CREATED)

@order_animators_bp.route('/<int:order_id>/<int:animator_id>', methods=['GET'])
def get_order_animators(order_id: int, animator_id: int) -> Response:
    return make_response(jsonify(order_animators_controller.find_order_animators(order_id, animator_id)), HTTPStatus.OK)

@order_animators_bp.route('/<int:order_id>/<int:animator_id>', methods=['PUT'])
def update_order_animators(order_id: int, animator_id: int) -> Response:
    content = request.get_json()
    order_animators = OrderAnimators.from_dict(content)
    order_animators_controller.update_order_animators(order_id, animator_id, order_animators)
    return make_response("Order Animators updated", HTTPStatus.OK)

@order_animators_bp.route('/<int:order_id>/<int:animator_id>', methods=['DELETE'])
def delete_order_animators(order_id: int, animator_id: int) -> Response:
    order_animators_controller.delete_order_animators(order_id, animator_id)
    return make_response("Order Animators deleted", HTTPStatus.OK)
