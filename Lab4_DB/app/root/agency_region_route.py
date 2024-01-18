from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import agency_region_controller
from ..domain.agency_region import AgencyRegion

agency_regions_bp = Blueprint('agency_regions', __name__, url_prefix='/agency_regions')

@agency_regions_bp.route('', methods=['GET'])
def get_all_agency_regions() -> Response:
    agency_regions = agency_region_controller.find_all_agency_regions()
    agency_regions_dtos = [ar.to_dict() for ar in agency_regions if isinstance(ar, AgencyRegion)]
    return make_response(jsonify(agency_regions_dtos), HTTPStatus.OK)

@agency_regions_bp.route('', methods=['POST'])
def create_agency_regions() -> Response:
    content = request.get_json()
    agency_regions = AgencyRegion.from_dict(content)
    agency_region_controller.create_agency_regions(agency_regions)
    return make_response(jsonify(agency_regions.to_dict()), HTTPStatus.CREATED)

@agency_regions_bp.route('/<int:agency_id>/<string:region>', methods=['GET'])
def get_agency_regions(agency_id: int, region: str) -> Response:
    return make_response(jsonify(agency_region_controller.find_agency_regions(agency_id, region)), HTTPStatus.OK)

@agency_regions_bp.route('/<int:agency_id>/<string:region>', methods=['PUT'])
def update_agency_regions(agency_id: int, region: str) -> Response:
    content = request.get_json()
    agency_regions = AgencyRegion.from_dict(content)
    agency_region_controller.update_agency_regions(agency_id, region, agency_regions)
    return make_response("Agency Regions updated", HTTPStatus.OK)

@agency_regions_bp.route('/<int:agency_id>/<string:region>', methods=['DELETE'])
def delete_agency_regions(agency_id: int, region: str) -> Response:
    agency_region_controller.delete_agency_regions(agency_id, region)
    return make_response("Agency Regions deleted", HTTPStatus.OK)
