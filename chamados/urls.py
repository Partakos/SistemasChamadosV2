from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_chamados, name='lista_chamados'),
    path('chamado/<int:chamado_id>/', views.detalhes_chamado, name='detalhes_chamado'),
    path('criar/', views.criar_chamado, name='criar_chamado'),
]
