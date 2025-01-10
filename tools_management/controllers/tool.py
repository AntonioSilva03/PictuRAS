from typing import Optional, List, Dict, Any
from models.tool import Tool
import traceback


def list_tools() -> List[Tool]:
    return Tool.objects()


def find_by_id(tool_id: str) -> Optional[Tool]:

    try:
        print(tool_id)
        return Tool.objects.get(name=tool_id)

    except Exception:
        traceback.print_exc()
        return None


def insert_tool(tool_data: Dict[str, Any]) -> Optional[Tool]:

    try:

        print(tool_data)
        new_tool = Tool(**tool_data)

        if Tool.objects.filter(name=new_tool.id):
            raise Exception('Tool alredy inserted')

        new_tool.save()
        return new_tool

    except Exception:
        traceback.print_exc()
        return None


def update_tool(tool_id: str, tool_data: Dict[str, Any]) -> Optional[Tool]:

    try:
        tool = Tool.objects.get(name=tool_id)
        tool.update(**tool_data)
        return Tool.objects.get(name=tool_id)

    except Exception:
        return None


def delete_tool(tool_id: str) -> Optional[Tool]:

    try:
        tool = Tool.objects.get(name=tool_id)
        tool.delete()
        return tool

    except Exception:
        return None