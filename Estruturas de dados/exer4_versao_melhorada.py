from collections import Counter


def menu():
    print(f"\n{40*'*'} MENU {40*'*'}")
    print("1 - Frequência das palavras")
    print("2 - Exibir apenas palavras únicas")
    print("3 - As 5 palavras mais comuns")
    print("4 - Palavras presentes nos dois textos")
    print("5 - SAIR")
    print(f"{85*'*'}\n")


def frequencia(texto):
    """Exibe a frequência de cada palavra no texto"""
    palavras = texto.lower().split()
    contador = Counter(palavras)
    
    print("\n--- FREQUÊNCIA DAS PALAVRAS ---")
    for palavra, freq in sorted(contador.items()):
        vez_vezes = "vez" if freq == 1 else "vezes"
        print(f"'{palavra}': Aparece no texto {freq} {vez_vezes}")


def unica(texto):
    """Exibe apenas palavras que aparecem uma única vez"""
    palavras = texto.lower().split()
    contador = Counter(palavras)
    
    unicas = [palavra for palavra, freq in contador.items() if freq == 1]
    
    print("\n--- PALAVRAS ÚNICAS ---")
    if unicas:
        print(f"Palavras que aparecem apenas 1 vez: {sorted(unicas)}")
    else:
        print("Não há palavras únicas no texto.")


def comum(texto):
    """Exibe as 5 palavras mais comuns"""
    palavras = texto.lower().split()
    contador = Counter(palavras)
    
    mais_comuns = contador.most_common(5)
    
    print("\n--- 5 PALAVRAS MAIS COMUNS ---")
    for posicao, (palavra, freq) in enumerate(mais_comuns, 1):
        print(f"{posicao}º - '{palavra}': {freq} ocorrências")


def compara(texto1, texto2):
    """Exibe palavras presentes em ambos os textos"""
    palavras1 = set(texto1.lower().split())
    palavras2 = set(texto2.lower().split())
    
    palavras_comuns = palavras1 & palavras2
    
    print("\n--- PALAVRAS EM AMBOS OS TEXTOS ---")
    if palavras_comuns:
        print(f"Palavras em comum: {sorted(palavras_comuns)}")
        print(f"Total: {len(palavras_comuns)} palavras")
    else:
        print("Não há palavras em comum entre os textos.")


def main():
    # Lê os arquivos UMA VEZ antes do loop
    try:
        with open('texto.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        with open('texto2.txt', 'r', encoding='utf-8') as arquivo:
            conteudo2 = arquivo.read()
    except FileNotFoundError as e:
        print(f"Erro: Arquivo não encontrado - {e}")
        return
    
    while True:
        menu()
        opcao = input("Digite uma opção: ").strip()
        
        if opcao == '1':
            frequencia(conteudo)
        elif opcao == '2':
            unica(conteudo)
        elif opcao == '3':
            comum(conteudo)
        elif opcao == '4':
            compara(conteudo, conteudo2)
        elif opcao == '5':
            print("\nEncerrando programa...")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")
        
        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()
