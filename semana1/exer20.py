# Saudação por turno

turno = input("Digite seu turno M = manhã, T = tarde, N = noite: ").upper()

if turno == "M":
    print("Bom dia!")
elif turno == "T":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Letra digitada invalida")

