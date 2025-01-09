from typing import Optional, List, Dict, Any
from models.tool import Tool


def list_tools() -> List[Tool]:
    return Tool.objects()


def find_by_id(tool_id: str) -> Optional[Tool]:

    try:
        return Tool.objects.get(id=tool_id)

    except Exception:
        return None


def insert_tool(tool_data: Dict[str, Any]) -> Optional[Tool]:

    try:

        new_tool = Tool(**tool_data)

        if Tool.objects.filter(id=new_tool.id):
            raise Exception('Tool alredy inserted')

        new_tool.save()
        return new_tool    

    except Exception:
        return None


def update_tool(tool_id: str, tool_data: Dict[str, Any]) -> Optional[Tool]:

    try:
        tool = Tool.objects.get(id=tool_id)
        tool.update(**tool_data)
        return Tool.objects.get(id=tool_id)

    except Exception:
        return None


def delete_tool(tool_id: str) -> Optional[Tool]:

    try:
        tool = Tool.objects.get(id=tool_id)
        tool.delete()
        return tool

    except Exception:
        return None