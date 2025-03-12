from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Chamado, Comentario
from .forms import ChamadoForm, ComentarioForm

@login_required
def lista_chamados(request):
    chamados = Chamado.objects.all()
    return render(request, 'chamados/lista_chamados.html', {'chamados': chamados})

@login_required
def detalhes_chamado(request, chamado_id):
    chamado = get_object_or_404(Chamado, id=chamado_id)
    comentarios = chamado.comentarios.all()

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.chamado = chamado
            comentario.usuario = request.user
            comentario.save()
            return redirect('detalhes_chamado', chamado_id=chamado.id)
    else:
        form = ComentarioForm()

    return render(request, 'chamados/detalhes_chamado.html', {
        'chamado': chamado,
        'comentarios': comentarios,
        'form': form
    })

@login_required
def criar_chamado(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)
        if form.is_valid():
            chamado = form.save(commit=False)
            chamado.usuario = request.user
            chamado.save()
            return redirect('lista_chamados')
    else:
        form = ChamadoForm()

    return render(request, 'chamados/criar_chamado.html', {'form': form})
