from django.urls import path
from .views import lista_chamados, criar_chamado, detalhes_chamado, atribuir_chamado, excluir_chamado

urlpatterns = [
    path("", lista_chamados, name="lista_chamados"),
    path("chamado/<int:chamado_id>/", detalhes_chamado, name="detalhes_chamado"),
    path("criar/", criar_chamado, name="criar_chamado"),
    path("chamado/<int:chamado_id>/atribuir/", atribuir_chamado, name="atribuir_chamado"),
    path("chamado/<int:chamado_id>/excluir/", excluir_chamado, name="excluir_chamado"),
]
