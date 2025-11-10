# Crie um programa que gerencie uma lista de compras.

def mostrar_menu():
    print("\nMENU: ")
    print("1 - Adicionar")
    print("2 - Listar")
    print("3 - Remover")
    print("4 - Ordenar")
    print("5 - Qtd Itens")
    print("6 - Pesquisar")
    print("7 - Sair")

def adicionar_item(lista):
    lista.append(input("Digite um item para adicionar: "))
    return lista

def listar_itens(lista):
    return print(lista)

def remover_itens(lista):
    try:
        lista.remove(input("Digite o item a ser excluido: "))
        return print(f"Item removido da lista com sucesso"), lista
    except ValueError:
        return print("O item digitado nao esta na lista.")

def ordenar(lista):
    return lista.sort()

def quantidade(lista):
    return len(lista)

def pesquisar(lista):
    try:
        lista.index(input("Digite o item a ser pesquisado: "))
        return print(f"O item existe dentro da lista."), lista
    except ValueError:
        return print("O item digitado nao esta na lista.")

def main():
    lista = []
    while True:
        mostrar_menu()
        opcao = input("Opção: ")
        if opcao == "1":
            adicionar_item(lista)
        elif opcao == "2":
            listar_itens(lista)
        elif opcao == "3":
            remover_itens(lista)
        elif opcao == "4":
            ordenar(lista)
        elif opcao == "5":
            print(f'A quantidade de itens é: {quantidade(lista)}')
        elif opcao == "6":
            pesquisar(lista)
        elif opcao == "7":
            break
        else:
            print("Opção digitada invalida")
main()
