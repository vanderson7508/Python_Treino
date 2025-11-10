# Peça ao usuário dois números inteiros (limite inferior e superior) e calcule a soma de todos os números pares nesse intervalo.

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
soma = 0

for i in range(n1, n2 + 1):
    if i % 2 == 0:
        soma += i

print(soma)
