from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name='inicio'),
    
    #ROPA CRUD-------------------------------------------------------------------------
    path('ropa/', mostrar_ropa, name="ropa"), 
    path('ropa_create/', crear_ropa, name="ropa_create"), 
    path('ropa_update/<int:id>/', editarRopa, name="ropa_update"), 
    path('ropa_delete/<int:pk>/', RopaDelete.as_view(), name="ropa_delete"),
    
    #BUSQUEDA----------------------------------------------------------------------
    path('buscar_ropa/', buscarRopa, name="buscar_ropa"),
    path('encontrar_ropa/', encontrarRopa, name="encontrar_ropa"),
    
    #LOGIN-------------------------------------------------------------------------
    path('login/', login_request, name="login"),
    path('logout/', logout_view, name='logout'),
    path('registrar/', register, name="registrar"),
    
    #EDITAR PERFIL------------------------------------------------------------------
    path('editar_perfil/', editarPerfil, name='editar_perfil'),
    path('<int:pk>/password/', CambiarClave.as_view(), name='cambiar_clave'),
    
    #FUNCIONALIDADES SHOP------------------------------------------------------------
    path('editar_ropa/', editarRopa, name='editar_ropa'),
    path('descripcion_ropa/<int:id>//', descripcionRopa, name='descripcion_ropa'),
    path('carrito/', verCarrito, name="carrito"),
    path("anadir_carro/<int:id>/", anadirCarro, name='anadir_carro'),
    path('carro_delete/<int:item_id>/', eliminarDelCarro, name='carro_delete'),
    path('confirmar_compra/', comprar, name='confirmar_compra'),
    path('ropa_hombre/', ropaHombre, name='ropa_hombre'),
    path('ropa_mujer/', ropaMujer, name='ropa_mujer'),
    
    #PORTFOLIO------------------------------------------------------------------------
    path('portfolio/', portfolio, name='portfolio')
]