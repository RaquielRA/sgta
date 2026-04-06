from django.urls import path
from .views import listar_tarefas, listar_tarefas_abertas, listar_tarefas_urgente, listar_tarefas_nao_urgente

urlpatterns = [
    path ('tarefas/', listar_tarefas),
    path('tarefas/abertas/', listar_tarefas_abertas, name='tarefas_abertas'),
    path('tarefas/urgente/', listar_tarefas_urgente, name='tarefas_urgente'),
    path('tarefas/nao_urgente/', listar_tarefas_nao_urgente, name='tarefas_nao_urgente'),

]