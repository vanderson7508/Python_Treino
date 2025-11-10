# Comparando dois números
# Peça dois números e diga qual é maior, qual é menor ou se são iguais.

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if n1 > n2:
    print(f"{n1} é o maior")
    print(f"{n2} é o menor")
elif n2 > n1:
    print(f"{n2} é o maior")
    print(f"{n1} é o menor")
elif n1 == n2:
    print("os numeros sao iguais")
else:
    print("Numero invalido!!!")

