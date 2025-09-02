from datetime import date

def calcular_signo_solar(data_nascimento: date) -> str:
    """
    Calcula o signo solar com base na data de nascimento.

    A lógica foi refatorada para ser independente do ano e para lidar
    corretamente com signos que cruzam a fronteira do ano (Capricórnio).
    """
    # Lista com as datas de *início* de cada signo.
    # O formato é (mês, dia, nome_do_signo).
    signos_inicio = [
        (1, 20, "Aquário"),
        (2, 19, "Peixes"),
        (3, 21, "Áries"),
        (4, 20, "Touro"),
        (5, 21, "Gêmeos"),
        (6, 21, "Câncer"),
        (7, 23, "Leão"),
        (8, 23, "Virgem"),
        (9, 23, "Libra"),
        (10, 23, "Escorpião"),
        (11, 22, "Sagitário"),
        (12, 22, "Capricórnio"),
    ]

    # O signo padrão é Capricórnio, pois é o último do ciclo astrológico.
    signo_calculado = "Capricórnio"
    for mes_limite, dia_limite, signo in signos_inicio:
        if data_nascimento.month < mes_limite or \
           (data_nascimento.month == mes_limite and data_nascimento.day < dia_limite):
            # Se a data de nascimento for anterior ao início do signo atual no loop,
            # significa que pertence ao signo anterior. O loop é interrompido.
            break
        # Caso contrário, a data pertence a este signo, então o atualizamos.
        signo_calculado = signo

    return signo_calculado

