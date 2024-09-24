# Inicializa uma lista vazia para armazenar as tarefas
tasks = []

def add_task():
    """Adiciona uma nova tarefa à lista."""
    description = input("Digite a descrição da tarefa: ")
    task = {"description": description, "status": "Não Concluída"}
    tasks.append(task)
    print(f"Tarefa '{description}' adicionada com sucesso!")

def list_tasks():
    """Lista todas as tarefas."""
    if not tasks:
        print("Nenhuma tarefa encontrada.")
    else:
        print("Lista de tarefas:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['description']} ({task['status']})")

def mark_task_completed():
    """Marca uma tarefa como concluída."""
    list_tasks()
    try:
        task_index = int(input("Digite o número da tarefa para marcar como concluída: ")) - 1
        tasks[task_index]["status"] = "Concluída"
        print(f"Tarefa '{tasks[task_index]['description']}' marcada como concluída.")
    except (ValueError, IndexError):
        print("Número de tarefa inválido. Por favor, tente novamente.")

def remove_task():
    """Remove uma tarefa da lista."""
    list_tasks()
    try:
        task_index = int(input("Digite o número da tarefa para remover: ")) - 1
        removed_task = tasks.pop(task_index)
        print(f"Tarefa '{removed_task['description']}' removida com sucesso.")
    except (ValueError, IndexError):
        print("Número de tarefa inválido. Por favor, tente novamente.")

def main():
    while True:
        print("\nSistema de Gerenciamento de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("5. Sair")
        choice = input("Digite sua escolha (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Escolha inválida. Por favor, selecione uma opção válida.")

if __name__ == "__main__":
    main()