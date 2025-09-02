from datetime import date
from django.test import TestCase
from .services import calcular_signo_solar

class AstrologiaServiceTests(TestCase):
    """
    Testes para os serviços de lógica astrológica, conforme o requisito RF-002.
    """

    def test_calcular_signo_solar(self):
        """
        Testa se a função calcular_signo_solar retorna o signo correto
        para diferentes datas, incluindo as datas de cúspide (início/fim de um signo).
        """
        casos_de_teste = {
            "Áries": [date(2024, 3, 21), date(2024, 4, 19)],
            "Touro": [date(2024, 4, 20), date(2024, 5, 20)],
            "Gêmeos": [date(2024, 5, 21), date(2024, 6, 20)],
            "Câncer": [date(2024, 6, 21), date(2024, 7, 22)],
            "Leão": [date(2024, 7, 23), date(2024, 8, 22)],
            "Virgem": [date(2024, 8, 23), date(2024, 9, 22)],
            "Libra": [date(2024, 9, 23), date(2024, 10, 22)],
            "Escorpião": [date(2024, 10, 23), date(2024, 11, 21)],
            "Sagitário": [date(2024, 11, 22), date(2024, 12, 21)],
            "Capricórnio": [date(2024, 12, 22), date(2024, 1, 19)],
            "Aquário": [date(2024, 1, 20), date(2024, 2, 18)],
            "Peixes": [date(2024, 2, 19), date(2024, 3, 20)],
        }

        for signo_esperado, datas in casos_de_teste.items():
            for data_nascimento in datas:
                with self.subTest(f"Testando data {data_nascimento} para signo {signo_esperado}"):
                    signo_calculado = calcular_signo_solar(data_nascimento)
                    self.assertEqual(signo_calculado, signo_esperado)

