from shotgun_api3 import Shotgun

from app.config import settings
from app.exceptions import ShotNotFoundException, ProjectNotFoundException, AssetNotFoundException, \
    TaskNotFoundException, UserNotFoundException
from app.schemas.asset import Asset, AssetCreate, AssetUpdate
from app.schemas.project import Project, ProjectCreate, ProjectUpdate
from app.schemas.shot import Shot, ShotCreate, ShotUpdate
from app.schemas.task import Task, TaskCreate, TaskUpdate
from app.schemas.upload import UploadThumbnailRequest, UploadFileRequest
from app.schemas.user import User, UserCreate, UserUpdate


class ShotgridService:
    def __init__(self):
        self.sg = Shotgun(
            settings.shotgrid_url,
            settings.shotgrid_script_name,
            settings.shotgrid_script_key
        )

    def get_projects(self):
        projects = self.sg.find("Project", [], ["id", "name", "code", "sg_description"])
        return [Project(**project) for project in projects]

    def get_project_by_id(self, project_id: int):
        project = self.sg.find_one("Project", [["id", "is", project_id]], ["id", "name", "code", "sg_description"])
        if not project:
            raise ProjectNotFoundException(project_id)
        return Project(**project)

    def create_project(self, project: ProjectCreate):
        data = project.model_dump(exclude={"id", "type"})
        created_project = self.sg.create("Project", data)
        return Project(**created_project)

    def update_project(self, project_id: int, project_update_data: ProjectUpdate):
        update_data = project_update_data.model_dump(exclude={"id", "type"})
        updated_project = self.sg.update("Project", project_id, update_data)
        if not updated_project:
            raise ProjectNotFoundException(project_id)
        return Project(**updated_project)

    def delete_project(self, project_id: int):
        deleted_project = self.sg.delete("Project", project_id)
        if not deleted_project:
            raise ProjectNotFoundException(project_id)
        return deleted_project

    def get_assets(self):
        assets = self.sg.find("Asset", [], ["id", "name", "code", "description", "project_id"])
        return [Asset(**asset) for asset in assets]

    def get_asset_by_id(self, asset_id: int):
        asset = self.sg.find_one("Asset", [["id", "is", asset_id]], ["id", "name", "code", "description", "project_id"])
        if not asset:
            raise AssetNotFoundException(asset_id)
        return Asset(**asset)

    def create_asset(self, asset: AssetCreate):
        data = asset.model_dump()
        created_asset = self.sg.create("Asset", data)
        return Asset(**created_asset)

    def update_asset(self, asset_id: int, asset: AssetUpdate):
        data = asset.model_dump(exclude_unset=True)
        updated_asset = self.sg.update("Asset", asset_id, data)
        if not updated_asset:
            raise AssetNotFoundException(asset_id)
        return Asset(**updated_asset)

    def delete_asset(self, asset_id: int):
        deleted_asset = self.sg.delete("Asset", asset_id)
        if not deleted_asset:
            raise AssetNotFoundException(asset_id)
        return deleted_asset

    def get_shots(self):
        shots = self.sg.find("Shot", [], ["id", "name", "code", "description", "project_id"])
        return [Shot(**shot) for shot in shots]

    def get_shot_by_id(self, shot_id: int):
        shot = self.sg.find_one("Shot", [["id", "is", shot_id]], ["id", "name", "code", "description", "project_id"])
        if not shot:
            raise ShotNotFoundException(shot_id)
        return Shot(**shot)

    def create_shot(self, shot: ShotCreate):
        data = shot.model_dump(exclude={"id"})
        created_shot = self.sg.create("Shot", data)
        return Shot(**created_shot)

    def update_shot(self, shot_id: int, shot: ShotUpdate):
        data = shot.model_dump(exclude_unset=True)
        updated_shot = self.sg.update("Shot", shot_id, data)
        if not updated_shot:
            raise ShotNotFoundException(shot_id)
        return Shot(**updated_shot)

    def delete_shot(self, shot_id: int):
        deleted_shot = self.sg.delete("Shot", shot_id)
        if not deleted_shot:
            raise ShotNotFoundException(shot_id)
        return deleted_shot

    def get_tasks(self):
        tasks = self.sg.find("Task", [], ["id", "name", "sg_description", "status", "asset_id", "shot_id"])
        return [Task(**task) for task in tasks]

    def get_task_by_id(self, task_id: int):
        task = self.sg.find_one("Task", [["id", "is", task_id]],
                                ["id", "name", "sg_description", "status", "asset_id", "shot_id"])
        if not task:
            raise TaskNotFoundException(task_id)
        return Task(**task)

    def create_task(self, task: TaskCreate):
        data = task.model_dump()
        created_task = self.sg.create("Task", data)
        return Task(**created_task)

    def update_task(self, task_id: int, task: TaskUpdate):
        data = task.model_dump(exclude_unset=True)
        updated_task = self.sg.update("Task", task_id, data)
        if not updated_task:
            raise TaskNotFoundException(task_id)
        return Task(**updated_task)

    def delete_task(self, task_id: int):
        deleted_task = self.sg.delete("Task", task_id)
        if not deleted_task:
            raise TaskNotFoundException(task_id)
        return deleted_task

    def get_users(self):
        users = self.sg.find("HumanUser", [], ["id", "name", "email", "role"])
        return [User(**user) for user in users]

    def get_user_by_id(self, user_id: int):
        user = self.sg.find_one("HumanUser", [["id", "is", user_id]], ["id", "name", "email", "role"])
        if not user:
            raise UserNotFoundException(user_id)
        return User(**user)

    def create_user(self, user: UserCreate):
        data = user.model_dump()
        created_user = self.sg.create("HumanUser", data)
        return User(**created_user)

    def update_user(self, user_id: int, user: UserUpdate):
        data = user.model_dump(exclude_unset=True)
        updated_user = self.sg.update("HumanUser", user_id, data)
        if not updated_user:
            raise UserNotFoundException(user_id)
        return User(**updated_user)

    def delete_user(self, user_id: int):
        deleted_user = self.sg.delete("HumanUser", user_id)
        if not deleted_user:
            raise UserNotFoundException(user_id)
        return deleted_user

    def upload_thumbnail(self, upload_data: UploadThumbnailRequest):
        result = self.sg.upload_thumbnail(upload_data.entity_type.capitalize(), upload_data.entity_id,
                                          upload_data.file_path)
        return dict(result=f"Successfully uploaded thumbnail for {upload_data.entity_type} {upload_data.entity_id}.")

    def upload_file(self, upload_data: UploadFileRequest):
        return self.sg.upload(upload_data.entity_type.capitalize(), upload_data.entity_id, upload_data.file_path,
                              upload_data.field_name)
