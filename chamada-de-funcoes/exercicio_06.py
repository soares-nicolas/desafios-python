n = int(input("Digite um valor inteiro: "))


def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def exibir_fibonacci(n):
    print(f"\nSequência de Fibonacci até o {n}º termo:")
    for i in range(n + 1):
        print(fibonacci(i), end=" ")
    print()


exibir_fibonacci(n)
