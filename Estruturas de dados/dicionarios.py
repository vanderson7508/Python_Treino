# ============================================
# REVISÃO COMPLETA: DICIONÁRIOS EM PYTHON
# ============================================

"""
Dicionário = Estrutura chave-valor
- Chaves únicas (não podem repetir)
- Valores podem ser qualquer tipo
- Mutável (pode ser modificado)
- Não ordenado (Python 3.7+ mantém ordem de inserção)
"""

from collections import Counter
print("="*70)
print("PARTE 1: CRIANDO DICIONÁRIOS")
print("="*70)

# 1. Forma básica
aluno = {
    'nome': 'João Silva',
    'idade': 20,
    'curso': 'Python'
}
print(f"1. Básico: {aluno}")

# 2. Dicionário vazio
vazio1 = {}
vazio2 = dict()
print(f"2. Vazios: {vazio1}, {vazio2}")

# 3. Usando dict() com pares chave-valor
pessoa = dict(nome='Maria', idade=25, cidade='São Paulo')
print(f"3. Com dict(): {pessoa}")

# 4. Usando zip() - combina duas listas
chaves = ['a', 'b', 'c']
valores = [1, 2, 3]
combinado = dict(zip(chaves, valores))
print(f"4. Com zip(): {combinado}")

# 5. Dictionary comprehension
quadrados = {x: x**2 for x in range(1, 6)}
print(f"5. Comprehension: {quadrados}")

# 6. fromkeys() - cria dict com mesmo valor
padrao = dict.fromkeys(['a', 'b', 'c'], 0)
print(f"6. fromkeys(): {padrao}")

print("\n" + "="*70)
print("PARTE 2: ACESSANDO VALORES")
print("="*70)

produto = {
    'nome': 'Notebook',
    'preco': 2500.00,
    'estoque': 15,
    'categorias': ['Eletrônicos', 'Informática']
}

# 1. Acesso direto (pode dar erro)
print(f"1. Acesso direto: {produto['nome']}")

# 2. Método get() (mais seguro - retorna None se não existir)
email = produto.get('email')
print(f"2. get() sem valor: {email}")

# 3. get() com valor padrão
email = produto.get('email', 'não cadastrado')
print(f"3. get() com padrão: {email}")

# 4. Acessar valores aninhados
print(f"4. Valor aninhado: {produto['categorias'][0]}")

# 5. Verificar se chave existe
if 'preco' in produto:
    print(f"5. Chave existe: R$ {produto['preco']}")

print("\n" + "="*70)
print("PARTE 3: ADICIONANDO E MODIFICANDO")
print("="*70)

config = {'tema': 'escuro', 'idioma': 'pt-BR'}
print(f"Inicial: {config}")

# 1. Adicionar/modificar diretamente
config['fonte'] = 14
config['tema'] = 'claro'  # Modifica existente
print(f"1. Após modificação: {config}")

# 2. update() - adiciona/modifica múltiplos
config.update({'fonte': 16, 'notificacoes': True})
print(f"2. Após update(): {config}")

# 3. setdefault() - adiciona SE NÃO existir
config.setdefault('volume', 50)
config.setdefault('tema', 'rosa')  # Não muda (já existe)
print(f"3. Após setdefault(): {config}")

# 4. Merge de dicionários (Python 3.9+)
padrao = {'cor': 'azul', 'tamanho': 'M'}
usuario = {'cor': 'verde', 'estilo': 'casual'}
completo = padrao | usuario  # usuario sobrescreve
print(f"4. Merge (|): {completo}")

print("\n" + "="*70)
print("PARTE 4: REMOVENDO ITENS")
print("="*70)

dados = {
    'nome': 'Ana',
    'idade': 30,
    'cidade': 'Rio',
    'email': 'ana@email.com',
    'telefone': '123456'
}
print(f"Inicial: {dados}")

# 1. pop() - remove e retorna valor
telefone = dados.pop('telefone')
print(f"1. pop() removeu: {telefone}")
print(f"   Restou: {dados}")

# 2. pop() com valor padrão (não dá erro)
cpf = dados.pop('cpf', 'Não cadastrado')
print(f"2. pop() com padrão: {cpf}")

