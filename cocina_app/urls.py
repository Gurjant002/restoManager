from django.urls import path
from .views import *
urlpatterns = [
    path('', cocina, name='cocina_home'),
]
