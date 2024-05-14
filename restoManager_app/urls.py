from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='admin_home'),
    path('platos/', platos, name='admin_platos'),
    path('bebidas/', bebidas, name='admin_bebidas'),
    path('categorias/', categorias, name='admin_categorias'),
    path('mesas/', mesas, name='admin_mesas'),
    path('trabajadores/', trabajadores, name='admin_trabajadores'),
    path('categorias/', mesas, name='admin_config'),
]
