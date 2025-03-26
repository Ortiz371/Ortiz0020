from django.shortcuts import render
from .models import Resolucion

def index(request):
    return render(request, 'resoluciones/index.html')

def buscar(request):
    year = request.GET.get('year', '')
    resolution = request.GET.get('resolution', '').lower()
    query = request.GET.get('query', '').lower()

    resultados = Resolucion.objects.all()

    if year:
        resultados = resultados.filter(year=year)
    if resolution:
        resultados = resultados.filter(res__iexact=resolution)
    if query:
        resultados = resultados.filter(tema__icontains=query) | resultados.filter(expte__icontains=query)

    return render(request, 'resoluciones/resultados.html', {'resultados': resultados})