# 3. popitem() - remove e retorna último item (Python 3.7+)
ultimo = dados.popitem()
print(f"3. popitem(): {ultimo}")
print(f"   Restou: {dados}")

# 4. del - remove chave específica
del dados['cidade']
print(f"4. Após del: {dados}")

# 5. clear() - remove tudo
dados_temp = dados.copy()
dados_temp.clear()
print(f"5. Após clear(): {dados_temp}")

print("\n" + "="*70)
print("PARTE 5: MÉTODOS IMPORTANTES")
print("="*70)

estoque = {
    'notebook': 10,
    'mouse': 50,
    'teclado': 30,
    'monitor': 15
}

# 1. keys() - retorna todas as chaves
print(f"1. keys(): {list(estoque.keys())}")

# 2. values() - retorna todos os valores
print(f"2. values(): {list(estoque.values())}")

# 3. items() - retorna pares (chave, valor)
print(f"3. items(): {list(estoque.items())}")

# 4. len() - quantidade de itens
print(f"4. len(): {len(estoque)} itens")

# 5. copy() - cria cópia superficial
backup = estoque.copy()
print(f"5. copy(): {backup}")

print("\n" + "="*70)
print("PARTE 6: ITERANDO SOBRE DICIONÁRIOS")
print("="*70)

notas = {
    'João': 8.5,
    'Maria': 9.0,
    'Pedro': 7.5,
    'Ana': 9.5
}

# 1. Iterar sobre chaves (padrão)
print("1. Iterando chaves:")
for aluno in notas:
    print(f"   {aluno}")

# 2. Iterar sobre valores
print("\n2. Iterando valores:")
for nota in notas.values():
    print(f"   {nota}")

# 3. Iterar sobre chave e valor
print("\n3. Iterando chave e valor:")
for aluno, nota in notas.items():
    print(f"   {aluno}: {nota}")

# 4. Iterar com enumerate (para índice)
print("\n4. Com enumerate:")
for i, (aluno, nota) in enumerate(notas.items(), 1):
    print(f"   {i}. {aluno}: {nota}")

print("\n" + "="*70)
print("PARTE 7: OPERAÇÕES AVANÇADAS")
print("="*70)

# 1. Inverter chave-valor
original = {'a': 1, 'b': 2, 'c': 3}
invertido = {v: k for k, v in original.items()}
print(f"1. Original: {original}")
print(f"   Invertido: {invertido}")

# 2. Filtrar dicionário
produtos_precos = {
    'Arroz': 10,
    'Feijão': 8,
    'Macarrão': 5,
    'Carne': 30
}
baratos = {k: v for k, v in produtos_precos.items() if v <= 10}
print(f"\n2. Produtos baratos (≤10): {baratos}")

# 3. Modificar valores
dobrado = {k: v*2 for k, v in produtos_precos.items()}
print(f"3. Preços dobrados: {dobrado}")

# 4. Contar ocorrências
texto = "python é incrível python é legal"
palavras = texto.split()
contagem = {}
for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1
print(f"\n4. Contagem de palavras: {contagem}")

# 5. Usando Counter (mais fácil)
contagem_auto = Counter(palavras)
print(f"5. Com Counter: {dict(contagem_auto)}")

# 6. Agrupar dados
alunos = [
    {'nome': 'João', 'turma': 'A'},
    {'nome': 'Maria', 'turma': 'B'},
    {'nome': 'Pedro', 'turma': 'A'},
    {'nome': 'Ana', 'turma': 'B'}
]

por_turma = {}
for aluno in alunos:
    turma = aluno['turma']
    if turma not in por_turma:
        por_turma[turma] = []
    por_turma[turma].append(aluno['nome'])

print(f"\n6. Agrupamento por turma:")
for turma, nomes in por_turma.items():
    print(f"   Turma {turma}: {nomes}")

print("\n" + "="*70)
print("PARTE 8: DICIONÁRIOS ANINHADOS")
print("="*70)

escola = {
    'turma_a': {
        'professor': 'Dr. Silva',
        'alunos': ['João', 'Maria', 'Pedro'],
        'sala': 101
    },
    'turma_b': {
        'professor': 'Dra. Santos',
        'alunos': ['Ana', 'Carlos'],
        'sala': 102
    }
}

