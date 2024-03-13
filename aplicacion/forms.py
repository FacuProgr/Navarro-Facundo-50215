from django import forms

class Perfil_Formulario(forms.Form):
    usuario = forms.CharField()
    contraseña = forms.CharField()
    edad = forms.CharField()
    pais = forms.CharField()
    direccion = forms.CharField()
    genero = forms.CharField()
        
class Ropa_Form(forms.Form):
    nombre = forms.CharField(max_length=60, required=True)
    genero = forms.CharField(max_length=60, required=True)
    precio = forms.CharField(max_length=60, required=True)