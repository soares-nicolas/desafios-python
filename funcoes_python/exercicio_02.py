# Calculadora de Desconto
def aplicar_desconto(valor, porcentagem):
    desconto = valor * (porcentagem / 100)
    return valor - desconto


print(aplicar_desconto(100, 15))
