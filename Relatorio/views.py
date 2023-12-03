from django.shortcuts import render

def relatorios(request):
    context = {}
    return render(request, 'html/Relatorio/relatorios.html', context)
 