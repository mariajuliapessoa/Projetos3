from django.db import models
from enum import Enum
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext as _

class Usuario(models.Model):
    nomeUsuario = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField()
    senha = models.CharField(max_length=30, null=False, blank=False)
    CPF = models.CharField(max_length=11, null=False, unique=True)
    CNPJ = models.CharField(max_length=14, null=False, unique=True)
    cidade = models.CharField(max_length=50, null=False)
    nascimentoData = models.DateField(null=False, blank=False)
    tipoUsuario = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.CPF
        
class TipoDoUsuario(Enum):
    usuarioComum = 1
    voluntario = 2
    embaixador = 3
    donoDeProjeto = 4
    gerente = 5 

class Projeto(models.Model):
    nomeProjeto = models.CharField(max_length=100, null=False, blank=False)
    responsavel = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(max_length=1000, null=False, blank=False)
    contatoTelefone = models.CharField(max_length=14, null=False, blank=False)
    contatoEmail = models.EmailField()
    contatoRedeSociais = models.CharField(max_length=50, null=False, blank=False)
    demanda = models.TextField(max_length=1000, null=False, blank=False)
    idProjeto = models.CharField(primary_key=True, max_length=50)  # Ajuste o tamanho conforme necessário

    def __str__(self):
        return self.nomeProjeto  # Alterado para retornar o nome do projeto ao invés do ID 
    
class Doacao(models.Model):
    nomeDoador = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    valorDoado = models.FloatField(null=False, blank=False)
    momentoDoacao = models.DateTimeField()
    idDoacao = models.CharField(primary_key=True, max_length=50)  # Ajuste o tamanho conforme necessário

    def __str__(self):
        return self.idDoacao
    
class Demanda(models.Model):
    idProjetoDemanda = models.ForeignKey(Projeto, on_delete=models.DO_NOTHING, related_name="demandas")  # Adicione este argumento
    idDemanda = models.CharField(primary_key=True, max_length=50)  # Ajuste o tamanho conforme necessário
    nomeDemanda = models.CharField(max_length=50, null=False, blank=False)
    descricaoDemanda = models.TextField(max_length=200, null=False, blank=False)
    contatoDemanda = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f"{self.idDemanda} - {self.nomeDemanda}"  # Alterado para retornar uma representação mais informativa
    
class Relatorio(models.Model):
    idRelatorio = models.CharField(primary_key=True, max_length=50)  # Ajuste o tamanho conforme necessário
    idProjetoRelatorio = models.ForeignKey(Projeto, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(max_length=15000, null=False, blank=False)
    dataRelatorio = models.DateTimeField()

    def __str__(self):
        return f"{self.idRelatorio} - {self.titulo}"  # Alterado para retornar uma representação mais informativa

User = get_user_model()

class CustomUser(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        "Username",
        max_length=150,
        unique=True,
        help_text=("Required. 150 characters or fewer. Letters, and digits only."),
        # customize the above string as you want
        validators=[username_validator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    email = models.EmailField(max_length=254, blank=False, unique=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=50, blank=False) 
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="customuser_set",  # Adicione este argumento
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="customuser_set",  # Adicione este argumento
        related_query_name="user",
    )
