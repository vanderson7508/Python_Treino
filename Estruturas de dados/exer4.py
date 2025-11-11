def menu():
    print(f"{40*'*'}MENU{40*'*'}")
    print("1 - Frenquencia das palavras.")
    print("2 - Exibe apenas palavras unicas.")
    print("3 - As 5 palavras mais comuns.")
    print("4 - Que estão presentes nos dois textos.")
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
    unicas = []
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
        if count == 1:
            unicas.append(i)
            print(unicas)


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
    unicas = set(palavras_verificadas)
    ordenado = sorted(unicas, key=lambda x:x[1], reverse=True)
    print(ordenado[:5])

def compara(lista1, lista2):
    lista1 = lista1.split()
    lista2 = lista2.split()

    comum = set(lista1) & set(lista2)
    return print(comum)


def main():
    lista = []
    menu()
    while True:
        with open('texto.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        with open('texto2.txt', 'r', encoding='utf-8') as arquivo:
            conteudo2 = arquivo.read()
        opcao = input("Digite uma opcao:")
        if opcao == '1':
            frequencia(conteudo)
        elif opcao == '2':
            unica(conteudo)
        elif opcao == '3':
            comum(conteudo)
        elif opcao == '4':
            compara(conteudo, conteudo2)
        elif opcao == '6':
            break
        else:
            print("Opcao invalida")

main()
