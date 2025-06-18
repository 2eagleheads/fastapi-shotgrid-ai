from fastapi import APIRouter, Depends

from app.schemas.upload import UploadThumbnailRequest, UploadResponse, UploadFileRequest
from app.services.shotgrid import ShotgridService

router = APIRouter(
    prefix="/upload",
    tags=["upload"],
    responses={404: {"description": "Not found"}},
)


@router.post("/thumbnail", response_model=UploadResponse, operation_id="upload_thumbnail")
async def upload_thumbnail(upload_request: UploadThumbnailRequest, service: ShotgridService = Depends()):
    return service.upload_thumbnail(upload_request)


@router.post("/file", response_model=UploadResponse, operation_id="upload_file")
async def upload_file(upload_request: UploadFileRequest, service: ShotgridService = Depends()):
    return service.upload_file(upload_request)
