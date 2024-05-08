from django.urls import path
from . import views

urlpatterns = [
    path('plantilla', views.plantilla, name='plantilla'),
    path('home', views.home, name='home'),
    path('listar', views.listar, name='listar'),
    path('crear', views.crear, name='crear'),
]
