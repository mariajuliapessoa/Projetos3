from django import forms as django_forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'tipo_usuario')

class UserChangeForm(django_forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
