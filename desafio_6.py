# Exercício 6 — Controle de estoque com while

estoque = int(input("Informe a quantidade inicial do insumo: "))

print("\n--- Simulação de consumo ---")
while estoque > 0:
    print(f"Estoque restante: {estoque} unidade(s)")
    estoque -= 1  

print("Estoque zerado. Produção encerrada.")