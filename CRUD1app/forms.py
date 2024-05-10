from django import forms


class modelo(forms.Form):
    Modelo = forms.CharField(label="Ingresar Modelos", max_length=100)