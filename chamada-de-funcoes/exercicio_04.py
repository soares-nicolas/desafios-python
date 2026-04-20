linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))


def desenha_moldura(linhas=1, colunas=1):
    linhas = max(1, min(20, linhas))
    colunas = max(1, min(20, colunas))

    topo_base = "+" + "-" * colunas + "+"
    meio = "|" + " " * colunas + "|"

    print(topo_base)
    for _ in range(linhas):
        print(meio)
    print(topo_base)


desenha_moldura(linhas, colunas)
