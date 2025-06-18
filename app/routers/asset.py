from typing import List

from fastapi import APIRouter, Depends

from app.schemas.asset import Asset, AssetCreate, AssetUpdate
from app.services.shotgrid import ShotgridService

router = APIRouter(
    prefix="/assets",
    tags=["assets"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[Asset], operation_id="get_assets")
async def get_assets(service: ShotgridService = Depends()):
    return service.get_assets()


@router.get("/{asset_id}", response_model=Asset, operation_id="get_asset_by_id")
async def get_asset(asset_id: int, service: ShotgridService = Depends()):
    return service.get_asset_by_id(asset_id)


@router.post("/", response_model=Asset, operation_id="create_asset")
async def create_asset(asset: AssetCreate, service: ShotgridService = Depends()):
    return service.create_asset(asset)


@router.put("/{asset_id}", response_model=Asset, operation_id="update_asset")
async def update_asset(asset_id: int, asset: AssetUpdate, service: ShotgridService = Depends()):
    return service.update_asset(asset_id, asset)


@router.delete("/{asset_id}", operation_id="delete_asset")
async def delete_asset(asset_id: int, service: ShotgridService = Depends()):
    service.delete_asset(asset_id)
    return {"message": "Asset deleted successfully"}
