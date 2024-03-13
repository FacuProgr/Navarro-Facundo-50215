from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# Create your views here.
def inicio(request):
    return render(request,"aplicacion/index.html")

def carrito(request):
    return render(request, "aplicacion/carrito.html")

def shop(request):
    return render(request, "aplicacion/shop.html")

def descripcion(request):
    return render(request, "aplicacion/descripcion.html")

def perfil_formu(request):
    if request.method == "POST":
        mi_formulario = Perfil_Formulario(request.POST)
        print(mi_formulario)
        
        if mi_formulario.is_valid():
            perf_usuario = mi_formulario.cleaned_data.get('usuario')
            contraseña = mi_formulario.cleaned_data['contraseña']
            edad = mi_formulario.cleaned_data['edad']
            pais = mi_formulario.cleaned_data['pais']
            direccion = mi_formulario.cleaned_data['direccion']
            genero = mi_formulario.cleaned_data['genero']  
            
                      
            return render(request,"aplicacion/index.html")
    else:
        mi_formulario = Perfil_Formulario()
        
    return render(request, "aplicacion/perfil.html", {"mi_formulario":mi_formulario})

#ROPA--------------------------------------------------------------------------------------
class RopaList(ListView):
    model = Ropa

class RopaCreate(CreateView):
    model = Ropa
    fields = ["nombre", "genero", "precio"]
    success_url = reverse_lazy("ropa")

class RopaUpdate(UpdateView):
    model = Ropa
    fields = ["nombre", "genero", "precio"]
    success_url = reverse_lazy("ropa")

class RopaDelete(DeleteView):
    model = Ropa
    success_url = reverse_lazy("ropa")

#BUSQUEDA------------------------------------------------------------------------------------
def buscarRopa(request):
    return render(request, "aplicacion/busqueda.html")

def encontrarRopa(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        ropa_list = Ropa.objects.filter(nombre__icontains=patron)
        contexto = {"ropa_list": ropa_list}
        return render(request, "aplicacion/ropa_list.html", contexto)
    

    contexto = {'ropa_list': Ropa.objects.all()}
    return render(request, "aplicacion/ropa_list.html", contexto)


