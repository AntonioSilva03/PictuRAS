from flask import Blueprint, request, jsonify # type: ignore
from controllers.tool import (
    list_tools,
    insert_tool,
    find_by_id,
    update_tool,
    delete_tool,
)

tools_blueprint = Blueprint('tool', __name__)


@tools_blueprint.route('/', methods=['GET'])
def rout_get_tools():
    tools = list_tools()
    return jsonify([tool.to_json() for tool in tools]), 200


@tools_blueprint.route('/<string:tool_name>', methods=['GET'])
def rout_get_tool(tool_name: str):
    tool = find_by_id(tool_name)
    if tool:
        return jsonify(tool.to_json()), 200
    return jsonify({"error": "Tool not found"}), 404


@tools_blueprint.route('/', methods=['POST'])
def rout_insert_tool():
    tool_data = request.json
    tool = insert_tool(tool_data)
    if tool:
        return jsonify(tool.to_json()), 200
    return jsonify({"error": "Invalid data"}), 500


@tools_blueprint.route('/<string:tool_name>', methods=['PUT'])
def rout_update_tool(tool_name: str):
    tool_data = request.json
    tool = update_tool(tool_name, tool_data)
    if tool:
        return jsonify(tool.to_json()), 200
    return jsonify({"error": "Tool not found"}), 500


@tools_blueprint.route('/<string:tool_name>', methods=['DELETE'])
def rout_delete_tool(tool_name: str):
    tool = delete_tool(tool_name)
    if tool:
        return jsonify(tool.to_json()), 200
    return jsonify({"error": "Tool not found"}), 500