from typing import Optional, List
from models.project import Project


def list_projects() -> List[Project]:
    return Project.objects()


def find_by_id(project_id: str) -> Optional[Project]:
    try:
        return Project.objects.get(id=project_id)
    except Exception:
        return None


def find_user_projects(user_id: str) -> List[Project]:
    return Project.objects.filter(owner=user_id)


def insert_project(project: Project) -> Optional[Project]:
    try:
        project.save()
        return project
    except Exception:
        return None


def update_project(project_id: str, project: dict) -> Optional[Project]:
    try:
        old_project = Project.objects.get(id=project_id)
        old_project.update(**project)
        return Project.objects.get(id=project_id)
    except Exception:
        return None


def delete_project(project_id: str) -> Optional[Project]:
    try:
        project = Project.objects.get(id=project_id)
        project.delete()
        return project
    except Exception:
        return None