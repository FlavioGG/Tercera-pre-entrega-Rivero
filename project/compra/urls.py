from django.urls import path
from . import views

urlpatterns = [
    path('ingresar_producto/', views.ingresar_producto, name='ingresar_producto'),
    path('buscar_producto/', views.buscar_producto, name='buscar_producto'),
]
