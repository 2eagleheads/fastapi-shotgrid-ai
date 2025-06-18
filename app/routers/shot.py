from typing import List

from fastapi import APIRouter, Depends

from app.schemas.shot import Shot, ShotCreate, ShotUpdate, ShotResponse
from app.services.shotgrid import ShotgridService

router = APIRouter(
    prefix="/shots",
    tags=["shots"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[Shot], operation_id="get_shots")
async def get_shots(service: ShotgridService = Depends()):
    return service.get_shots()


@router.get("/{shot_id}", response_model=ShotResponse, operation_id="get_shot_by_id")
async def get_shot(shot_id: int, service: ShotgridService = Depends()):
    shot = service.get_shot_by_id(shot_id)
    return ShotResponse.to_response(shot)


@router.post("/", response_model=ShotResponse, operation_id="create_shot")
async def create_shot(shot: ShotCreate, service: ShotgridService = Depends()):
    shot = service.create_shot(shot)
    return ShotResponse.to_response(shot)


@router.put("/{shot_id}", response_model=ShotResponse, operation_id="update_shot")
async def update_shot(shot_id: int, shot: ShotUpdate, service: ShotgridService = Depends()):
    shot = service.update_shot(shot_id, shot)
    return ShotResponse.to_response(shot)


@router.delete("/{shot_id}", operation_id="delete_shot")
async def delete_shot(shot_id: int, service: ShotgridService = Depends()):
    service.delete_shot(shot_id)
    return {"message": "Shot deleted successfully"}
