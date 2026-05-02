# CAPA: Aplicación | ROL: Caso de uso para eliminar/archivar una tarea
class DeleteTaskUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, task_id: str):
        raise NotImplementedError("La versión 1 no incluye la funcionalidad de eliminar tareas")
