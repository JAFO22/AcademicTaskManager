# CAPA: Puerto de salida | ROL: Contrato que el dominio exige al repositorio
from abc import ABC, abstractmethod
from typing import List
from task_manager.domain.task import Task


class TaskRepositoryPort(ABC):
    @abstractmethod
    def save(self, task: Task) -> None:
        pass

    @abstractmethod
    def list_all(self) -> List[Task]:
        pass

    @abstractmethod
    def find_by_id(self, task_id: str) -> Task:
        pass

    @abstractmethod
    def update(self, task: Task) -> None:
        pass

    @abstractmethod
    def delete(self, task_id: str) -> None:
        pass
