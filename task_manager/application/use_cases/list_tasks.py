# CAPA: Aplicación | ROL: Caso de uso para listar tareas con su estado
from typing import Dict, List
from task_manager.ports.output.task_repository_port import TaskRepositoryPort


class ListTasksUseCase:
    def __init__(self, repository: TaskRepositoryPort):
        self.repository = repository

    def execute(self) -> Dict[str, List]:
        tasks = self.repository.list_all()
        pending = [task for task in tasks if task.is_pending]
        completed = [task for task in tasks if task.is_completed]
        return {
            "pending": sorted(pending, key=lambda task: task.created_at),
            "completed": sorted(completed, key=lambda task: task.created_at),
        }
