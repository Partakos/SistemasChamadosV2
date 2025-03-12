from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chamados.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Adiciona as rotas de login/logout
]
