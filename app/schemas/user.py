from typing import Optional

from pydantic import Field

from app.schemas.enity import BaseEntity


class UserBaseEntity(BaseEntity):
    type: str = "User"


class User(UserBaseEntity):
    name: str = Field(description="Name of the user")
    login: str
    email: Optional[str] = Field(None, description="Email address of the user")
    role: Optional[str] = Field(None, description="Role of the user")
    sg_status_list: str


class UserCreate(User):
    pass


class UserUpdate(User):
    pass
