
# Gerador de E-mails
def gerar_email(nome, sobrenome):
    return f"{nome.lower()}.{sobrenome.lower()}@escola.com"


nome = input("Digite o nome: ")
sobrenome = input("Digite o sobrenome: ")

print(gerar_email(nome, sobrenome))
