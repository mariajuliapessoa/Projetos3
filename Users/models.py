# Users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

class Users(AbstractUser):
    nomeUsuario = models.CharField(max_length=50, null=False, blank=False)
    CPF = models.CharField(max_length=11, null=False, unique=True)
    cidade = models.CharField(max_length=50, null=False)
    nascimentoData = models.DateField(null=False, blank=False)
    tipo_usuario_choices = [
        ('U', 'Usuário Comum'),
        ('V', 'Voluntário'),
        ('E', 'Embaixador'),
        ('D', 'Dono de Projeto')
    ]
    tipo_usuario = models.CharField(
        max_length=1,
        choices=tipo_usuario_choices,
        default='U',
        help_text='Tipo de Usuário'
    )

    def __str__(self):
        return self.username 
