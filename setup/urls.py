from django.contrib import admin
from django.urls import path, include
from Users.views import home
from Users.views import cadastrar_Users
from Demanda.views import demanda
from Doacao.views import doacao
from Projeto.views import projetos
from Relatorio.views import relatorios
from Users.views import inicial
from Users.views import login

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', inicial),
    path('home', home, name = "home"),
    path('cadastrar_Users/', cadastrar_Users, name="cadastrar_Users"),
    path('projetos/', projetos, name ="projetos"),
    path ('demanda/', demanda, name ="demanda"),
    path ('doacao/', doacao, name ="doacao"),
    path ('relatorios/', relatorios, name ="relatorios"),
    path ('login/', login, name ="login"),

]
