from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from asgiref.sync import sync_to_async
from .controller.camarero_controller import CamareroController
import logging
 
logger = logging.getLogger(__name__)

# Create your views here.
@sync_to_async
@login_required
def home(request: HttpRequest):
    camarero = CamareroController(request)
    diccionario = camarero.peticiones()
    return render(request, "camarero/camarero.html", diccionario)