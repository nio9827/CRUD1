from django.db import models

# Create your models here.

#creas el modelo y le asignas los atributos que se mostraran en la base de datos

class Marca_E(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre}"


class Tipo_E(models.Model):
    tipos = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.tipos}"
    
    
class Modelo_E(models.Model):
    modelos = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now_add=True)
    marca = models.ForeignKey(Marca_E, on_delete=models.CASCADE)
    tipos = models.ForeignKey(Tipo_E, on_delete=models.CASCADE,unique=True, null=True)
    def __str__(self):
        return f"{self.modelos}{self.fecha_creacion}{self.marca}"

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    tipos = models.ForeignKey(Tipo_E, on_delete=models.CASCADE,unique=True, null=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre}{self.apellido}{self.correo}{self.fecha_creacion}"
    
class Equipos(models.Model):
    marca = models.ForeignKey(Marca_E, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo_E, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo_E, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.marca}{self.modelo}{self.usuario}{self.tipo}{self.fecha_creacion}"