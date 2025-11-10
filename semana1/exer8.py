# Exercicio 08 da semana 1

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura ** 2)

print(f"Seu imc é {round(imc, 2)}")
