# Peça um número e exiba sua tabuada de 1 a 10.
# Depois pergunte se o usuário quer continuar.
# Se ele digitar "não", o programa encerra.

while True:
    numero = int(input("Informe um numero para ver a tabuada: "))
    for i in range(0, 10 + 1):
        print(f"{numero} x {i} = {numero * i}")

    opcao = input("Para encerrar o programa digite 'nao': ").lower()
    if opcao == "nao":
        break
