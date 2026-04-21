from django.db import models
from django.db.models.deletion import SET_NULL



class Tarefas(models.Model):
    STATUS_CHOICES = [
        ('ABERTA', 'Aberta'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('CONCLUIDA', 'Concluída'),
        ('CANCELADA', 'Cancelada')
        ]
    
    PRIORIDADE_CHOICES = [
        ('URGENTE', 'Urgente'),
        ('NAO_URGENTE', 'Não Urgente'),
    ]
    
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ABERTA')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateField()
    prioridade = models.CharField(max_length=20, choices=PRIORIDADE_CHOICES, default='NAO_URGENTE')
    
    usuario_responsavel = models.ForeignKey('usuarios.Usuarios', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Usuário Responsável")
    
    def __str__(self):
        return self.titulo
    