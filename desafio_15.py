# Desafio 15 — Auditoria de código de barras

numero = int(input("Digite o número: "))
soma = 0

while numero > 0:
    digito = numero % 10
    soma += digito
    numero = numero // 10

print(f"Soma dos dígitos: {soma}")
