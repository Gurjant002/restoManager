"""
URL configuration for restoManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cocina_app.views import *
from restoManager_app.views import *
import logging

logger = logging.getLogger('tuna')
logger.debug("Hello, world. I'm fine.")
logger.info("Hello, world. I'm fine.")
urlpatterns = [
    # path('', home),
    path('platos/', platos),
    path('admin/', admin.site.urls),
    path('mesas/', mesas),
    path('avisos/', avisos),
]
