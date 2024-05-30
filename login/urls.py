from django.urls import path
from .views import login_view, salir

"""
Define las URL para el inicio de sesión y el cierre de sesión.
"""

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', salir, name='logout'),
]
