from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    nombres = request.POST['nombres']
    #nombres = nombre.upper()
    #return render(request,'proceso.html', {'name':nombre})

def inicio(request):
    return render(request,'inicio.html')

def acercaDe(request):
    return render(request,'acercaDe.html')

def instrucciones(request):
    return render(request,'instrucciones.html')

def estadisticas(request):
    return render(request,'estadisticas.html')

def reto(request):
    return render(request,'reto.html')

def contactanos(request):
    return render(request,'contactanos.html')