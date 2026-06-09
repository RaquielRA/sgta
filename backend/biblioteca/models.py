from django.db import models
from django.db.models.deletion import SET_NULL



class Biblioteca(models.Model):
    STATUS_CHOICES = [
        ('EMPRESTADO', 'Emprestado'),
        ('NO_CATALOGO', 'No Catalogo')
        ]

    titulo = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NO_CATALOGO')

    usuario_responsavel = models.ForeignKey('usuarios.Usuarios', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Usuário Responsável")
    
    def __str__(self):
        return self.titulo
    