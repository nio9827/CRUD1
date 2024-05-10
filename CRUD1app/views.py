from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *

# Create your views here.

def plantilla (request):
    return render (request,'plantilla.html')

def home(request):
    
    return render(request, 'home.html')

def listar(request):
    
    return render(request, 'lista.html')



def c_modelo (request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render (request, "crear/c_modelo.html", {"form": form})


def c_usuario(request):
    return render (request,'crear/c_usuario.html')


def c_equipo(request):
    return render (request,'crear/c_equipo.html')