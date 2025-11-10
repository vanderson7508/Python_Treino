# ============================================
# LIÇÃO 1: ESTRUTURAS DE DADOS AVANÇADAS
# ============================================

"""
Nesta lição você vai aprender:
1. Listas (list) - Operações avançadas
2. Dicionários (dict) - Manipulação de dados
3. Sets (set) - Operações de conjuntos
4. Tuplas (tuple) - Dados imutáveis
"""

# ============================================
# 1. LISTAS - Operações Avançadas
# ============================================

print("=" * 50)
print("1. LISTAS - Operações Avançadas")
print("=" * 50)

# List slicing (fatiamento)
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Lista original: {numeros}")
print(f"Primeiros 3: {numeros[:3]}")
print(f"Últimos 3: {numeros[-3:]}")
print(f"Do 2º ao 5º: {numeros[2:6]}")
print(f"Pulando de 2 em 2: {numeros[::2]}")
print(f"Lista invertida: {numeros[::-1]}")

# Métodos úteis de lista
frutas = ['maçã', 'banana', 'laranja']
frutas.append('uva')  # Adiciona no final
frutas.insert(1, 'morango')  # Adiciona em posição específica
print(f"\nFrutas: {frutas}")

# Remove e retorna último item
ultima_fruta = frutas.pop()
print(f"Removeu: {ultima_fruta}, Restou: {frutas}")

# Ordenação
numeros_desordenados = [5, 2, 8, 1, 9]
numeros_desordenados.sort()  # Ordena in-place
print(f"Ordenado: {numeros_desordenados}")

# sorted() retorna nova lista
original = [5, 2, 8, 1, 9]
ordenada = sorted(original)
print(f"Original: {original}, Nova: {ordenada}")

# ============================================
# 2. DICIONÁRIOS - Manipulação de Dados
# ============================================

print("\n" + "=" * 50)
print("2. DICIONÁRIOS - Manipulação de Dados")
print("=" * 50)

# Criando dicionários
aluno = {
    'nome': 'João Silva',
    'idade': 20,
    'curso': 'Python',
    'notas': [8.5, 9.0, 7.5]
}

print(f"Aluno: {aluno['nome']}")
print(f"Média: {sum(aluno['notas']) / len(aluno['notas']):.2f}")

# Métodos úteis de dicionário
print(f"\nChaves: {list(aluno.keys())}")
print(f"Valores: {list(aluno.values())}")
print(f"Itens: {list(aluno.items())}")

# get() - retorna None se não existir (evita erro)
email = aluno.get('email', 'Não cadastrado')
print(f"Email: {email}")

# setdefault() - define valor se não existir
aluno.setdefault('cidade', 'São Paulo')
print(f"Cidade: {aluno['cidade']}")

# update() - atualiza múltiplos valores
aluno.update({'idade': 21, 'semestre': 3})
print(f"Atualizado: {aluno}")

# Dicionário aninhado
escola = {
    'turma_a': {
        'alunos': ['Ana', 'Bruno', 'Carlos'],
        'professor': 'Dr. Silva'
    },
    'turma_b': {
        'alunos': ['Diana', 'Eduardo'],
        'professor': 'Dra. Santos'
    }
}
print(f"\nTurma A - Professor: {escola['turma_a']['professor']}")

# ============================================
# 3. SETS - Operações de Conjuntos
# ============================================

print("\n" + "=" * 50)
print("3. SETS - Operações de Conjuntos")
print("=" * 50)

# Sets não permitem duplicatas
numeros_com_duplicatas = [1, 2, 2, 3, 3, 3, 4, 5]
numeros_unicos = set(numeros_com_duplicatas)
print(f"Com duplicatas: {numeros_com_duplicatas}")
print(f"Set (únicos): {numeros_unicos}")

# Operações de conjuntos
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(f"\nConjunto A: {a}")
print(f"Conjunto B: {b}")
print(f"União (A | B): {a | b}")
print(f"Interseção (A & B): {a & b}")
print(f"Diferença (A - B): {a - b}")
print(f"Diferença Simétrica (A ^ B): {a ^ b}")

# Métodos de set
linguagens = {'Python', 'JavaScript', 'Java'}
linguagens.add('Go')
linguagens.discard('Java')  # Remove se existir (não dá erro)
print(f"\nLinguagens: {linguagens}")

# ============================================
# 4. TUPLAS - Dados Imutáveis
# ============================================

print("\n" + "=" * 50)
print("4. TUPLAS - Dados Imutáveis")
print("=" * 50)

# Tuplas são imutáveis (não podem ser alteradas)
coordenadas = (10, 20)
print(f"Coordenadas: {coordenadas}")

# Desempacotamento de tupla
x, y = coordenadas
print(f"X: {x}, Y: {y}")

# Tupla nomeada (mais legível)
from collections import namedtuple

Pessoa = namedtuple('Pessoa', ['nome', 'idade', 'cidade'])
pessoa1 = Pessoa('Maria', 25, 'Rio de Janeiro')
print(f"\nPessoa: {pessoa1.nome}, {pessoa1.idade} anos, {pessoa1.cidade}")

# Múltiplos retornos de função usando tupla
def calcular_estatisticas(numeros):
    return min(numeros), max(numeros), sum(numeros) / len(numeros)

minimo, maximo, media = calcular_estatisticas([1, 2, 3, 4, 5])
print(f"\nMín: {minimo}, Máx: {maximo}, Média: {media}")

# ============================================
# 5. COMPARAÇÃO E QUANDO USAR
# ============================================

print("\n" + "=" * 50)
print("5. QUANDO USAR CADA ESTRUTURA")
print("=" * 50)

print("""
LISTA (list):
- Use quando precisar de ordem
- Permite duplicatas
- Mutável (pode ser alterada)
- Exemplo: histórico de transações, lista de tarefas

DICIONÁRIO (dict):
- Use para associar chaves a valores
- Acesso rápido por chave
- Exemplo: dados de usuário, configurações

SET (set):
- Use para valores únicos
- Operações matemáticas de conjuntos
- Exemplo: tags, categorias únicas, remover duplicatas

TUPLA (tuple):
- Use para dados que não devem mudar
- Mais rápida que lista
- Exemplo: coordenadas, configurações fixas, retornos de função
""")

# ============================================
# EXERCÍCIO PRÁTICO
# ============================================

print("=" * 50)
print("EXERCÍCIO PRÁTICO")
print("=" * 50)

# Sistema simples de gerenciamento de estudantes
estudantes = []

# Adicionar estudantes
estudantes.append({
    'id': 1,
    'nome': 'Ana Silva',
    'notas': [8.5, 9.0, 7.5],
    'disciplinas': {'Python', 'JavaScript', 'SQL'}
})

estudantes.append({
    'id': 2,
    'nome': 'Bruno Costa',
    'notas': [7.0, 8.5, 9.0],
    'disciplinas': {'Python', 'Java', 'C++'}
})

# Processar dados
for estudante in estudantes:
    media = sum(estudante['notas']) / len(estudante['notas'])
    print(f"\n{estudante['nome']}:")
    print(f"  Média: {media:.2f}")
    print(f"  Disciplinas: {', '.join(estudante['disciplinas'])}")

# Encontrar disciplinas em comum
disc_comum = estudantes[0]['disciplinas'] & estudantes[1]['disciplinas']
print(f"\nDisciplinas em comum: {disc_comum}")

print("\n" + "=" * 50)
print("FIM DA LIÇÃO 1")
print("=" * 50)
