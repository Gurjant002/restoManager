from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home, name='admin_home'),
    path('platos/', platos, name='admin_platos'),
    path('bebidas/', bebidas, name='admin_bebidas'),
    path('mesas/', mesas, name='admin_mesas'),
    path('categorias/', mesas, name='admin_categorias'),
    path('categorias/', mesas, name='admin_trabajadores'),
    path('categorias/', mesas, name='admin_config'),
]
