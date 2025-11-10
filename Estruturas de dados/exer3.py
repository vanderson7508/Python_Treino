# Criar dicionario de contatos.

def mostrar_menu():
    print(f"\n{30*'*'}MENU{30*'*'}")
    print("1 - Adicionar")
    print("2 - Buscar")
    print("3 - Listar")
    print("4 - Atualizar")
    print("5 - Remove")
    print("6 - Sair")
    print(f"{64*'*'}")


def adicionar_contato(lista):
    contato = {
        'nome': input("Digite o nome do contato: "),
        'telefone': input("Digite o telefone: : "),
        'email': input("Digite o email: ")
    }
    lista.append(contato)
    return lista


def buscar_contato(lista):
    nome_busca = input("Digite o nome que deseja buscar: ")
    for i, contato in enumerate(lista):
        if lista[i]['nome'] == nome_busca:
            return print(f"{contato['nome']} está salvo nos seus contatos")

    return print("Nome nao encontrado")


def listar_contatos(lista):
    print("Segue contatos salvos em sua agenda:\n")
    for contato in lista:
        print(contato['nome'])


def atualizar(lista):
    nome_editar = input('Digite o nome do contato que deseja modificar: ')
    for i, contato in enumerate(lista):
        if lista[i]['nome'] == nome_editar:
            lista[i]['telefone'] = input('Digite o numero atualizado: ')
            lista[i]['email'] = input('Digite o email atualizado: ')
            return lista

    return print("contato nao encontrado na agenda para modificar")


def remover(dicionario):
    ...


def main():
    lista = []
    while True:
        mostrar_menu()
        opcao = input("Opção: ")
        if opcao == "1":
            adicionar_contato(lista)
            print(lista)
        elif opcao == "2":
            buscar_contato(lista)
        elif opcao == "3":
            listar_contatos(lista)
        elif opcao == "4":
            atualizar(lista)
        elif opcao == "5":
            ...
        elif opcao == "6":
            break
        else:
            print("Opção digitada invalida")
main()
