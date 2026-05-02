# CAPA: Adaptador de salida | ROL: Persistencia en memoria para pruebas y ejecución simple
from typing import Dict, List
from task_manager.domain.task import Task
from task_manager.domain.exceptions import TaskNotFound
from task_manager.ports.output.task_repository_port import TaskRepositoryPort


class InMemoryTaskRepository(TaskRepositoryPort):
    def __init__(self):
        self.tasks: Dict[str, Task] = {}

    def save(self, task: Task) -> None:
        self.tasks[str(task.id)] = task

    def list_all(self) -> List[Task]:
        return list(self.tasks.values())

    def find_by_id(self, task_id: str) -> Task:
        task = self.tasks.get(str(task_id))
        if task is None:
            raise TaskNotFound(f"No se encontró la tarea con id {task_id}")
        return task

    def update(self, task: Task) -> None:
        if str(task.id) not in self.tasks:
            raise TaskNotFound(f"No se encontró la tarea con id {task.id}")
        self.tasks[str(task.id)] = task

    def delete(self, task_id: str) -> None:
        if str(task_id) not in self.tasks:
            raise TaskNotFound(f"No se encontró la tarea con id {task_id}")
        del self.tasks[str(task_id)]
