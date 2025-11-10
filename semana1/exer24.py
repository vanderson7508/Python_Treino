# Simule um controle simples de saldo bancário:

saldo = 0

while True:
    opcao = input("Digite uma opcao: depositar(d), sacar(s) ou sair: ")
    if opcao == "d":
        valor = float(input("Digite o valor a depositar: "))
        saldo += valor
    elif opcao == "s":
        valor = float(input("Digite o valor a depositar: "))
        saldo -= valor
    else:
        print(f"Seu saldo em conta é {saldo}")
        break


