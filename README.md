# Academic Task Manager - Version 2

## Descripción

Esta versión evoluciona la arquitectura inicial e incluye más funcionalidad: permite crear tareas, listar todas, completar tareas y listar pendientes.

## Funcionalidades incluidas

- Crear tarea
- Listar tareas
- Completar tarea
- Listar tareas pendientes

## Qué contiene esta versión

- Dominio: `task.py`, `exceptions.py`
- Puertos: `task_service_port.py`, `task_repository_port.py`
- Adaptadores: `cli_adapter.py`, `memory_repository.py`
- Casos de uso: `create_task.py`, `list_tasks.py`, `complete_task.py`, `list_pending.py`, `delete_task.py`

## Nota de implementación

Esta versión intermedia mantiene la misma arquitectura hexagonal completa y añade las funciones de completar tareas y listar pendientes. La operación de eliminar tareas se define en puertos y casos de uso, pero su ejecución real se reserva para la versión 3.

## Cómo ejecutar

1. Abre una terminal en la carpeta `AcademicTaskManager_v2`.
2. Ejecuta:

```bash
python -m task_manager.main
```

3. Usa el menú para crear tareas, listarlas, completarlas y mostrar pendientes.
