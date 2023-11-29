from django.db import models
from Projeto.models import Projeto

class Relatorio(models.Model):
    idRelatorio = models.CharField(
        primary_key=True, max_length=50
    )  # Ajuste o tamanho conforme necessário
    idProjetoRelatorio = models.ForeignKey(Projeto, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(max_length=15000, null=False, blank=False)
    dataRelatorio = models.DateTimeField()

    def __str__(self):
        return f"{self.idRelatorio} - {self.titulo}"  # Alterado para retornar uma representação mais informativa


