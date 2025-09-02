from django.db import models

class Cliente(models.Model):
    """
    Armazena os dados de nascimento de um cliente para a geração do mapa astral.
    Corresponde ao requisito RF-001.
    """
    nome = models.CharField(max_length=100, help_text="Nome completo do cliente.")
    data_nascimento = models.DateField(help_text="Data de nascimento (DD/MM/AAAA).")
    hora_nascimento = models.TimeField(help_text="Hora de nascimento (HH:MM).")
    local_nascimento = models.CharField(
        max_length=255,
        help_text="Cidade, estado e país de nascimento (ex: São Paulo, SP, Brasil)."
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} - {self.data_nascimento.strftime('%d/%m/%Y')}"
