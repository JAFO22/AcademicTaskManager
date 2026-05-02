# CAPA: Aplicación | ROL: Caso de uso para eliminar/archivar una tarea
from task_manager.domain.exceptions import TaskNotFound


class DeleteTaskUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, task_id: str):
        # delega al repositorio; propagate TaskNotFound si no existe
        self.repository.delete(task_id)
