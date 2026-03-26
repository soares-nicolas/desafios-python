# Desafio 12 — Verificador de chave criptográfica (número primo)

numero = int(input("Digite um número inteiro positivo: "))

primo = True  

if numero < 2:
    primo = False
else:
    for i in range(2, int(numero ** 0.5) + 1): 
        if numero % i == 0:
            primo = False
            break  

if primo:
    print("Chave Válida (Primo)")
else:
    print("Chave Inválida (Composto)")