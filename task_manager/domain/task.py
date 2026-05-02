# CAPA: Dominio | ROL: Entidad central con reglas de negocio puras
import enum
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from task_manager.domain.exceptions import InvalidTaskTitle, TaskAlreadyCompleted


class TaskStatus(enum.Enum):
    PENDING = "PENDIENTE"
    COMPLETED = "COMPLETADA"


class Task:
    def __init__(self, title: str, description: Optional[str] = None):
        if not title or not title.strip():
            raise InvalidTaskTitle("El título de la tarea es obligatorio")

        self.id: UUID = uuid4()
        self.title: str = title.strip()
        self.description: Optional[str] = description.strip() if description else None
        self.status: TaskStatus = TaskStatus.PENDING
        self.created_at: datetime = datetime.utcnow()

    def mark_completed(self):
        if self.status == TaskStatus.COMPLETED:
            raise TaskAlreadyCompleted("La tarea ya está completada y no puede completarse de nuevo")
        self.status = TaskStatus.COMPLETED

    @property
    def is_pending(self) -> bool:
        return self.status == TaskStatus.PENDING

    @property
    def is_completed(self) -> bool:
        return self.status == TaskStatus.COMPLETED

    def __str__(self) -> str:
        description = f" - {self.description}" if self.description else ""
        return f"[{self.id}] {self.title}{description} ({self.status.value})"
