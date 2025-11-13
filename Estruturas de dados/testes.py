pessoa = [
    {'nome': 'carlos', 'quantidade': 14, 'preco': 2.5},
    {'nome': 'ludmilla','quantidade': 35, 'preco': 10}
]

valores = [valor for dicionario in pessoa for valor in dicionario.values()]

valor = 0
for dicionario in pessoa:
        valor += dicionario['quantidade'] * dicionario['preco']

print(valor)
