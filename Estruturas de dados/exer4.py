def menu():
    print(f"{40*'*'}MENU{40*'*'}")
    print("1 - Frenquencia das palavras.")
    print("2 - Exibe apenas palavras unicas.")
    print("3 - As 5 palavras mais comuns.")
    print("6 - SAIR.")


def frequencia(lista):
    lista = lista.split()
    palavras_verificadas = []
    for i in lista:
        if i in palavras_verificadas:
            continue
        count = 0
        for j in lista:
            if i == j:
                count += 1
        palavras_verificadas.append(i)
        if count != 1:
            print(f'({i}): Aparece no texto: {count} vezes')
        else:
            print(f'({i}): Aparece no texto: {count} vez')


def unica(lista):
    lista = lista.split()
    lista = set(lista)
    return print(lista)


def comum(lista):
    lista = lista.split()
    palavras_verificadas = []
    for i in lista:
        if i in palavras_verificadas:
            continue
        count = 0
        for j in lista:
            if i == j:
                count += 1
        palavras_verificadas.append((i, count))
    print(sorted(palavras_verificadas))


def main():
    lista = []
    menu()
    while True:
        with open('/home/vanderson/python_treino/Estruturas de dados/texto.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        opcao = input("Digite uma opcao:")
        if opcao == '1':
            frequencia(conteudo)
        elif opcao == '2':
            unica(conteudo)
        elif opcao == '3':
            comum(conteudo)
        elif opcao == '6':
            break
        else:
            print("Opcao invalida")


main()
