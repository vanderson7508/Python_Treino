# Entrada em festa


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade < 18:
    print(f"{nome} entrada proibida")
elif idade >= 18 and idade <= 59:
    print(f"{nome} entrada permitida")
else:
    print(f"{nome} entrada gratuita")
