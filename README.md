# Academic Task Manager - Version 1

## Descripción

Esta es la versión inicial del gestor de tareas académicas. Contiene la estructura básica con arquitectura hexagonal y permite crear y listar tareas.

## Funcionalidades incluidas

- Crear tarea
- Listar tareas

## Qué contiene esta versión

- Dominio: `task.py`, `exceptions.py`
- Puertos: `task_service_port.py`, `task_repository_port.py`
- Adaptadores: `cli_adapter.py`, `memory_repository.py`
- Casos de uso: `create_task.py`, `list_tasks.py`, `complete_task.py`, `list_pending.py`, `delete_task.py`

## Nota de implementación

Esta versión inicial mantiene la arquitectura hexagonal completa y el contrato de puertos con todas las operaciones previstas. Las funciones de completar, listar pendientes y eliminar están definidas en los puertos y los casos de uso, pero su ejecución real se habilita en versiones posteriores.

## Cómo ejecutar

1. Abre una terminal en la carpeta `AcademicTaskManager_v1`.
2. Ejecuta:

```bash
python -m task_manager.main
```

3. Elige una opción del menú para crear o listar tareas.
