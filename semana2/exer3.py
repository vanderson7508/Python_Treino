# Peça 10 números ao usuário e guarde em uma lista.
# Mostre apenas os números pares.

numeros = []
pares = []

for i in range(0, 10):
    numero = float(input(f"Digite o {i + 1}° numero: "))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(f"Os numeros pares da lista são: {pares}")
