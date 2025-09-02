from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    """
    Configuração da exibição do modelo Cliente no painel de administração do Django.
    """
    list_display = ('nome', 'data_nascimento', 'local_nascimento', 'criado_em')
    search_fields = ('nome', 'local_nascimento')
    list_filter = ('data_nascimento',)
