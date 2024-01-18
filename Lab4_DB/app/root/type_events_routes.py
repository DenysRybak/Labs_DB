from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import type_events_controller
from ..domain.type_events import TypeEvent

type_events_bp = Blueprint('type_events', __name__, url_prefix='/type_events')

@type_events_bp.route('', methods=['GET'])
def get_all_type_events() -> Response:
    type_events = type_events_controller.find_all_type_events()
    type_events_dtos = [type_event.to_dict() for type_event in type_events if isinstance(type_event, TypeEvent)]
    return make_response(jsonify(type_events_dtos), HTTPStatus.OK)

@type_events_bp.route('', methods=['POST'])
def create_type_event() -> Response:
    content = request.get_json()
    type_event = TypeEvent.from_dict(content)
    type_events_controller.create_type_event(type_event)
    return make_response(jsonify(type_event.to_dict()), HTTPStatus.CREATED)

@type_events_bp.route('/<int:type_event_id>', methods=['GET'])
def get_type_event(type_event_id: int) -> Response:
    return make_response(jsonify(type_events_controller.find_type_event_by_id(type_event_id)), HTTPStatus.OK)

@type_events_bp.route('/<int:type_event_id>', methods=['PUT'])
def update_type_event(type_event_id: int) -> Response:
    content = request.get_json()
    type_event = TypeEvent.from_dict(content)
    type_events_controller.update_type_event(type_event_id, type_event)
    return make_response("Type event updated", HTTPStatus.OK)

@type_events_bp.route('/<int:type_event_id>', methods=['DELETE'])
def delete_type_event(type_event_id: int) -> Response:
    type_events_controller.delete_type_event(type_event_id)
    return make_response("Type event deleted", HTTPStatus.OK)
