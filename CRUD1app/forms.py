from django import forms
from django.forms import ModelForm
from .models import *


    
class ModeloForm(ModelForm):
    class Meta:
        model = Modelo_E
        fields = ['modelos', 'marca', 'tipos']
        

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ["nombre","apellido", "correo","tipos"]
        
        
class EquipoForm(ModelForm):
    class Meta:
        model = Equipos
        fields = ["usuario","marca","modelo","tipo"]