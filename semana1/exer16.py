# Classificação de notas

nota = float(input("Informe sua nota: "))

if nota >= 7:
    print("Aprovado")
elif nota >= 5 and nota < 7:
    print("Recuperação")
else:
    print("Reprovado")
