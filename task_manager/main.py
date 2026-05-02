# CAPA: Composición | ROL: Punto de entrada y ensamblaje de capas hexagonales
from typing import Optional
from task_manager.adapters.input.cli_adapter import CLIAdapter
from task_manager.adapters.output.memory_repository import InMemoryTaskRepository
from task_manager.application.use_cases.create_task import CreateTaskUseCase
from task_manager.application.use_cases.list_tasks import ListTasksUseCase
from task_manager.ports.input.task_service_port import TaskServicePort


class TaskService(TaskServicePort):
    def __init__(self, repository):
        self.create_task_use_case = CreateTaskUseCase(repository)
        self.list_tasks_use_case = ListTasksUseCase(repository)

    def create_task(self, title: str, description: Optional[str] = None):
        return self.create_task_use_case.execute(title=title, description=description)

    def list_tasks(self):
        return self.list_tasks_use_case.execute()

    def complete_task(self, task_id: str):
        raise NotImplementedError("Completar tareas se habilita en versiones posteriores")

    def list_pending_tasks(self):
        raise NotImplementedError("Listado de pendientes se habilita en versiones posteriores")

    def delete_task(self, task_id: str):
        raise NotImplementedError("Eliminar tareas se habilita en versiones posteriores")


def main():
    repository = InMemoryTaskRepository()
    service = TaskService(repository)
    cli = CLIAdapter(service)
    cli.run()


if __name__ == "__main__":
    main()
