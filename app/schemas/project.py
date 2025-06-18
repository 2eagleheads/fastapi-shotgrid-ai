from typing import Optional

from pydantic import Field, computed_field, BaseModel

from app.config import settings
from app.schemas.enity import BaseEntity


class ProjectBaseEntity(BaseEntity):
    type: str = "Project"


class Project(ProjectBaseEntity):
    name: str = Field(description="Name of the project")
    code: Optional[str] = Field(None, description="Project code")
    sg_description: Optional[str] = Field(None, description="Project description")


class ProjectRequest(Project):
    pass


class ProjectResponse(Project):
    @computed_field
    def project_url(self) -> str:
        return f"{settings.shotgrid_url}/page/project_overview?project_id={self.id}"


class ProjectCreate(BaseModel):
    name: str
    tank_name: Optional[str] = Field(None)
    code: Optional[str] = Field(None)
    sg_description: Optional[str] = Field(None)

    def model_dump(self, *args, **kwargs):
        data = super().model_dump(*args, **kwargs)
        if self.tank_name is None:
            data['tank_name'] = self.name
        return data


class ProjectUpdate(Project):
    pass
