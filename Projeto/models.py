from django.db import models

class Projeto(models.Model):
    nomeProjeto = models.CharField(max_length=100, null=False, blank=False)
    responsavel = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(max_length=1000, null=False, blank=False)
    contatoTelefone = models.CharField(max_length=14, null=False, blank=False)
    contatoEmail = models.EmailField()
    contatoRedeSociais = models.CharField(max_length=50, null=False, blank=False)
    demanda = models.TextField(max_length=1000, null=False, blank=False)
    idProjeto = models.CharField(
        primary_key=True, max_length=50
    )  

    def __str__(self):
        return (
            self.nomeProjeto
        )  # Alterado para retornar o nome do projeto ao invés do ID