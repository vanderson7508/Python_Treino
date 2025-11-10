# Peça números ao usuário até ele digitar 0.
numero = 1
cont = 0
maior = -9999
menor = 9999

while numero != 0:
    numero = float(input("Digite um numero: "))
    if numero == 0:
        break
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    cont += 1

print(f"O maior numero digitado é {maior}")
print(f"O menor digitado é {menor}")
print(f"A quantidade total de numeros digitados foi {cont}")


