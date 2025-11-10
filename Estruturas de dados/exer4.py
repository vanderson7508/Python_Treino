def menu():
    print(f"{40*'*'}MENU{40*'*'}")
    print("1 - Frenquencia das palavras.")
    print("2 - Exibe apenas palavras unicas.")
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

def comum():
    ...

def main():
    lista = []
    menu()
    while True:
        texto = 'A vida é muito valiosa por isso merece ser aproveitada cada dia vida vida'
        opcao = input("Digite uma opcao:")
        if opcao == '1':
            frequencia(texto)
        elif opcao == '2':
            unica(texto)
        elif opcao == '6':
            break
        else:
            print("Opcao invalida")

main()
