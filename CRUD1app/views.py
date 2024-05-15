from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
# Create your views here.

def plantilla (request):
    return render (request,'plantilla.html')

def home(request):
    
    return render(request, 'home.html')

def listar(request):

    all_object = Equipos.objects.all()
    
    
    
    return render(request, 'lista.html',{'all_object':all_object})



def c_modelo (request):
    
    if request.method == 'POST':
        # Si el formulario ha sido enviado, procesar los datos
        form = ModeloForm(request.POST)
        if form.is_valid():
            instance = form.save()  # Obtener la instancia del modelo guardado
            print("Datos guardados exitosamente:", instance)
            # Redirigir a alguna página de éxito
            return redirect('c_modelo')  # Ajusta esto según la URL de tu página de éxito
        else:
            print("Formulario inválido:", form.errors)
    else:
        # Si la solicitud no es un POST, mostrar el formulario en blanco
        form = ModeloForm()
    
    return render(request, 'crear/c_modelo.html', {'form': form})


def c_usuario(request):
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            instance = form.save()
            print("Datos guardados exitosamente:", instance)
            return redirect('c_usuario')
        else: 
            print ("Formulario inválido:", form.errors)
    else:
        form = UsuarioForm()
    
    return render (request,'crear/c_usuario.html',{'form':form})


def c_equipo(request):
    form = EquipoForm()  # Inicializar el formulario fuera de la lógica condicional

    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            instance = form.save()
            print("Datos guardados exitosamente:", instance)
            return redirect('c_equipo')
        else:
            print ("Formulario Invalido:", form.errors)

    return render (request,'crear/c_equipo.html', {'form':form})