from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required #INICIO SESION
from django.contrib.auth import logout #INICIO SESION
from .models import Producto
from django.contrib.admin.views.decorators import staff_member_required #Limitar vista solo a miebros staff

# Create your views here.
from CarritoApp.Carrito import Carrito
from CarritoApp.models import Producto

# Create your views here.


@login_required
def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos':productos})

def cerrar_sesion(request): #INICIO SESION
    logout(request)
    return redirect('/')

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.elimminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar
    return redirect("Tienda")


@staff_member_required
def maestroProductos(request):
    productosListados= Producto.objects.all()
    return render(request, "gestionProductos.html", {"productos":productosListados})


def registrarProducto(request):
    nombre = request.POST['txtNombre']
    categoria = request.POST['txtCategoria']
    precio = request.POST['numPrecio']

    producto = Producto.objects.create(nombre=nombre, categoria=categoria, precio=precio)
    return redirect('maestroProductos')

def edicionProducto(request, Producto):
    producto = Producto.objects.get(Producto.id) #no se como traer el producto para eliminar minuto55.
    return render(request, "edicionProducto.html", {"producto": producto})

def editarProducto(request):
    nombre = request.POST['txtNombre']
    categoria = request.POST['txtCategoria']
    precio = request.POST['numPrecio']

    producto = Producto.objects.get(Producto.id) #no se como traer el producto para eliminar minuto55.
    producto.nombre = nombre
    producto.categoria = categoria
    producto.precio = precio
    producto.save()

    return redirect('maestroProductos')

def eliminarProducto(request, Producto):
    producto = Producto.objects.get(Producto.id) #no se como traer el producto para eliminar minuto55.
    producto.delete()

    return redirect('maestroProductos')
