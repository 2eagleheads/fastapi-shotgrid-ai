from typing import Optional, Dict

from pydantic import Field

from app.schemas.enity import BaseEntity
from app.schemas.project import Project


class AssetBaseEntity(BaseEntity):
    type: str = "Asset"

class Asset(AssetBaseEntity):
    code: Optional[str] = Field(description="The name of each individual Asset")
    description: Optional[str] = Field(None, description="Asset description")
    project: Project


class AssetCreate(Asset):
    pass


class AssetUpdate(Asset):
    pass

