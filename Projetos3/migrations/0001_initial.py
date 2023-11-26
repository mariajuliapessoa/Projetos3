# Generated by Django 4.2.7 on 2023-11-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nomeUsuario", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("senha", models.CharField(max_length=30)),
                ("CPF", models.CharField(max_length=11, unique=True)),
                ("CNPJ", models.CharField(max_length=14, unique=True)),
                ("cidade", models.CharField(max_length=50)),
                ("nascimentoData", models.DateField()),
                ("tipoUsuario", models.IntegerField()),
            ],
        ),
    ]
