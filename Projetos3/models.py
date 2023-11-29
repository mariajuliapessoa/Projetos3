from django.db import models
from Projeto.models import Projeto




class Demanda(models.Model):
    idProjetoDemanda = models.ForeignKey(
        Projeto, on_delete=models.DO_NOTHING, related_name="demandas"
    )  # Adicione este argumento
    idDemanda = models.CharField(
        primary_key=True, max_length=50
    )  # Ajuste o tamanho conforme necessário
    nomeDemanda = models.CharField(max_length=50, null=False, blank=False)
    descricaoDemanda = models.TextField(max_length=200, null=False, blank=False)
    contatoDemanda = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f"{self.idDemanda} - {self.nomeDemanda}"  # Alterado para retornar uma representação mais informativa


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


