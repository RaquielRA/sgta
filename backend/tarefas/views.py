from django.http import JsonResponse
from .models import Tarefas

def listar_tarefas(request):
    tarefas = Tarefas.objects.all().values()
    return JsonResponse(list(tarefas), safe=False)