print("1. Estrutura completa:")
for turma, dados in escola.items():
    print(f"\n{turma.upper()}:")
    print(f"  Professor: {dados['professor']}")
    print(f"  Sala: {dados['sala']}")
    print(f"  Alunos: {', '.join(dados['alunos'])}")

# Acessar item específico
print(f"\n2. Professor da turma_a: {escola['turma_a']['professor']}")
print(f"3. Primeiro aluno turma_b: {escola['turma_b']['alunos'][0]}")

print("\n" + "="*70)
print("PARTE 9: DICAS E BOAS PRÁTICAS")
print("="*70)

dicas = """
✅ BOAS PRÁTICAS:

1. Use get() ao invés de acesso direto para evitar erros
   ❌ valor = dict[chave]  # Erro se não existir
   ✅ valor = dict.get(chave, padrão)

2. Verifique existência antes de acessar
   ✅ if 'chave' in dict:

3. Use items() para iterar chave e valor
   ✅ for k, v in dict.items():

4. setdefault() para valores padrão
   ✅ dict.setdefault('contador', 0)

5. copy() para cópias (não apenas referência)
   ❌ dict2 = dict1  # Mesma referência!
   ✅ dict2 = dict1.copy()

6. Dict comprehension para transformações
   ✅ {k: v*2 for k, v in dict.items()}

⚠️ CUIDADOS:

• Chaves devem ser IMUTÁVEIS (str, int, tuple)
  ❌ {[1,2]: 'valor'}  # Lista não pode ser chave
  ✅ {(1,2): 'valor'}  # Tupla pode

• Modificar dict durante iteração = ERRO
  ❌ for k in dict:
        del dict[k]  # Erro!

• copy() é superficial (cuidado com nested dicts)
"""
print(dicas)

print("\n" + "="*70)
print("PARTE 10: EXERCÍCIOS PRÁTICOS")
print("="*70)

# Exercício 1: Sistema de Notas
print("\n📝 EXERCÍCIO 1: Sistema de Notas")
print("-" * 70)

turma = {
    'João': [8.5, 9.0, 7.5],
    'Maria': [9.0, 9.5, 8.5],
    'Pedro': [7.0, 7.5, 8.0]
}

print("Médias dos alunos:")
for nome, notas in turma.items():
    media = sum(notas) / len(notas)
    status = "Aprovado" if media >= 7.0 else "Reprovado"
    print(f"  {nome}: {media:.2f} - {status}")

# Exercício 2: Inventário de Loja
print("\n📦 EXERCÍCIO 2: Inventário de Loja")
print("-" * 70)

inventario = {
    'P001': {'nome': 'Notebook', 'preco': 2500, 'qtd': 10},
    'P002': {'nome': 'Mouse', 'preco': 50, 'qtd': 100},
    'P003': {'nome': 'Teclado', 'preco': 150, 'qtd': 50}
}

# Valor total do estoque
total = sum(p['preco'] * p['qtd'] for p in inventario.values())
print(f"Valor total em estoque: R$ {total:,.2f}")

# Produtos mais caros
mais_caro = max(inventario.items(), key=lambda x: x[1]['preco'])
print(
    f"Produto mais caro: {mais_caro[1]['nome']} - R$ {mais_caro[1]['preco']}")

# Exercício 3: Contato Telefônico
print("\n📞 EXERCÍCIO 3: Agenda de Contatos")
print("-" * 70)

agenda = {}


def adicionar_contato(nome, telefone, email=None):
    agenda[nome] = {'telefone': telefone, 'email': email}
    print(f"✓ {nome} adicionado!")


def buscar_contato(nome):
    if nome in agenda:
        info = agenda[nome]
        print(f"\n📇 {nome}")
        print(f"   Telefone: {info['telefone']}")
        print(f"   Email: {info.get('email', 'Não cadastrado')}")
    else:
        print(f"❌ {nome} não encontrado")


adicionar_contato("João", "11-98765-4321", "joao@email.com")
adicionar_contato("Maria", "11-91234-5678")
buscar_contato("João")
buscar_contato("Maria")

print("\n" + "="*70)
print("✅ REVISÃO COMPLETA DE DICIONÁRIOS FINALIZADA!")
print("="*70)
