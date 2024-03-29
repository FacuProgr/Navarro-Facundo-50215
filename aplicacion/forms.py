from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Ropa, Comentario, Perfil, Avatar

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['usuario', 'edad', 'pais', 'direccion', 'genero']
        
class Ropa_Form(forms.ModelForm):
    OPCIONES_GENERO = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    nombre = forms.CharField(max_length=60, required=True)
    genero = forms.ChoiceField(choices=OPCIONES_GENERO, label='Género')
    precio = forms.CharField(max_length=60, required=True)
    descripcion = forms.CharField(max_length=60)
    img = forms.ImageField(required=True)
    
    class Meta:
        model = Ropa
        fields = ["nombre","genero","precio","descripcion","img"]
    
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme su contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class UserEditForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

class AvatarForm(forms.ModelForm):
      class Meta:
        model = Avatar
        fields = ['imagen']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre', 'contenido']

class AgregarAlCarritoForm(forms.Form):
    producto = forms.ModelChoiceField(queryset=Ropa.objects.all())
    cantidad = forms.IntegerField(min_value=1, initial=1)
    
class AgregarCarroForm(forms.Form):
    cantidad = forms.IntegerField(min_value=1)