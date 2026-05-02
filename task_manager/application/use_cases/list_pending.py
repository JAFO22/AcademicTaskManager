# CAPA: Aplicación | ROL: Caso de uso para consultar tareas pendientes
class ListPendingUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self) -> list:
        raise NotImplementedError("La versión 1 no incluye la funcionalidad de listar pendientes")
