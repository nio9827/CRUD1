from django.urls import path
from . import views

urlpatterns = [
    path('plantilla', views.plantilla, name='plantilla'),
    path('home', views.home, name='home'),
    path('listar', views.listar, name='listar'),
    path('c_modelo', views.c_modelo, name='c_modelo'),
    path('c_usuario', views.c_usuario, name='c_usuario'),
    path('c_equipo', views.c_equipo, name='c_equipo'),
]
