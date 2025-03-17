from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Chamado, Comentario
from django.contrib.auth.models import User
from django.utils.timezone import now

@login_required
def lista_chamados(request):
    chamados = Chamado.objects.all()
    return render(request, "chamados/lista_chamados.html", {"chamados": chamados})

@login_required
def detalhes_chamado(request, chamado_id):
    chamado = get_object_or_404(Chamado, id=chamado_id)
    comentarios = chamado.comentarios.all()
    return render(request, "chamados/detalhes_chamado.html", {"chamado": chamado, "comentarios": comentarios})

@login_required
def criar_chamado(request):
    if request.method == "POST":
        titulo = request.POST["titulo"]
        descricao = request.POST["descricao"]
        prioridade = request.POST["prioridade"]

        chamado = Chamado.objects.create(
            titulo=titulo,
            descricao=descricao,
            prioridade=prioridade,
            usuario=request.user
        )

        messages.success(request, "Chamado criado com sucesso!")
        return redirect("lista_chamados")

    return render(request, "chamados/criar_chamado.html")

@login_required
def atribuir_chamado(request, chamado_id):
    chamado = get_object_or_404(Chamado, id=chamado_id)

    if request.user.is_staff:
        chamado.tecnico_responsavel = request.user
        chamado.status = "em_andamento"
        chamado.save()
        messages.success(request, "Chamado atribuído a você com sucesso!")
    else:
        messages.error(request, "Você não tem permissão para atribuir chamados.")

    return redirect("lista_chamados")

@login_required
def excluir_chamado(request, chamado_id):
    chamado = get_object_or_404(Chamado, id=chamado_id)

    if chamado.tecnico_responsavel != request.user:
        messages.error(request, "Você não tem permissão para excluir este chamado.")
        return redirect("lista_chamados")

    if request.method == "POST":
        chamado.delete()
        messages.success(request, "Chamado excluído com sucesso!")
        return redirect("lista_chamados")

    return render(request, "chamados/excluir_chamado.html", {"chamado": chamado})
