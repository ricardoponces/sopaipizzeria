"""Sopaipizzeria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from CarritoApp.views import agregar_producto, cerrar_sesion, eliminar_producto, maestroProductos, restar_producto, limpiar_carrito, registrarProducto, eliminarProducto, edicionProducto
from CarritoApp.views import tienda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tienda, name="Tienda"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Agr"),
    path('eliminar/<int:producto_idv>/', eliminar_producto, name="Qtr"),
    path('restar/<int:producto_id>/', restar_producto, name="Rtr"),
    path('limpiar/', limpiar_carrito, name="Lpr"),
    path('accounts/', include('django.contrib.auth.urls')),  # INICIO SESION
    path('logout/', cerrar_sesion, name="logout"),  # INICIO SESION
    path('maestroProductos/', maestroProductos, name="maestroProductos"),
    path('registrarProducto/', registrarProducto, name="registrarProducto"),
    path('eliminarProducto/<nombre>', eliminarProducto, name="eliminarProducto"),
    path('edicionProducto/<nombre>', edicionProducto, name="edicionProducto"),
]
