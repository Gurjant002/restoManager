"""
Configuración de URL para el proyecto restoManager.

La lista `urlpatterns` enruta las URLs a las vistas. Para más información, consulte:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Ejemplos:
Vistas basadas en funciones
    1. Agregue una importación:  from mi_app import views
    2. Agregue una URL a urlpatterns:  path('', views.home, name='home')
Vistas basadas en clases
    1. Agregue una importación:  from otro_app.views import Home
    2. Agregue una URL a urlpatterns:  path('', Home.as_view(), name='home')
Incluyendo otro URLconf
    1. Importe la función include():  from django.urls import include, path
    2. Agregue una URL a urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

from restoManager.views import home, puestos, about

from cocina_app.views import *
from restoManager_app.urls import urlpatterns as restoManager_urls
from login.urls import urlpatterns as login_urls

urlpatterns = [
    path('', about, name='about'),
    path('home/', home, name='home'),
    path('config/', include(restoManager_urls)),
    path('puestos/', puestos, name='puestos'),
    path('puestos/camarero/', include('camarero_app.urls')),
    path('puestos/cocina/', include('cocina_app.urls')),
    path('accounts/', include(login_urls)),
    path('admin/', admin.site.urls),
]

