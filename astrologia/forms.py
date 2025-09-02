from django import forms
from .models import Cliente


TAILWIND_INPUT_CLASSES = (
    "block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset "
    "ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset "
    "focus:ring-indigo-600 sm:text-sm sm:leading-6"
)

class ClienteForm(forms.ModelForm):
    """
    Formulário para a entrada de dados do cliente, baseado no modelo Cliente.
    Corresponde à primeira parte da Tarefa 1.1 do roadmap (RF-001).
    """
    class Meta:
        model = Cliente
        fields = [
            'nome',
            'data_nascimento',
            'hora_nascimento',
            'local_nascimento'
        ]
        labels = {
            'nome': 'Nome Completo',
            'data_nascimento': 'Data de Nascimento',
            'hora_nascimento': 'Horário de Nascimento (formato 24h)',
            'local_nascimento': 'Local de Nascimento',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu nome completo', 'class': TAILWIND_INPUT_CLASSES}),
            'data_nascimento': forms.DateInput(attrs={'type': 'date', 'class': TAILWIND_INPUT_CLASSES}),
            'hora_nascimento': forms.TimeInput(attrs={'type': 'time', 'class': TAILWIND_INPUT_CLASSES}),
            'local_nascimento': forms.TextInput(attrs={'placeholder': 'Ex: São Paulo, Brasil', 'class': TAILWIND_INPUT_CLASSES}),
        }
