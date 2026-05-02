# CAPA: Adaptador de salida | ROL: Persistencia en memoria para pruebas y ejecución simple
from typing import Dict, List
from task_manager.domain.task import Task
from task_manager.ports.output.task_repository_port import TaskRepositoryPort


class InMemoryTaskRepository(TaskRepositoryPort):
    def __init__(self):
        self.tasks: Dict[str, Task] = {}

    def save(self, task: Task) -> None:
        self.tasks[str(task.id)] = task

    def list_all(self) -> List[Task]:
        return list(self.tasks.values())
