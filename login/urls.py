from django.urls import path
from .views import login_view, salir

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', salir, name='logout'),
]