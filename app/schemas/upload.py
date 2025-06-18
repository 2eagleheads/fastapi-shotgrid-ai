from typing import Optional, Literal

from pydantic import BaseModel
from pydantic import Field


class UploadBase(BaseModel):
    entity_id: int
    entity_type: str
    file_path: Optional[str] = Field(description="Full path to the file on disk")


class UploadThumbnailRequest(UploadBase):
    pass


class UploadFileRequest(UploadBase):
    field_name: str


class UploadResponse(BaseModel):
    result: str
