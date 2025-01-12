from flask import Blueprint, request, jsonify # type: ignore
from controllers.tool import *

tools_blueprint = Blueprint('tool', __name__)


@tools_blueprint.route('/', methods=['GET'])
def route_get_tools():
    tools = list_tools()
    return jsonify([tool.to_json() for tool in tools]), 200


@tools_blueprint.route('/<string:tool_name>', methods=['GET'])
def route_get_tool(tool_name: str):
    tool = find_by_id(tool_name)
    if tool:
        return jsonify(tool.to_json()), 200
    return jsonify({"error": "Tool not found"}), 404


@tools_blueprint.route('/', methods=['POST'])
def route_insert_tool():
    tool_data = request.json
    tool = insert_tool(tool_data)
    if tool:
        return jsonify(tool.to_json()), 200
    return jsonify({"error": "Invalid data"}), 500


@tools_blueprint.route('/<string:tool_name>', methods=['PUT'])
def route_update_tool(tool_name: str):
    tool_data = request.json
    tool = update_tool(tool_name, tool_data)
    if tool:
        return jsonify(tool.to_json()), 200
    return jsonify({"error": "Tool not found"}), 500


@tools_blueprint.route('/<string:tool_name>', methods=['DELETE'])
def route_delete_tool(tool_name: str):
    tool = delete_tool(tool_name)
    if tool:
        return jsonify(tool.to_json()), 200
    return jsonify({"error": "Tool not found"}), 500