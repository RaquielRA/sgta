from django.urls import path
from .views import listar_tarefas, buscar_por_titulo, listar_abertas_urgentes, listar_atrasadas, listar_por_prioridade, listar_tarefas, listar_tarefas_abertas, listar_tarefas_urgente, listar_tarefas_nao_urgente

urlpatterns = [
    path ('api/tarefas/', listar_tarefas),
    path('api/tarefas/abertas/', listar_tarefas_abertas, name='tarefas_abertas'),
    path('api/tarefas/urgente/', listar_tarefas_urgente, name='tarefas_urgente'),
    path('api/tarefas/nao_urgente/', listar_tarefas_nao_urgente, name='tarefas_nao_urgente'),
    path('api/tarefas/prioridade/<str:prioridade>/', listar_por_prioridade),
    path('api/tarefas/abertas-urgentes/', listar_abertas_urgentes),
    path('api/tarefas/atrasadas/', listar_atrasadas),
    path('api/tarefas/busca/<str:termo>/', buscar_por_titulo),

]