def mostrar_menu():
    print("\nMENU: ")
    print("1 - Adicionar")
    print("2 - Listar")
    print("3 - Remover")

def adicionar_tarefa(tarefas):
    tarefas.append(input("Digite uma tarefa: "))
    return tarefas

def listar_tarefas(tarefas):
    ...

def remover_tarefa(tarefas):
    ...

def main():
    tarefas = []
    while True:
        mostrar_menu()
        opcao = input("Opção: ")
        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "sair":
            print(tarefas)
            break


main()
