from django.http import JsonResponse
from .models import Tarefas

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