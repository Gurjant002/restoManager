from django.urls import path

from .views import cocina, mesas_pedidos

urlpatterns = [
    path('', cocina, name='cocina'),
    path('pedidos', mesas_pedidos, name='pedidos'),
]
"""
Urls para la aplicación de cocina.

Define las urls para la aplicación de cocina.
"""

