from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.urls import reverse_lazy

from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView

from django.http import JsonResponse

# Create your views here.
#INICIO--------------------------------------------------------------------------------------
def inicio(request):
    return render(request,"aplicacion/index.html")

#PORTFOLIO-----------------------------------------------------------------------------------
def portfolio(request):
    return render(request, "aplicacion/portfolio.html")


#BUSQUEDA------------------------------------------------------------------------------------
@login_required
def buscarRopa(request):
    return render(request, "aplicacion/busqueda.html")

@login_required
def encontrarRopa(request):
    if request.GET.get("buscar"):
        patron = request.GET.get("buscar")

        ropa = Ropa.objects.filter(nombre__icontains=patron)

        contexto = {"ropa": ropa}
        return render(request, "aplicacion/ropa_list.html", contexto)
    else:
        contexto = {'ropa': Ropa.objects.all()}
        return render(request, "aplicacion/ropa_list.html", contexto)

#LOGIN-----------------------------------------------------------------------------------------
def login_request(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        contraseña = request.POST["password"]
        user = authenticate(request, username=usuario, password=contraseña)
        if user is not None:
            login(request,user)
             #____ Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #__________________________________________

            return render(request, "aplicacion/index.html")
        else:
            return redirect(reverse_lazy("login"))
    
    else:
        miForm = AuthenticationForm()
    
    return render(request,"aplicacion/login.html", {"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy("inicio"))
    
    else:
        miForm = RegistroForm()
    return render(request,"aplicacion/registro.html", {"form": miForm})

def logout_view(request):
    logout(request)
    return redirect('inicio')
            
#PERFIL-------------------------------------------------------------------------
@login_required
def editarPerfil(request):
    usuario = request.user
    perfil_usuario, creado = Perfil.objects.get_or_create(usuario=usuario)
    avatar_existente, creado = Avatar.objects.get_or_create(user=usuario)

    if request.method == "POST":
        form_perfil = PerfilForm(request.POST, instance=perfil_usuario)
        form_avatar = AvatarForm(request.POST, request.FILES, instance=avatar_existente)

        if form_perfil.is_valid() and form_avatar.is_valid():
            form_perfil.save()
            form_avatar.save()
            request.session["avatar"] = avatar_existente.imagen.url
            return redirect('inicio')
    else:
        form_perfil = PerfilForm(instance=perfil_usuario)
        form_avatar = AvatarForm(instance=avatar_existente)

    return render(request, "aplicacion/editar_perfil.html", {"form_perfil": form_perfil, "form_avatar": form_avatar})
#CAMBIO CLAVE-------------------------------------------------------------------------------------

class CambiarClave(LoginRequiredMixin,PasswordChangeView):
    template_name = "aplicacion/cambiar_clave.html"
    success_url = reverse_lazy("inicio")


#ROPA CRUD-------------------------------------------------------------------------------
@login_required
def mostrar_ropa(request):
    ropa = Ropa.objects.all()
    return render(request, "aplicacion/ropa_list.html", {"ropa" : ropa})

    
@login_required
def crear_ropa(request):
    if request.method == "POST":
        form = Ropa_Form(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('ropa')
    else:    
        form = Ropa_Form()

    return render(request, "aplicacion/ropa_form.html", {"form": form })

@login_required
def editarRopa(request, id):
    ropa = Ropa.objects.get(id=id)
    form = Ropa_Form(instance=ropa)

    if request.method == "POST":
        form = Ropa_Form(data=request.POST, instance=ropa, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ropa')
    else:
        return render(request, "aplicacion/editar_ropa.html", {"form": form})

class RopaDelete(LoginRequiredMixin,DeleteView):
    model = Ropa
    success_url = reverse_lazy("ropa")

#FUNCIONALIDAD SHOP-------------------------------------------------------------------------------
@login_required
def descripcionRopa(request, id):
    ropa = Ropa.objects.get(id=id)
    comentarios = Comentario.objects.filter(ropa=ropa)
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            contenido = form.cleaned_data['contenido']
            comentario = Comentario(nombre=nombre, contenido=contenido, ropa=ropa)
            comentario.save()
            return redirect('descripcion_ropa', id=id)
    else:
        form = ComentarioForm()
    
    return render(request, 'aplicacion/descripcion_ropa.html', {'ropa': ropa, 'comentarios': comentarios, 'form': form})

def ropaHombre(request):
    ropa_hombre = Ropa.objects.filter(genero='M')
    return render(request, 'aplicacion/ropa_hombre.html', {'ropa_hombre': ropa_hombre})

def ropaMujer(request):
    ropa_mujer = Ropa.objects.filter(genero='F')
    return render(request, 'aplicacion/ropa_mujer.html', {'ropa_mujer': ropa_mujer})

@login_required
def anadirCarro(request, id):
    if request.method == 'POST':
        form = AgregarAlCarritoForm(request.POST)
        if form.is_valid():
            producto = form.cleaned_data['producto']
            cantidad = form.cleaned_data['cantidad']
            # Verificar si el producto ya está en el carrito
            try:
                carrito_item = CarritoItem.objects.get(producto=producto)
                carrito_item.cantidad += cantidad
                carrito_item.save()
            except CarritoItem.DoesNotExist:
                CarritoItem.objects.create(producto=producto, cantidad=cantidad)
            return redirect('carrito')
    else:
        form = AgregarAlCarritoForm()
    return render(request, 'aplicacion/anadir_carro.html', {'form': form})

@login_required
def verCarrito(request):
    items_carrito = CarritoItem.objects.all()
    # Pasar los elementos del carrito a la plantilla
    return render(request, 'aplicacion/carrito.html', {'items_carrito': items_carrito})

@login_required
def mostrar_formulario(request, ropa_id):
    ropa = Ropa.objects.get(id=ropa_id)
    if request.method == 'POST':
        form = AgregarCarroForm(request.POST)
        if form.is_valid():
            cantidad = form.cleaned_data['cantidad']
    else:
        form = AgregarCarroForm()
    return render(request, 'aplicacion/agregar_carro.html', {'ropa': ropa, 'form': form})

def eliminarDelCarro(request, item_id):
    item = get_object_or_404(CarritoItem, id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('carrito') 

    return render(request, 'aplicacion/carro_delete.html', {'item': item})

def comprar(request):
    if request.method == 'POST':
        CarritoItem.objects.all().delete()
        return redirect('inicio')
    
    return render(request, 'aplicacion/confirmar_compra.html')

def mostrar_confirmacion_compra(request):
    # Obtener el nombre del producto (reemplaza esta lógica con la tuya)
    nombre_producto = "Camisa elegante"  # Aquí deberías obtener el nombre del producto de alguna manera
    
    return render(request, 'aplicacion/confirmar_compra.html', {'nombre_producto': nombre_producto})