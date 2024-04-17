from django.http import HttpRequest
from django.shortcuts import render
from datetime import datetime

# from restoManager_app.models import Plato_Categoria
from .controller.relacion_plato_categoria_controller import RelacionController

# Create your views here.

# Funciones de para tener codigo limpio
# Funciones para crear registros
""" def crear_plato(post_request:HttpRequest):
    new_plato = ""
    new_cat = ""
    result = ""
    
    nombrePlato = post_request.POST.get("nombre-plato")
    numeroPlato = post_request.POST.get("numero-plato")
    categoria = post_request.POST.get("categoria")
    estado = int(post_request.POST.get("estado"))
    descripcion = post_request.POST.get("descripcion")
    
    platoExiste = Plato.objects.filter(nombre=nombrePlato).first()

    if platoExiste is None:
        catExiste = Categoria.objects.filter(nombre=categoria).first()
        if catExiste is None:
            new_cat = crear_categoria(categoria)
        else:
            new_cat = catExiste
            
        new_plato = Plato.objects.create(nombre=nombrePlato, descripcion=descripcion)
        
        crear_plato_cat_relacion(new_plato, numeroPlato, new_cat, estado)
        result = "Nuevo plato creado:",new_plato.nombre
    else:
        result = "El plato que intentas crear, ya existe:",nombrePlato

    return result

def crear_categoria(nombre: str):
    new_cat = Categoria.objects.create(nombre=nombre)
    return new_cat

def crear_plato_cat_relacion(plato, numero, categoria, estado):
    relacion = Plato_Categoria.objects.create(plato=plato, numero_menu=numero, categoria=categoria, habilitado=estado)
    return relacion
 """


# Funciones para eliminar
""" def eliminar_plato_cat_relacion(post_request:HttpRequest):
    texto = post_request.POST.get("eliminar-btn")
    texto = texto.split("|")
    plato_id = int(texto[1])
    print(plato_id)
    result = ""
    
    platoExist = Plato_Categoria.objects.filter(id=plato_id)
    if platoExist != None:
        Plato_Categoria.objects.filter(id=plato_id).delete()
        result = "Plato eliminado."
    else: # Esta condicion es inecesaria.
        result = "El plato que intentas borrar, no existe"
    return result """


# Funciones para vistas
""" def listar():

    return diccionario
 """
def crear_alerta():
    ahora = datetime.now()
    tiempo = ahora.strftime("%H:%M")
    return tiempo

def actualizar_cat_plato(post_request: HttpRequest):
    idPlato = post_request.POST.get("id-plato")
    numeroPlato = post_request.POST.get("numero-plato")
    nombrePlato = post_request.POST.get("nombre-plato")
    categoria = post_request.POST.get("categoria")
    descripcion = post_request.POST.get("descripcion")
    estado = int(post_request.POST.get("estado"))
    
def crear_plato(request):
    print("Hola")

# Views
def platos(request):
    diccionario = {}
    relacionController = RelacionController()
    if request.method == "POST":
        if request.POST.get('new-plato-btn'):
            result = {}
            tiempo = crear_alerta()
            result = {
                'resultado':relacionController.tipos_de_peticiones(request),
                'tiempo':tiempo
            }
            print(result)
            diccionario.update({'resultado_new_plato':result})
        
        elif request.POST.get('update-plate-btn'):
            print('editar-btn')
            relacionController.tipos_de_peticiones(request)
            
        elif request.POST.get('eliminar-btn'):
            result = relacionController.tipos_de_peticiones(request)
            diccionario.update({'resultado_plato_eliminado': result})
        
        diccionario.update(relacionController.get_lista_relacion())
        return render(request, "restoManager/secciones/platos.html", diccionario)

    diccionario = relacionController.get_lista_relacion()
    return render(request, "restoManager/secciones/platos.html", diccionario)

def test(request):
    print("Hola mundo")
    return render(request, "restoManager/base/base.html")