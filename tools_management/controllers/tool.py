from typing import Optional, List, Dict, Any
from models.tool import Tool
import traceback


def list_tools() -> List[Tool]:
    return Tool.objects()


def find_by_id(tool_name: str) -> Optional[Tool]:

    try:
        return Tool.objects.get(name=tool_name)

    except Exception:
        traceback.print_exc()
        return None


def insert_tool(tool_data: Dict[str, Any]) -> Optional[Tool]:

    try:

        new_tool = Tool(**tool_data)

        if Tool.objects.filter(name=new_tool.name):
            raise Exception('Tool alredy inserted')

        new_tool.save()
        return new_tool

    except Exception:
        traceback.print_exc()
        return None


def update_tool(tool_name: str, tool_data: Dict[str, Any]) -> Optional[Tool]:

    try:
        tool = Tool.objects.get(name=tool_name)
        tool.update(**tool_data)
        return Tool.objects.get(name=tool_name)

    except Exception:
        return None


def delete_tool(tool_name: str) -> Optional[Tool]:

    try:
        tool = Tool.objects.get(name=tool_name)
        tool.delete()
        return tool

    except Exception:
        return None