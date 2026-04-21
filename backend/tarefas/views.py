from django.http import JsonResponse
from .models import Tarefas
from datetime import date


def listar_tarefas(request):
    tarefas = Tarefas.objects.all().values('id', 'titulo', 'status', 'usuario_responsavel')
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas(request):
    tarefas = Tarefas.objects.all().values()
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas_abertas(request):
    tarefas = Tarefas.objects.filter(status='ABERTA').values()
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas_urgente(request):
    tarefas = Tarefas.objects.filter(status='URGENTE').values()
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas_nao_urgente(request):
    tarefas = Tarefas.objects.filter(status='NAO_URGENTE').values()
    return JsonResponse(list(tarefas), safe=False)

def listar_por_prioridade(request, prioridade):
    tarefas = Tarefas.objects.filter(prioridade=prioridade.upper()).values()
    return JsonResponse(list(tarefas), safe=False)

def listar_abertas_urgentes(request):
    tarefas = Tarefas.objects.filter(status='ABERTA', prioridade='URGENTE').values()
    return JsonResponse(list(tarefas), safe=False)

def listar_atrasadas(request):
    hoje = date.today()
    tarefas = Tarefas.objects.filter(data_entrega__lt=hoje).exclude(status='CONCLUIDA').values()
    return JsonResponse(list(tarefas), safe=False)

def buscar_por_titulo(request, termo):
    tarefas = Tarefas.objects.filter(titulo__icontains=termo).values()
    return JsonResponse(list(tarefas), safe=False)