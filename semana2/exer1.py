# Crie uma lista vazia chamada compras.
# Peça ao usuário para digitar produtos até que ele escreva "sair".
# Mostre ao final todos os produtos digitados.

compras = []
condicao = True

while condicao:
    compras.append(input("Digite um item a lista: "))

    condicao = input("Para encerrar digite 'sair': ")
    if condicao == "sair":
        break

print(compras)
