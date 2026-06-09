from django.http import JsonResponse
from .models import Biblioteca

def listar_biblioteca(request):
    biblioteca = Biblioteca.objects.all().values()
    return JsonResponse(list(biblioteca), safe=False)

def listar_livros_no_catalogo(request):
    biblioteca = Biblioteca.objects.filter(status='NO_CATALOGO').values()
    return JsonResponse(list(biblioteca), safe=False)
