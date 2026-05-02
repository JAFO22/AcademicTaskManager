# CAPA: Aplicación | ROL: Caso de uso para crear una tarea
from typing import Optional
from task_manager.domain.task import Task
from task_manager.ports.output.task_repository_port import TaskRepositoryPort


class CreateTaskUseCase:
    def __init__(self, repository: TaskRepositoryPort):
        self.repository = repository

    def execute(self, title: str, description: Optional[str] = None) -> Task:
        task = Task(title=title, description=description)
        self.repository.save(task)
        return task
