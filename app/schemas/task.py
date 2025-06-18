from typing import Optional

from pydantic import Field

from app.schemas.enity import BaseEntity
from app.schemas.project import Project


class TaskBaseEntity(BaseEntity):
    type: str = "Task"


class Task(BaseEntity):
    content: str = Field(description="Name of the task")
    sg_description: Optional[str] = Field(None, description="Task description")
    sg_status_list: Optional[str] = Field(None, description="Status of the task")
    project: Project


class TaskCreate(Task):
    pass


class TaskUpdate(Task):
    pass
