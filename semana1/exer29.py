# Peça ao usuário um número inicial, final e o passo.
# Exemplo: início=2, fim=10, passo=2 → saída: 2, 4, 6, 8, 10
# Use um loop for.


numero_inicial = int(input("Informe um numero inicial: "))
numero_final = int(input("Informe um numero final: "))
passo = int(input("Informe o passo: "))

for i in range(numero_inicial, numero_final + 1, passo):
    print(i)
