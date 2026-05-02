# CAPA: Dominio | ROL: Excepciones específicas de reglas de negocio


class DomainException(Exception):
    """Excepción base del dominio."""


class InvalidTaskTitle(DomainException):
    """Se lanza cuando una tarea se crea sin título válido."""


class TaskAlreadyCompleted(DomainException):
    """Se lanza cuando se intenta completar una tarea ya completada."""


class TaskNotFound(DomainException):
    """Se lanza cuando no se encuentra una tarea en el repositorio."""
