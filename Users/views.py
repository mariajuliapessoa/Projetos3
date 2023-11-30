from django.http import HttpResponse
from django.shortcuts import render 
from rolepermissions.decorators import has_permission_decorator
from django.contrib.auth import Users

@has_permission_decorator('cadastrar_Users')

def cadastrar_Users(request):
	User = Users()
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			username = form.cleaned.data['username']
			email = form.cleaned.data['email']
			password1 = form.cleaned.data['password1']
			password2 = form.cleaned.data['password2']
			first_name = form.cleaned.data['first_name']
			last_name = form.cleaned.data['last_name']
			tipo_usuario = form.cleaned.data['tipo_usuario']

			Users = form.save(commit=False)
			Users.set_password(form.cleaned_data['password1'])
			Users.save()

			return redirect('Projetos3/home.html')

	else: 
		form = CustomUserCreationForm()

	return render(request, 'cadastrar_Users.html', {'form': form})

