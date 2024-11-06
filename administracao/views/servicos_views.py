from django.shortcuts import render, redirect
from administracao.forms.servicos_forms import ServicoForm
from ..models import Servico
from django.contrib.auth.decorators import login_required


@login_required
def cadastrar_servico(request):
    if request.method == 'POST':
        form_servico = ServicoForm(request.POST)

        if form_servico.is_valid():
            form_servico.save()
            return redirect('administracao:lista_servicos')

        else:
            form_servico = ServicoForm()

    form_servico = ServicoForm()
    return render(
        request,
        'servicos/form_servico.html',
        {'form_servico': form_servico}
    )

@login_required
def listar_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos/lista_servicos.html', {'servicos': servicos})


@login_required
def editar_servico(request, id):
    servico = Servico.objects.get(id=id)
    form_servico = ServicoForm(request.POST or None, instance=servico)

    if form_servico.is_valid():
        form_servico.save()
        return redirect('administracao:editar_servico')

    return render(request, 'servicos/form_servico.html', {'form_servico': form_servico})