# Número perfeito

def eh_perfeito(numero):
    if numero < 2:
        return False
    soma = sum(i for i in range(1, numero) if numero % i == 0)
    return soma == numero


def listar_perfeitos(n):
    print(f"\nNúmeros perfeitos até {n}:")
    perfeitos = [i for i in range(1, n + 1) if eh_perfeito(i)]
    if perfeitos:
        print(perfeitos)
    else:
        print("Nenhum número perfeito encontrado.")


# entrada do usuário
n = int(input("Digite um número inteiro: "))

# chamada da função
listar_perfeitos(n)
