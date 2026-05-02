# Academic Task Manager

## Descripción del problema

Este proyecto resuelve la gestión básica de tareas académicas desde consola. Permite crear tareas, guardarlas en memoria y consultar su estado en una interfaz simple de terminal.

La idea es separar claramente la lógica del negocio de los detalles de entrada y salida, para que la aplicación sea fácil de entender, extender y probar.

## Estructura del proyecto

```text
task_manager/
	main.py
	adapters/
		input/
			cli_adapter.py
		output/
			memory_repository.py
	application/
		use_cases/
			complete_task.py
			create_task.py
			delete_task.py
			list_pending.py
			list_tasks.py
	domain/
		exceptions.py
		task.py
	ports/
		input/
			task_service_port.py
		output/
			task_repository_port.py
```

## Pasos para ejecutar

1. Abre una terminal en la raíz del proyecto, `AcademicTaskManager`.
2. Ejecuta la aplicación con:

```bash
python -m task_manager.main
```

3. En el menú de consola, elige una opción:

- `1` para crear una tarea.
- `2` para listar las tareas guardadas (pendientes y completadas).
- `4` para listar solo las tareas pendientes.
- `5` para completar una tarea (se solicita el `ID`).
- `6` para eliminar una tarea (se solicita el `ID`).
- `3` para salir.

## Tecnologías usadas

- Python 3.13
- Programación orientada a objetos
- Arquitectura hexagonal
- Aplicación de consola
- Persistencia en memoria

## Casos de uso implementados

- `CreateTaskUseCase`: crea una tarea nueva y la guarda en el repositorio.
- `ListTasksUseCase`: obtiene las tareas guardadas y las separa en pendientes y completadas.
- `CompleteTaskUseCase`: marca una tarea como completada y actualiza el repositorio.
- `ListPendingUseCase`: lista las tareas pendientes ordenadas por creación.
- `DeleteTaskUseCase`: elimina una tarea del repositorio por `ID`.

## Casos de uso pendientes

- Ninguno: todos los casos de uso listados arriba están implementados en esta versión.

## Puertos y adaptadores

El proyecto usa la arquitectura de puertos y adaptadores para desacoplar la lógica central de la forma en que la aplicación interactúa con el exterior.

- Los puertos definen contratos. Por ejemplo, `TaskServicePort` describe lo que la interfaz de entrada debe ofrecer y `TaskRepositoryPort` define cómo debe comportarse el repositorio.
- Los adaptadores implementan esos contratos. `CLIAdapter` traduce la interacción por consola hacia la capa de aplicación, y `InMemoryTaskRepository` cumple el contrato de almacenamiento usando un diccionario en memoria.

Esta separación permite cambiar la interfaz o el mecanismo de persistencia sin tocar el núcleo del dominio.
