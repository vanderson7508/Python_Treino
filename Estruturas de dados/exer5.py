# Sistema de Estoque

def menu():
    print(f"\n{40*'*'} MENU {40*'*'}")
    print("1 - Adiciona produto")
    print("2 - Atualizar quantidade de estoque")
    print("3 - ")
    print("4 - ")
    print("5 - SAIR")
    print(f"{85*'*'}\n")


def adicionar_produto(lista):
    produto = {
        "nome": input("Digite o nome do produto: "),
        "preco": float(input("Digite o preço do produto: ")),
        "quantidade": int(input("Digite a quantidade: "))
    }
    lista.append(produto)
    print("Produto cadastrado com sucesso!!!")


def atualizar_produto(lista):
    produto_buscado = input("Digite o nome do produto que deseja buscar: ")
    valores = [valor for dicionario in lista for valor in dicionario.values()]
    if produto_buscado in valores:
        qtd_alterar = int(input("Digite a nova quantidade do produto: "))
    else:
        print("O produto digitado nao foi encontrado: ")

    for produto in lista:
        if produto["nome"] == produto_buscado:
            produto["quantidade"] = qtd_alterar
            return lista

def valor_total(lista):
    total = 0
    for dicionario in lista:
        total += dicionario['preco'] * dicionario['quantidade']
    print(f"O valor total em estoque é de {total}")

def main():
    estoque = []
    while True:
        menu()
        opcao = input("Digite uma opção: ").strip()
        if opcao == "1":
            adicionar_produto(estoque)
        elif opcao == "2":
            atualizar_produto(estoque)
        elif opcao == "3":
            print(estoque)
        elif opcao == "4":
            valor_total(estoque)
        elif opcao == "5":
            break

        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()
