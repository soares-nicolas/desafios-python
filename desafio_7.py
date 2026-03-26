# Exercício 7 — Registro e análise de vendas da semana

vendas = []  

for dia in range(1, 8):
    valor = float(input(f"Digite o valor de vendas do dia {dia}: "))
    vendas.append(valor)

total = sum(vendas)
melhor_dia = vendas.index(max(vendas)) + 1  

print(f"\n--- Resumo semanal ---")
print(f"Total acumulado: R$ {total:.2f}")
print(f"Melhor dia de vendas: Dia {melhor_dia} com R$ {max(vendas):.2f}")