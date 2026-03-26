# Desafio 13 — Simulador de crescimento de capital

capital_inicial = float(input("Capital inicial: R$ "))
aporte = float(input("Aporte mensal: R$ "))
taxa = float(input("Taxa de juros mensal (%): ")) / 100

saldo = capital_inicial
objetivo = capital_inicial * 2
mes = 0

while saldo < objetivo:
    saldo = saldo * (1 + taxa) 
    saldo += aporte           
    mes += 1
    print(f"Mês {mes:>3}: R$ {saldo:.2f}")

anos = mes // 12
meses_restantes = mes % 12
print(f"\nObjetivo atingido em {anos} ano(s) e {meses_restantes} mês(es).")