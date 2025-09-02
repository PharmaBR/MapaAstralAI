from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm
from .models import Cliente
from .services import calcular_signo_solar

def home_view(request):
    """
    Renderiza o formulário de entrada de dados e processa a submissão.
    Corresponde à Tarefa 1.1 do roadmap.
    """
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return redirect('resultado', cliente_id=cliente.id)
    else:
        form = ClienteForm()

    return render(request, 'astrologia/home.html', {'form': form})

def resultado_view(request, cliente_id):
    """
    Exibe o resultado do cálculo do signo.
    Corresponde à Tarefa 1.3 do roadmap.
    """
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    signo = calcular_signo_solar(cliente.data_nascimento)
    context = {'cliente': cliente, 'signo': signo}
    return render(request, 'astrologia/resultado.html', context)