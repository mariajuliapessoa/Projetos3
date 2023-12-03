from django.shortcuts import render

def projetos(request):
    context = {}
    return render (request,'html/Projeto/projetos.html', context)

 