def celsius_para_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def menu_temperatura():
    while True:
        print("\n--- Conversão de Temperatura ---")
        print("1 - Celsius → Fahrenheit")
        print("2 - Fahrenheit → Celsius")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            valor = float(input("Digite a temperatura em Celsius: "))
            resultado = celsius_para_fahrenheit(valor)
            print(f"{valor}°C = {resultado:.2f}°F")
        elif opcao == "2":
            valor = float(input("Digite a temperatura em Fahrenheit: "))
            resultado = fahrenheit_para_celsius(valor)
            print(f"{valor}°F = {resultado:.2f}°C")
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu_temperatura()
