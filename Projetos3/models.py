from django.db import models

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
        