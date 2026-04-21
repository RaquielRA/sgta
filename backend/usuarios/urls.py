from django.urls import path
from .views import listar_usuarios, buscar_usuario_por_id

urlpatterns = [
    path ('api/usuarios/', listar_usuarios),
    path('usuarios/<int:id>/', buscar_usuario_por_id, name='buscar_usuario'),
]