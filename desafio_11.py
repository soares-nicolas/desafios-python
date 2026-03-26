# Desafio 11 — Gerador de pirâmide simétrica

altura = int(input("Digite a altura da pirâmide: "))

for linha in range(1, altura + 1):
    espacos = altura - linha         
    caracteres = 2 * linha - 1        
    print(" " * espacos + "#" * caracteres)