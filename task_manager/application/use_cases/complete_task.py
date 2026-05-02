# CAPA: Aplicación | ROL: Caso de uso para marcar tareas como completadas
from task_manager.domain.exceptions import TaskNotFound


class CompleteTaskUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, task_id: str):
        # Buscar la tarea, marcar como completada y actualizar el repositorio
        task = self.repository.find_by_id(task_id)
        task.mark_completed()
        self.repository.update(task)
        return task
