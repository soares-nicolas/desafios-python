# Desafio 14 — Fibonacci 

n = int(input("Quantos números da sequência deseja ver? "))

anterior = 0
atual = 1

for i in range(n):
    print(atual, end="")
    if i < n - 1:
        print(", ", end="")
    anterior, atual = atual, anterior + atual  #

print()  