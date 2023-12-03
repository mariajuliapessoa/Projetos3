from django.shortcuts import render

def demanda(request):
    context = {}
    return render(request, 'html/Demanda/demanda.html', context)
