from django.contrib import admin
from . models import *

# Register your models here.

#se crean las vistas de las tablas que se mostraran en el admin y se le asignan los campos que se mostraran

class Marca_EAdmin(admin.ModelAdmin):
    list_display = ("nombre","fecha_creacion")

class Modelo_EAdmin(admin.ModelAdmin):
    list_display = ("modelos","fecha_creacion")

class Tipo_EAdmin(admin.ModelAdmin):
    list_display = ("tipos","fecha_creacion")
    
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nombre","apellido","correo","fecha_creacion")
    
class EquiposAdmin(admin.ModelAdmin):
    list_display = ("marca","modelo","tipo","usuario","fecha_creacion")


admin.site.register(Marca_E,Marca_EAdmin)
admin.site.register(Modelo_E,Modelo_EAdmin)
admin.site.register(Tipo_E,Tipo_EAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Equipos,EquiposAdmin)