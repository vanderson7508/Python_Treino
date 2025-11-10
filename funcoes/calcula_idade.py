# Função para verificar a idade

def verificar_idade(idade):
    if idade < 18:
        return "Menor de idade"
    elif idade >= 18 and idade < 60:
        return "Adulto"
    else:
        return "Idoso"


resultado = verificar_idade(60)
print(resultado)

