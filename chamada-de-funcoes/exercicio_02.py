# Reverso de um número inteiro

def reverso_numero(numero):
    """Retorna o reverso de um número inteiro. Ex: 127 -> 721."""
    negativo = numero < 0
    reverso = int(str(abs(numero))[::-1])
    return -reverso if negativo else reverso


print(reverso_numero(12345))
