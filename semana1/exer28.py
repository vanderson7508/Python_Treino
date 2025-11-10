# Defina usuario = "vanderson" e senha = "1234"
# Peça para o usuário digitar nome e senha.
# Se ambos forem corretos → "Acesso permitido"
# Caso contrário → "Usuário ou senha incorretos"

usuario = "vanderson"
senha = 1234

while True:
    usuario_ = input("Digite seu usuario: ")
    senha_ = int(input("Digite sua senha: "))

    if usuario_ == usuario and senha_ == senha:
        print("Acesso permitido")
        break
    else:
        print("Usuário ou senha incorretos")

