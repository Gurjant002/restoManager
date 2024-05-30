"""
URLs para el módulo de camarero
"""

from django.urls import path
from .views import home, platos

urlpatterns = [
    path('', home, name='camarero_home'),
    path('platos', platos, name='camarero_platos'),
]
