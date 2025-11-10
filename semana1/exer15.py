# Verificando sinais
# Peça dois números e diga:

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

if n1 > 0 and n2 > 0:
    print("Ambos sao positivos")
elif n1 < 0 and n2 < 0:
    print("Ambos sao negativos")
else:
    print("Os numeros tem sinais diferentes")


