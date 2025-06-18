from typing import Optional

from pydantic import Field, BaseModel

from app.schemas.enity import BaseEntity
from app.schemas.project import ProjectBaseEntity


class ShotBaseEntity(BaseEntity):
    type: str = "Shot"


class Shot(ShotBaseEntity):
    code: Optional[str] = Field(description="The name of each individual Shot")
    description: Optional[str] = Field(None, description="A description of each individual Shot")


class ShotCreate(BaseModel):
    project: ProjectBaseEntity
    code: Optional[str] = Field(None,description="The name of each individual Shot")
    description: Optional[str] = Field(None, description="A description of each individual Shot")

    class Config:
        extra = 'ignore'


class ShotUpdate(ShotBaseEntity):
    pass



class ShotResponse(BaseModel):
    entity_id: int
    entity_type: str
    code: Optional[str] = Field(None,description="The name of each individual Shot")
    description: Optional[str] = Field(None, description="A description of each individual Shot")

    @classmethod
    def to_response(cls, shot: Shot):
        return cls(entity_id=shot.id, entity_type=shot.type, code=shot.code, description=shot.description)
