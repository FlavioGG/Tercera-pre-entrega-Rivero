# views.py
from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

from django.shortcuts import render, redirect
from .forms import ProductoForm, ClienteForm, BusquedaForm
from .models import Producto

def ingresar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm()
    return render(request, 'compra/ingresar_producto.html', {'form': form})

def buscar_producto(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            resultados = Producto.objects.filter(nombre__icontains=termino_busqueda)
            return render(request, 'compra/resultados_busqueda.html', {'resultados': resultados})
    else:
        form = BusquedaForm()
    return render(request, 'compra/buscar_producto.html', {'form': form})

