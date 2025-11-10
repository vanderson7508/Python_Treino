# Peça números ao usuário até que ele digite 0.
# Mostre a soma total apenas dos números positivos digitados.
# Use while.

soma = 0
numero = int(input("Informe um numero: "))

while numero != 0:
    if numero > 0:
        soma += numero
    numero = int(input("Informe um numero: "))

print(f"A soma dos numeros positivos informados é {soma}")
