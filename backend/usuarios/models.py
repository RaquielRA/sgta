from django.db import models

class Usuarios(models.Model):
    
    STATUS_CHOICES = [
        ('ATIVO', 'Ativo'),
        ('NAO_ATIVO', 'Não Ativo'),
    ]
    
    nome = models.CharField(max_length=255)
    email = models.EmailField (unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ATIVO')
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
