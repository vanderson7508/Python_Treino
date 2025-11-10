# Verificador de empréstimo

nome = input("Informe seu nome: ")
idade = int(input("Sua idade: "))
renda_mensal = float(input("Qual sua renda mensal: "))
valor = float(input("Digite o valor desejado de emprestimo: "))

if idade >= 21 and renda_mensal > 2500:
    if valor < (renda_mensal * 10):
        print("emprestimo Autorizado")
    else:
        print("Valor inferior ao limite")
else:
    print("Voce nao possui os requesitos para o emprestimo")
