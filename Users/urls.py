from django.urls import path
from .views import cadastrar_Users

urlpatterns = [
	path('cadastrar_Users/', cadastrar_Users, 
    name="cadastrar_Users"),
    	
]

