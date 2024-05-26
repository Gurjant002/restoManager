from django.urls import path
from .views import *
urlpatterns = [
    path('', cocina, name='cocina'),
    path('pedidos', mesas_pedidos, name='pedidos'),
    path('listar', listar, name='listar'),
    path('listar/estado', cambiar_estado, name='estado'),
]
