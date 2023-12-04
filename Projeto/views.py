from django.shortcuts import render
from .models import Projeto

def projetos(request):
    projetos = Projeto.objects.all()
    context = {'projetos': projetos}
    return render (request,'html/Projeto/projetos.html', context)

def detalhes_de_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    context = {'projeto': projeto}
    return render(request, 'html/Projeto/detalhes_de_projeto.html', context)
 