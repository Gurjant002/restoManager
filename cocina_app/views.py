from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from asgiref.sync import sync_to_async
import logging
 
logger = logging.getLogger(__name__)

def cocina(request):
    diccionario = {}
    return render(request, 'cocina/pedidos.html', diccionario)