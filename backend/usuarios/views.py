from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Usuarios
from datetime import date

def listar_usuarios(request):
    usuarios = Usuarios.objects.all().values()
    return JsonResponse(list(usuarios), safe=False)

def buscar_usuario_por_id(request, id):
    usuario = get_object_or_404(Usuarios, id=id)
    
    dados = {
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "status": usuario.status,
        "data_criacao": usuario.data_criacao.strftime('%d/%m/%Y %H:%M')
    }
    
    return JsonResponse(dados, status=200)