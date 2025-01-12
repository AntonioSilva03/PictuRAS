from flask import Blueprint, request, jsonify # type: ignore
from models.project import Project
from controllers.project import *

projects_blueprint = Blueprint('project', __name__)


@projects_blueprint.route('/', methods=['GET'])
def route_get_projects():
    projects = list_projects()
    return jsonify([project.to_json() for project in projects]), 200


@projects_blueprint.route('/<string:project_id>', methods=['GET'])
def route_get_project(project_id: str):
    project = find_by_id(project_id)
    if project:
        return jsonify(project.to_json()), 200
    return jsonify({'error': 'Project not found'}), 404


@projects_blueprint.route('/user/<string:user_id>', methods=['GET'])
def route_get_user_projects(user_id: str):
    projects = find_user_projects(user_id)
    return jsonify([project.to_json() for project in projects]), 200


@projects_blueprint.route('/', methods=['POST'])
def route_insert_project():
    project = Project(**request.json)
    project = insert_project(project)
    if project:
        return jsonify(project.to_json()), 200
    return jsonify({'error': 'Invalid data'}), 500


@projects_blueprint.route('/<string:project_id>', methods=['PUT'])
def route_update_project(project_id: str):
    project = update_project(project_id,request.json)
    if project:
        return jsonify(project.to_json()), 200
    return jsonify({'error': 'Invalid data'}), 500


@projects_blueprint.route('/<string:project_id>', methods=['DELETE'])
def route_delete_(project_id: str):
    project = delete_project(project_id)
    if project:
        return jsonify(project.to_json()), 200
    return jsonify({'error': 'Project not found'}), 500