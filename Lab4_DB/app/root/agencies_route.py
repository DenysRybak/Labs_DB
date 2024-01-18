from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import agencies_controller
from ..domain.agencies import Agency

agency_bp = Blueprint('agencies', __name__, url_prefix='/agencies')

@agency_bp.route('', methods=['GET'])
def get_all_agencies() -> Response:
    agencies = agencies_controller.find_all_agencies()
    agency_dtos = [agency.to_dict() for agency in agencies if isinstance(agency, Agency)]
    return make_response(jsonify(agency_dtos), HTTPStatus.OK)

@agency_bp.route('', methods=['POST'])
def create_agency() -> Response:
    content = request.get_json()
    agency = Agency.from_dict(content)
    agencies_controller.create_agency(agency)
    return make_response(jsonify(agency.to_dict()), HTTPStatus.CREATED)

@agency_bp.route('/<int:agency_id>', methods=['GET'])
def get_agency(agency_id: int) -> Response:
    return make_response(jsonify(agencies_controller.find_agency_by_id(agency_id)), HTTPStatus.OK)

@agency_bp.route('/<int:agency_id>', methods=['PUT'])
def update_agency(agency_id: int) -> Response:
    content = request.get_json()
    agency = Agency.from_dict(content)
    agencies_controller.update_agency(agency_id, agency)
    return make_response("Agency updated", HTTPStatus.OK)

@agency_bp.route('/<int:agency_id>', methods=['DELETE'])
def delete_agency(agency_id: int) -> Response:
    agencies_controller.delete_agency(agency_id)
    return make_response("Agency deleted", HTTPStatus.OK)
