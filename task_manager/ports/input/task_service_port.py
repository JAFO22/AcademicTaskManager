# CAPA: Puerto de entrada | ROL: Contrato que expone las acciones de la aplicación hacia el adaptador
from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from task_manager.domain.task import Task


class TaskServicePort(ABC):
    @abstractmethod
    def create_task(self, title: str, description: Optional[str] = None) -> Task:
        pass

    @abstractmethod
    def list_tasks(self) -> Dict[str, List[Task]]:
        pass

    @abstractmethod
    def complete_task(self, task_id: str) -> Task:
        pass

    @abstractmethod
    def list_pending_tasks(self) -> list:
        pass

    @abstractmethod
    def delete_task(self, task_id: str) -> None:
        pass
