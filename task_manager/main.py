# CAPA: Composición | ROL: Punto de entrada y ensamblaje de capas hexagonales
from typing import Optional
from task_manager.adapters.input.cli_adapter import CLIAdapter
from task_manager.adapters.output.memory_repository import InMemoryTaskRepository
from task_manager.application.use_cases.create_task import CreateTaskUseCase
from task_manager.application.use_cases.list_tasks import ListTasksUseCase
from task_manager.application.use_cases.complete_task import CompleteTaskUseCase
from task_manager.application.use_cases.list_pending import ListPendingUseCase
from task_manager.application.use_cases.delete_task import DeleteTaskUseCase
from task_manager.ports.input.task_service_port import TaskServicePort


class TaskService(TaskServicePort):
    def __init__(self, repository):
        self.create_task_use_case = CreateTaskUseCase(repository)
        self.list_tasks_use_case = ListTasksUseCase(repository)
        self.complete_task_use_case = CompleteTaskUseCase(repository)
        self.list_pending_use_case = ListPendingUseCase(repository)
        self.delete_task_use_case = DeleteTaskUseCase(repository)

    def create_task(self, title: str, description: Optional[str] = None):
        return self.create_task_use_case.execute(title=title, description=description)

    def list_tasks(self):
        return self.list_tasks_use_case.execute()

    def complete_task(self, task_id: str):
        return self.complete_task_use_case.execute(task_id)

    def list_pending_tasks(self):
        return self.list_pending_use_case.execute()

    def delete_task(self, task_id: str):
        return self.delete_task_use_case.execute(task_id)


def main():
    repository = InMemoryTaskRepository()
    service = TaskService(repository)
    cli = CLIAdapter(service)
    cli.run()


if __name__ == "__main__":
    main()
