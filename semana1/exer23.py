# Peça um número inicial e faça uma contagem regressiva até 0, exibindo:

numero = int(input("Digite um numero: "))

while numero > 0:
    if numero > 50:
        print("Digite um numero menor que 50.")
        numero = int(input("Digite um numero: "))
    else:
        numero -= 1
        print(numero)
        if numero == 0:
            print("FIM!")

