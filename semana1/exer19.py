# Temperatura ambiente

temperatura = float(input("Digite a temperatura: "))

if temperatura < 20:
    print("Frio ❄️")
elif temperatura >= 20 and temperatura <= 29:
    print("Agradável 🌤️")
else:
    print("Quente ☀️")

