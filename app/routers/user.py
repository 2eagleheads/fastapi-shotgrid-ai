from typing import List

from fastapi import APIRouter, Depends

from app.schemas.user import User, UserCreate, UserUpdate
from app.services.shotgrid import ShotgridService

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[User], operation_id="get_users")
async def get_users(service: ShotgridService = Depends()):
    return service.get_users()


@router.get("/{user_id}", response_model=User, operation_id="get_user_by_id")
async def get_user(user_id: int, service: ShotgridService = Depends()):
    return service.get_user_by_id(user_id)


@router.post("/", response_model=User, operation_id="create_user")
async def create_user(user: UserCreate, service: ShotgridService = Depends()):
    return service.create_user(user)


@router.put("/{user_id}", response_model=User, operation_id="update_user")
async def update_user(user_id: int, user: UserUpdate, service: ShotgridService = Depends()):
    return service.update_user(user_id, user)


@router.delete("/{user_id}", operation_id="delete_user")
async def delete_user(user_id: int, service: ShotgridService = Depends()):
    service.delete_user(user_id)
    return {"message": "User deleted successfully"}
