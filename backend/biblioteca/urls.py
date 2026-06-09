from django.urls import path
from .views import listar_biblioteca, listar_livros_no_catalogo

urlpatterns = [
    path ('api/biblioteca/', listar_biblioteca),
    path('api/biblioteca/no_catalogo/', listar_livros_no_catalogo, name='livros_no_catalogo'),
]