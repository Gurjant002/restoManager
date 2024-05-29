from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='admin_home'),
    path('platos/', platos, name='admin_platos'),
    path('bebidas/', bebidas, name='admin_bebidas'),
    path('categorias/', categorias, name='admin_categorias'),
    path('ubicaciones/',ubicaciones, name='admin_ubicaciones'),
    path('trabajadores/', trabajadores, name='admin_trabajadores'),
    path('trabajadores/camareros', camareros, name='admin_camareros'),
    path('categorias/',ubicaciones, name='admin_config'),
]
