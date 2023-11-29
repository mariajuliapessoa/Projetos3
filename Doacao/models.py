from django.db import models
from Users.models import Users

class Doacao(models.Model):
    nomeDoador = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    valorDoado = models.FloatField(null=False, blank=False)
    momentoDoacao = models.DateTimeField()
    idDoacao = models.CharField(
        primary_key=True, max_length=50
    )  # Ajuste o tamanho conforme necessário

    def __str__(self):
        return self.idDoacao