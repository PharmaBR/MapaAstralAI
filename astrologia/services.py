from datetime import date

SIGNOS_DETALHES = {
    "Áries": {
        "elemento": "Fogo",
        "descricao": "Aventureiros, cheios de energia, pioneiros e corajosos. São rápidos e dinâmicos, e muitas vezes agem antes de pensar."
    },
    "Touro": {
        "elemento": "Terra",
        "descricao": "Práticos, determinados, e apreciam a segurança e o conforto. São conhecidos pela sua teimosia, mas também pela sua lealdade."
    },
    "Gêmeos": {
        "elemento": "Ar",
        "descricao": "Comunicativos, curiosos, e versáteis. Adaptam-se facilmente a novas situações e adoram aprender e trocar ideias."
    },
    "Câncer": {
        "elemento": "Água",
        "descricao": "Emocionais, protetores e muito ligados à família. São sensíveis e intuitivos, mas podem ser um pouco temperamentais."
    },
    "Leão": {
        "elemento": "Fogo",
        "descricao": "Criativos, generosos e autoconfiantes. Gostam de ser o centro das atenções e têm um coração nobre e leal."
    },
    "Virgem": {
        "elemento": "Terra",
        "descricao": "Metódicos, analíticos e trabalhadores. Prestam muita atenção aos detalhes e buscam a perfeição em tudo o que fazem."
    },
    "Libra": {
        "elemento": "Ar",
        "descricao": "Diplomáticos, charmosos e idealistas. Buscam o equilíbrio e a harmonia em todos os relacionamentos e situações."
    },
    "Escorpião": {
        "elemento": "Água",
        "descricao": "Intensos, passionais e determinados. São misteriosos e têm uma grande força emocional e poder de transformação."
    },
    "Sagitário": {
        "elemento": "Fogo",
        "descricao": "Otimistas, amantes da liberdade e aventureiros. Adoram viajar, explorar e buscar novos conhecimentos e filosofias."
    },
    "Capricórnio": {
        "elemento": "Terra",
        "descricao": "Responsáveis, disciplinados e ambiciosos. São práticos e têm uma grande capacidade de planejamento e trabalho duro."
    },
    "Aquário": {
        "elemento": "Ar",
        "descricao": "Originais, independentes e humanitários. Gostam de inovar e lutar por causas sociais, valorizando a amizade e a liberdade."
    },
    "Peixes": {
        "elemento": "Água",
        "descricao": "Sensíveis, sonhadores e compassivos. Têm uma forte intuição e uma grande capacidade de empatia e conexão com os outros."
    },
}

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

def obter_dados_signo(signo_nome: str) -> dict:
    """
    Retorna os detalhes de um signo (elemento, descrição).
    """
    dados = SIGNOS_DETALHES.get(signo_nome, {}).copy()
    dados['nome'] = signo_nome
    return dados
