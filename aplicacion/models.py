from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    edad = models.IntegerField(blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    genero = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username

class Ropa(models.Model):
    nombre = models.CharField(max_length=60)
    genero = models.CharField(max_length=60)
    precio = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=60)
    img = models.ImageField(upload_to="ropaimagenes")
    def __str__(self):
        return f"{self.nombre}, {self.genero}, {self.precio}, {self.img}, {self.descripcion}"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"

class Comentario(models.Model):
    nombre = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ropa = models.ForeignKey(Ropa, related_name='comentarios', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class CarritoItem(models.Model):
    producto = models.ForeignKey(Ropa, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)