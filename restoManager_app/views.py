from django.http import HttpRequest
from django.shortcuts import render
from restoManager_app.models import Categoria, Plato, Plato_Categoria
from datetime import datetime
# Create your views here.

# Funciones de para tener codigo limpio
# Funciones para crear registros
def crear_plato(post_request:HttpRequest):
    new_plato = ""
    new_cat = ""
    result = ""
    
    nombrePlato = post_request.POST.get("nombre-plato")
    numeroPlato = post_request.POST.get("numero-plato")
    categoria = post_request.POST.get("categoria")
    descripcion = post_request.POST.get("descripcion")
    
    platoExiste = Plato.objects.filter(nombre=nombrePlato).first()

    if platoExiste is None:
        catExiste = Categoria.objects.filter(nombre=categoria).first()
        if catExiste is None:
            new_cat = crear_categoria(categoria)
        else:
            new_cat = catExiste
            
        new_plato = Plato.objects.create(nombre=nombrePlato, descripcion=descripcion)
        crear_plato_cat_relacion(new_plato, numeroPlato, new_cat)
        result = "Nuevo plato creado:",new_plato.nombre
    else:
        result = "El plato que intentas crear, ya existe:",nombrePlato

    return result

def crear_categoria(nombre: str):
    new_cat = Categoria.objects.create(nombre=nombre)
    return new_cat

def crear_plato_cat_relacion(plato, numero, categoria):
    relacion = Plato_Categoria.objects.create(plato=plato, numero_menu=numero, categoria=categoria)
    return relacion

# Funciones para eliminar
def eliminar_plato_cat_relacion(post_request:HttpRequest):
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
    return result


# Funciones para vistas
def listar():
    lista = Plato_Categoria.objects.all()
    lista_platos = []
    lista_categoria = []

    if lista != None:
        for elements in lista:
            lista_platos.append(elements.plato)
            lista_categoria.append(elements.categoria)

    diccionario = {
        'lista': lista,
        'lista_platos': lista_platos,
        'lista_categoria': lista_categoria
        }
    return diccionario

def crear_alerta():
    ahora = datetime.now()
    tiempo = ahora.strftime("%H:%M")
    return tiempo

# Views
def platos(request):
    diccionario = {}
    if request.method == "POST":
        if request.POST.get('new-plato-btn'):
            print("IN")
            result = {}
            tiempo = crear_alerta()
            result = {
                'resultado':crear_plato(request),
                'tiempo':tiempo
            }
            diccionario.update({'resultado_new_plato':result})
        
        if request.POST.get('editar-btn'):
            print('editar-btn')
            
        if request.POST.get('desactivar-btn'):
            print('editar-btn')
            
        if request.POST.get('eliminar-btn'):
            result = eliminar_plato_cat_relacion(request)
            diccionario.update({'resultado_plato_eliminado': result})
        
        diccionario.update(listar())
        return render(request, "restoManager/secciones/platos.html", diccionario)

    diccionario = listar()
    return render(request, "restoManager/secciones/platos.html", diccionario)