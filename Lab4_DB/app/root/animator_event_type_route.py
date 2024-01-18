from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import animator_event_type_controller
from ..domain.animator_event_type import AnimatorEventType

animator_event_types_bp = Blueprint('animator_event_types', __name__, url_prefix='/animator_event_types')

@animator_event_types_bp.route('', methods=['GET'])
def get_all_animator_event_types() -> Response:
    animator_event_types = animator_event_type_controller.find_all_animator_event_types()
    animator_event_types_dtos = [aet.to_dict() for aet in animator_event_types if isinstance(aet, AnimatorEventType)]
    return make_response(jsonify(animator_event_types_dtos), HTTPStatus.OK)

@animator_event_types_bp.route('', methods=['POST'])
def create_animator_event_types() -> Response:
    content = request.get_json()
    animator_event_types = AnimatorEventType.from_dict(content)
    animator_event_type_controller.create_animator_event_types(animator_event_types)
    return make_response(jsonify(animator_event_types.to_dict()), HTTPStatus.CREATED)

@animator_event_types_bp.route('/<int:animator_id>/<int:type_event_id>', methods=['GET'])
def get_animator_event_types(animator_id: int, type_event_id: int) -> Response:
    return make_response(jsonify(animator_event_type_controller.find_animator_event_types(animator_id, type_event_id)), HTTPStatus.OK)

@animator_event_types_bp.route('/<int:animator_id>/<int:type_event_id>', methods=['PUT'])
def update_animator_event_types(animator_id: int, type_event_id: int) -> Response:
    content = request.get_json()
    animator_event_types = AnimatorEventType.from_dict(content)
    animator_event_type_controller.update_animator_event_types(animator_id, type_event_id, animator_event_types)
    return make_response("Animator Event Types updated", HTTPStatus.OK)

@animator_event_types_bp.route('/<int:animator_id>/<int:type_event_id>', methods=['DELETE'])
def delete_animator_event_types(animator_id: int, type_event_id: int) -> Response:
    animator_event_type_controller.delete_animator_event_types(animator_id, type_event_id)
    return make_response("Animator Event Types deleted", HTTPStatus.OK)
