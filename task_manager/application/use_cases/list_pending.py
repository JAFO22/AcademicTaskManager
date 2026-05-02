# CAPA: Aplicación | ROL: Caso de uso para consultar tareas pendientes
from typing import List
from task_manager.ports.output.task_repository_port import TaskRepositoryPort


class ListPendingUseCase:
    def __init__(self, repository: TaskRepositoryPort):
        self.repository = repository

    def execute(self) -> List:
        tasks = self.repository.list_all()
        pending = [task for task in tasks if task.is_pending]
        return sorted(pending, key=lambda task: task.created_at)
