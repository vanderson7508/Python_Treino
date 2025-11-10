# Peça a temperatura e a umidade.
# Mostre:
# - "Calor extremo" se temperatura > 35 e umidade > 70
# - "Clima agradável" se temperatura entre 20 e 30 e umidade entre 40 e 60
# - "Frio" se temperatura < 15 ou umidade < 30


temperatura = float(input("Informe a temperatura: "))
umidade = float(input("Informe a umidade: "))

if temperatura > 35 and umidade > 70:
    print("Calor extremo")
elif temperatura >= 20 and temperatura <= 30 and umidade >= 40 and umidade <= 60:
    print("Clima agradavel")
elif temperatura < 15 or umidade < 30:
    print("Frio")
else:
    print("Informe um valor valido")
