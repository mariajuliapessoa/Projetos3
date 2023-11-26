
from django.contrib import admin
from django.urls import path
from Projetos3.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]