from django.contrib import admin
from django.urls import path, include
from Projetos3.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path('auth/', include('Users.urls'))
]
