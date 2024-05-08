from django.shortcuts import render

# Create your views here.

def plantilla (request):
    return render (request,'plantilla.html')

def home(request):
    
    return render(request, 'home.html')

def listar(request):
    
    return render(request, 'lista.html')


def crear (request):
    return render (request,'crear.html')