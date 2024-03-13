from django.db import models

# Create your models here.

class Perfil(models.Model):
    usuario = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=30)
    edad = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.usuario}"

class Ropa(models.Model):
    nombre = models.CharField(max_length=60)
    genero = models.CharField(max_length=60)
    precio = models.CharField(max_length=60)
    def __str__(self):
        return f"{self.nombre}, {self.genero}, {self.precio}"