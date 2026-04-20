data_str = input("Digite a data")


def data_por_extenso(data_str):
    """
    Recebe uma data no formato DD/MM/AAAA e retorna
    'D de Mês de AAAA'. Retorna None se a data for inválida.
    """
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril",
        "Maio", "Junho", "Julho", "Agosto",
        "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    try:
        partes = data_str.strip().split("/")
        if len(partes) != 3:
            return None
        dia, mes, ano = int(partes[0]), int(partes[1]), int(partes[2])
        if not (1 <= mes <= 12):
            return None
        if not (1 <= dia <= 31):
            return None
        # Validação básica de dias por mês
        dias_no_mes = [31, 29 if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)) else 28,
                       31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if dia > dias_no_mes[mes - 1]:
            return None
        return f"{dia} de {meses[mes - 1]} de {ano}"
    except (ValueError, IndexError):
        return None


print(data_por_extenso(data_str))
