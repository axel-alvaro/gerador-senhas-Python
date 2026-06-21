import random
import string

def gerar_senha(tamanho, usar_numeros=True, usar_simbolos=True):
    caracteres = string.ascii_letters

    if usar_numeros:
        caracteres += string.digits

    if usar_simbolos:
        caracteres += "!@#$%&*?"

    senha = ""

    for _ in range(tamanho):
        senha += random.choice(caracteres)

    return senha


print("=== GERADOR DE SENHAS ===")

tamanho = int(input("Digite o tamanho da senha: "))

senha = gerar_senha(tamanho)

print(f"\nSenha gerada: {senha}")