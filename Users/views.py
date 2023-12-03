from django.http import HttpResponse
from django.shortcuts import render, redirect
from rolepermissions.decorators import has_permission_decorator
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm


@has_permission_decorator('cadastrar_Users')
def cadastrar_Users(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            tipo_usuario = form.cleaned_data['tipo_usuario']

            user = form.save(commit=False)
            user.set_password(password1)
            user.save()

            return redirect('Projetos3:home')  # Use o nome da URL correta aqui

    else:
        form = CustomUserCreationForm()
    
    return render(request, 'html/Users/cadastrar_Users.html', {'form': form})



def home(request):
    context = {}
    return render(request, 'html/padrao/home.html', context)

def inicial(request):
    context = {}
    return render(request, 'html/padrao/home.html', context)

def login (request):
    context={}
    return render(request, 'html/Users/login.html', context)