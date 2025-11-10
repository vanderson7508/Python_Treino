# Peça ao usuário para informar 5 notas e armazene em uma lista.
# Calcule e mostre a média das notas.

notas = []

for i in range(0, 5):
    nota = float(input(f"Digite a {i + 1}° nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f"A media das notas é {media}")
