class NotFoundException(Exception):
    entity: str
    id: int

    def __init__(self, entity: str, entity_id: int):
        self.entity = entity
        self.id = entity_id


class ProjectNotFoundException(NotFoundException):
    def __init__(self, project_id: int):
        super().__init__("Project", project_id)


class AssetNotFoundException(NotFoundException):
    def __init__(self, project_id: int):
        super().__init__("Asset", project_id)


class ShotNotFoundException(NotFoundException):
    def __init__(self, shot_id: int):
        super().__init__("Shot", shot_id)

class TaskNotFoundException(NotFoundException):
    def __init__(self, shot_id: int):
        super().__init__("Task", shot_id)

class UserNotFoundException(NotFoundException):
    def __init__(self, shot_id: int):
        super().__init__("User", shot_id)
