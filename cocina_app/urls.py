from django.urls import path
from .views import *
urlpatterns = [
    path('', cocina, name='cocina'),
    path('pedidos', mesas_pedidos, name='pedidos'),
]
