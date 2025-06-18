from typing import List

from fastapi import APIRouter, Depends

from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse
from app.services.shotgrid import ShotgridService

router = APIRouter(
    prefix="/projects",
    tags=["projects"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[ProjectResponse], operation_id="get_projects")
async def get_projects(service: ShotgridService = Depends()):
    return service.get_projects()


@router.get("/{project_id}", response_model=ProjectResponse, operation_id="get_project_by_id")
async def get_project(project_id: int, service: ShotgridService = Depends()):
    return service.get_project_by_id(project_id)


@router.post("/", response_model=ProjectResponse, operation_id="create_project")
async def create_project(project: ProjectCreate, service: ShotgridService = Depends()):
    return service.create_project(project)


@router.put("/{project_id}", response_model=ProjectResponse, operation_id="update_project")
async def update_project(project_id: int, project_update_data: ProjectUpdate, service: ShotgridService = Depends()):
    return service.update_project(project_id, project_update_data)


@router.delete("/{project_id}", operation_id="delete_project")
async def delete_project(project_id: int, service: ShotgridService = Depends()):
    service.delete_project(project_id)
    return {"message": "Project deleted successfully"}
