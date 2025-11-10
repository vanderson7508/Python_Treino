# Peça um número ao usuário e exiba sua tabuada completa, mas:

n1 = int(input("Digite um numero: "))

for i in range(0, 9 + 1):
    if i % 2 != 0:
        if n1 * i < 50:
            print(f"{n1} x {i} = {n1 * i}")

