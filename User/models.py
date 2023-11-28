from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth import get_user_model

class Usuario(models.Model):
    nomeUsuario = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField()
    senha = models.CharField(max_length=30, null=False, blank=False)
    CPF = models.CharField(max_length=11, null=False, unique=True)
    cidade = models.CharField(max_length=50, null=False)
    nascimentoData = models.DateField(null=False, blank=False)
    tipoUsuario = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.CPF


class Users(AbstractUser):

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

Users = get_user_model()


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
            "unique": ("A user with that username already exists."),
        },
    )
    email = models.EmailField(max_length=254, blank=False, unique=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="customuser_set",  # Adicione este argumento
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("user permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="customuser_set",  # Adicione este argumento
        related_query_name="user",
    )
