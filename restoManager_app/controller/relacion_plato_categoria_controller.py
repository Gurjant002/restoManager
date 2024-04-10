from django.http import HttpRequest

from restoManager_app.models import Plato, Categoria, Plato_Categoria
from .plato_controller import PlatoController
from .categoria_controller import CategoriaController
from ..service.relacion_plato_categoria_service import PlatoCategoriaService

class RelacionController:
    __relacion_service: PlatoCategoriaService
    plato_controller: PlatoController
    __categoria_controller: CategoriaController

    def __init__(self):
        self.__relacion_service=PlatoCategoriaService()
        self.plato_controller=PlatoController()
        # print(self.plato_controller.dimeAlgo())
        self.__categoria_controller=CategoriaController()
    
    def tipos_de_peticiones(self, req: HttpRequest):
        if req.POST.get('new-plato-btn'):
            # CREAR
            nombre_plato = req.POST.get("nombre-plato")
            numero_plato = req.POST.get("numero-plato")
            nombre_categoria = req.POST.get("categoria")
            estado = int(req.POST.get("estado"))
            descripcion = req.POST.get("descripcion")
            self.crear_relacion(nombre_plato, numero_plato, nombre_categoria, estado, descripcion)
        
        elif req.POST.get('update-plate-btn'):
            # ACTUALIZA 
            btn_value=req.POST.get("update-plate-btn")
            id_relacion=btn_value.split("_")[2]
            nombre_plato=req.POST.get("nombre-plato")
            numero_plato=req.POST.get("numero-plato")
            nombre_categoria=req.POST.get("nombre-categoria")
            estado=req.POST.get("estado")
            descripcion=req.POST.get("descripcion")

            plato=self.plato_controller.actualizar_plato(nombre_plato, descripcion)
            categoria=self.__categoria_controller.actualizar_categoria(id_relacion, nombre_categoria)

            self.actualizar_relacion(id_relacion, numero_plato, estado)

    def crear_relacion(self, nombre_plato: str, numero_plato: int, nombre_categoria: str, estado:int, descripcion: str) -> str:
        plato=self.plato_controller.get_plato_by_name(nombre_plato)
        if plato is None:
            plato=self.plato_controller.crear_plato(nombre_plato, descripcion)

        categoria=self.__categoria_controller.get_categoria_by_name(nombre_categoria)
        if categoria is None:
            categoria=self.__categoria_controller.crear_categoria(nombre_categoria)

        resultado: str
        relacion=self.get_relacion_by_plato_and_categoria(plato, categoria)
        if relacion is None:
            relacion=self.__relacion_service.crear_relacion(plato, numero_plato, categoria, estado)
            resultado = "Nuevo plato y categoria creada."
        else:
            result = "El plato", nombre_plato, " en la categoria",nombre_categoria,"ya existe"
        return resultado

    def get_relacion_by_plato_and_categoria(self, plato: Plato, categoria: Categoria) -> Plato_Categoria | None:
        relacion=self.__relacion_service.get_relacion_by_plato_and_categoria(plato, categoria)
        return relacion

    def get_lista_relacion(self) -> dict:
        lista = self.__relacion_service.get_lista_relacion_plato_categoria()
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

    def actualizar_relacion(self, id_relacion:int ,numero_menu: int, estado) -> Plato_Categoria | None:
        relacion=self.__relacion_service.actualizar_relacion(id_relacion, numero_menu, estado)
        return relacion

    def borrar_relacion(self, id_relacion:int) -> None:
        self.__relacion_service.eliminar_relacion(id_relacion)

""" 
def crear_plato_categoria(req: HttpRequest):
    nombre_plato = req.POST.get("nombre-plato")
    numero_plato = req.POST.get("numero-plato")
    nombre_categoria = req.POST.get("categoria")
    estado = int(req.POST.get("estado"))
    descripcion = req.POST.get("descripcion")
    
    plato=PlatoController.get_plato_by_name(nombre_plato)
    if plato is None:
        plato=PlatoController.crear_plato(nombre_plato, descripcion)

    categoria = CategoriaController.get_categoria_by_name(nombre_categoria)
    if categoria is None:
        categoria=CategoriaController.crear_categoria(nombre_categoria)

    relacion_plato_cat = get_relacion_by_plato_cat(plato, categoria)
    
    if relacion_plato_cat is None:
        relacion_plato_cat


def get_relacion_by_plato_cat(plato: Plato, categoria: Categoria):
    relacion = Plato_Categoria.objects.filter(plato=plato, categoria=categoria)
    return relacion """