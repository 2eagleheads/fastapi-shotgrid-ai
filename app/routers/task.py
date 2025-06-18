from typing import List

from fastapi import APIRouter, Depends

from app.schemas.task import Task, TaskCreate, TaskUpdate
from app.services.shotgrid import ShotgridService

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[Task], operation_id="get_tasks")
async def get_tasks(service: ShotgridService = Depends()):
    return service.get_tasks()


@router.get("/{task_id}", response_model=Task, operation_id="get_task_by_id")
async def get_task(task_id: int, service: ShotgridService = Depends()):
    return service.get_task_by_id(task_id)


@router.post("/", response_model=Task, operation_id="create_task")
async def create_task(task: TaskCreate, service: ShotgridService = Depends()):
    return service.create_task(task)


@router.put("/{task_id}", response_model=Task, operation_id="update_task")
async def update_task(task_id: int, task: TaskUpdate, service: ShotgridService = Depends()):
    return service.update_task(task_id, task)


@router.delete("/{task_id}", operation_id="delete_task")
async def delete_task(task_id: int, service: ShotgridService = Depends()):
    return service.delete_task(task_id)
    return {"message": "Task deleted successfully"}
