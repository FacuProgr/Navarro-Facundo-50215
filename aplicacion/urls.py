from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('carrito/', carrito, name='carrito'),
    path('descripcion/', descripcion, name='descripcion'),
    path('shop/', shop, name='shop'),
    path('perfil/', perfil_formu, name = 'perfil_formu'),
    
    #ROPA-------------------------------------------------------------------------
    path('ropa/', RopaList.as_view(), name="ropa"), 
    path('ropa_create/', RopaCreate.as_view(), name="ropa_create"), 
    path('ropa_update/<int:pk>/', RopaUpdate.as_view(), name="ropa_update"), 
    path('ropa_delete/<int:pk>/', RopaDelete.as_view(), name="ropa_delete"), 
    
    #BUSQUEDA----------------------------------------------------------------------
    path('buscar_ropa/', buscarRopa, name="buscar_ropa"),
    path('encontrar_ropa/', encontrarRopa, name="encontrar_ropa"),
]