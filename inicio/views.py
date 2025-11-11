from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Auto

def inicio(request):
    #return HttpResponse('<h1>Hola soy el proyecto</h1>')
    return render(request, 'inicio.html')

def otra(request):
    #return HttpResponse('<h1>Hola soy el proyecto</h1>')
    return render(request, 'otra.html')

def crear_auto(request, marca, modelo):
    auto = Auto(marca=marca, modelo=modelo)
    auto.save()
    return render(request, 'crear_auto.html', {'objeto_guardado': auto})

def listar_autos(request):
    autos = Auto.objects.all()

    return render (request, 'listar_autos.html', {'listado_de_autos': autos})


