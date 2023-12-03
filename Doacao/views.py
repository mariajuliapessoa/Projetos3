from django.shortcuts import render

def doacao(request):
    context = {}
    return render(request, 'html/Doacao/doacao.html', context)
