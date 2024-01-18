from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import animators_agencies_controller
from ..domain.animators_agencies import AnimatorsAgencies

animators_agencies_bp = Blueprint('animators_agencies', __name__, url_prefix='/animators_agencies')

@animators_agencies_bp.route('', methods=['GET'])
def get_all_animators_agencies() -> Response:
    animators_agencies = animators_agencies_controller.find_all_animators_agencies()
    animators_agencies_dtos = [aa.to_dict() for aa in animators_agencies if isinstance(aa, AnimatorsAgencies)]
    return make_response(jsonify(animators_agencies_dtos), HTTPStatus.OK)

@animators_agencies_bp.route('', methods=['POST'])
def create_animators_agencies() -> Response:
    content = request.get_json()
    animators_agencies = AnimatorsAgencies.from_dict(content)
    animators_agencies_controller.create_animators_agencies(animators_agencies)
    return make_response(jsonify(animators_agencies.to_dict()), HTTPStatus.CREATED)

@animators_agencies_bp.route('/<int:agency_id>/<int:animator_id>', methods=['GET'])
def get_animators_agencies(agency_id: int, animator_id: int) -> Response:
    return make_response(jsonify(animators_agencies_controller.find_animators_agencies(agency_id, animator_id)), HTTPStatus.OK)

@animators_agencies_bp.route('/<int:agency_id>/<int:animator_id>', methods=['PUT'])
def update_animators_agencies(agency_id: int, animator_id: int) -> Response:
    content = request.get_json()
    animators_agencies = AnimatorsAgencies.from_dict(content)
    animators_agencies_controller.update_animators_agencies(agency_id, animator_id, animators_agencies)
    return make_response("Animators Agencies updated", HTTPStatus.OK)

@animators_agencies_bp.route('/<int:agency_id>/<int:animator_id>', methods=['DELETE'])
def delete_animators_agencies(agency_id: int, animator_id: int) -> Response:
    animators_agencies_controller.delete_animators_agencies(agency_id, animator_id)
    return make_response("Animators Agencies deleted", HTTPStatus.OK)
