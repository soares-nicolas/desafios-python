# Conversão 24h → 12h

def converter_hora(horas, minutos):
    if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
        return None
    periodo = 'A' if horas < 12 else 'P'
    hora_12 = horas % 12
    if hora_12 == 0:
        hora_12 = 12
    return hora_12, minutos, periodo


def exibir_hora_12(horas, minutos):
    resultado = converter_hora(horas, minutos)
    if resultado is None:
        print("Hora inválida!")
        return
    h, m, p = resultado
    periodo_str = "A.M." if p == 'A' else "P.M."
    print(f"{horas:02d}:{minutos:02d} → {h}:{m:02d} {periodo_str}")


def loop_conversao_hora():
    while True:
        print("\n--- Conversão de Horário (24h → 12h) ---")
        entrada = input("Digite a hora no formato HH MM (ou 'sair'): ").strip()

        if entrada.lower() == "sair":
            print("Saindo...")
            break

        try:
            partes = entrada.split()
            horas, minutos = int(partes[0]), int(partes[1])
            exibir_hora_12(horas, minutos)
        except (ValueError, IndexError):
            print("Entrada inválida. Use o formato HH MM (ex: 14 25).")


# CHAMADA DA FUNÇÃO
loop_conversao_hora()
