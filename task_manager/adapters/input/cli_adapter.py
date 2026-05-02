# CAPA: Adaptador de entrada | ROL: Interfaz de consola que usa el puerto de entrada
from task_manager.domain.exceptions import DomainException
from task_manager.ports.input.task_service_port import TaskServicePort


class CLIAdapter:
    def __init__(self, service: TaskServicePort):
        self.service = service

    def run(self):
        while True:
            self._print_menu()
            option = input("Seleccione una opción: ").strip()

            if option == "1":
                self._create_task()
            elif option == "2":
                self._list_tasks()
            elif option == "3":
                print("Saliendo. Gracias por usar el gestor de tareas.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def _print_menu(self):
        print("\n=== GESTOR DE TAREAS ACADÉMICAS - V1 ===")
        print("1. Crear tarea")
        print("2. Listar tareas")
        print("3. Salir")

    def _create_task(self):
        title = input("Título: ").strip()
        description = input("Descripción (opcional): ").strip()
        description = description or None
        try:
            task = self.service.create_task(title=title, description=description)
            print(f"Tarea creada: {task}")
        except DomainException as error:
            print(f"Error: {error}")

    def _list_tasks(self):
        tasks = self.service.list_tasks()
        self._print_task_group("Pendientes", tasks["pending"])
        self._print_task_group("Completadas", tasks["completed"])

    def _print_task_group(self, title: str, tasks: list):
        print(f"\n--- {title} ---")
        if not tasks:
            print("(ninguna tarea)")
            return
        for task in tasks:
            description = f" - {task.description}" if task.description else ""
            print(f"- {task.id} | {task.title}{description} | {task.status.value}")
