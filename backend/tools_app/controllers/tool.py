from typing import Optional, List, Dict, Any
from models.tool import Tool


def list_tools() -> List[Tool]:
    return Tool.objects()


def find_by_id(tool_name: str) -> Optional[Tool]:
    return Tool.objects.get(name=tool_name)


def insert_tool(tool: Tool) -> Optional[Tool]:
    tool.save()
    return tool


def update_tool(tool_name: str, tool_data: Dict[str, Any]) -> Optional[Tool]:
    tool = Tool.objects.get(name=tool_name)
    tool.update(**tool_data)
    return Tool.objects.get(name=tool_name)


def delete_tool(tool_name: str) -> Optional[Tool]:
    tool = Tool.objects.get(name=tool_name)
    tool.delete()
    return tool