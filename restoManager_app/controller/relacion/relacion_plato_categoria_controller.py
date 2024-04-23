from django.http import HttpRequest

from restoManager_app.models import Plato, Categoria, Plato_Categoria
from ..plato.plato_controller import PlatoController
from ..categoria.categoria_controller import CategoriaController
from ...service.relacion.relacion_plato_categoria_service import PlatoCategoriaService

class RelacionController:
    __relacion_service: PlatoCategoriaService
    plato_controller: PlatoController
    __categoria_controller: CategoriaController

    def __init__(self):
        self.__relacion_service=PlatoCategoriaService()
        self.plato_controller=PlatoController()
        self.__categoria_controller=CategoriaController()
    
    def tipos_de_peticiones(self, req: HttpRequest) :
        btn_update=req.POST.get("update-plate-btn")
        btn_create=req.POST.get("new-plato-btn")
        btn_eliminar=req.POST.get("eliminar-btn")
        try:
            id_relacion=int(btn_update.split("_")[2])
        except:
            id_relacion=0
            print("ERROR EN EL ID DE LA RELACION")
        nombre_plato=req.POST.get("nombre-plato")
        numero_menu=req.POST.get("numero-menu")
        nombre_categoria=req.POST.get("categoria")
        estado=req.POST.get("estado")
        descripcion=req.POST.get("descripcion")
        if btn_eliminar:
            eliminar=btn_eliminar.split("|")[1]
        else:
            eliminar=""

        # CREAR
        if req.POST.get('new-plato-btn'):
            print("CREAR")
            return self.crear_relacion(nombre_plato, numero_menu, nombre_categoria, estado, descripcion)

        # ACTUALIZA 
        elif req.POST.get('update-plate-btn'):
            print("ACTUALIZA")
            
            rel=self.get_relacion_by_id(id_relacion)
            
            plato=rel[rel.count()-1].plato
            plato=self.plato_controller.actualizar_plato(plato.id, nombre_plato, descripcion)
            
            categoria=rel[rel.count()-1].categoria
            categoria=self.__categoria_controller.actualizar_categoria(categoria.id, nombre_categoria)
            self.actualizar_relacion(id_relacion, numero_menu, estado)
        
        # ELIMINAR
        elif req.POST.get('eliminar-btn'):
            print("ELIMINAR")
            relacion = self.get_relacion_by_id(int(eliminar))
            plato = relacion[relacion.count()-1].plato
            categoria = relacion[relacion.count()-1].categoria
            self.borrar_relacion(relacion[relacion.count()-1].id)
            self.plato_controller.eliminar_plato(plato.id)
            self.__categoria_controller.eliminar_categoria(categoria.id)

    def crear_relacion(self, nombre_plato: str, numero_menu: int, nombre_categoria: str, estado:int, descripcion: str) -> str:
        plato=self.plato_controller.get_plato_by_name(nombre_plato)
        if not plato:
            plato=self.plato_controller.crear_plato(nombre_plato, descripcion)

        categoria=self.__categoria_controller.get_categoria_by_name(nombre_categoria)
        if not categoria:
            categoria=self.__categoria_controller.crear_categoria(nombre_categoria)

        relacion=self.get_relacion_by_plato_and_categoria(plato, categoria)
        if not relacion:
            if numero_menu == 0:
                num = self.__relacion_service.get_lista_relacion_plato_categoria()
                if num is not None:
                    numero_menu = num[num.count()-1].numero_menu + 1
            relacion=self.__relacion_service.crear_relacion(plato, numero_menu, categoria, estado)
            resultado = "> Nuevo plato y categoria creada."
            print("relacion_controller > crear_relacion > NUEVA RELACION")
        else:
            resultado = "El plato", nombre_plato, " en la categoria",nombre_categoria,"ya existe"
        print("relacion_controller > crear_relacion > resultado:", resultado)
        return resultado

    def get_relacion_by_id(self, id_relacion: int) -> Plato_Categoria:
        relacion = self.__relacion_service.get_relacion_by_id(id_relacion)
        return relacion

    def get_relacion_by_plato_and_categoria(self, plato: Plato, categoria: Categoria) -> Plato_Categoria | None:
        relacion=self.__relacion_service.get_relacion_by_plato_and_categoria(plato, categoria)
        print("get_relacion_by_plato_and_categoria > relacion:", relacion)
        return relacion

    def get_relacion_by_numero_menu(self, numero_menu: int):
        print("> NUMERO MENU ", numero_menu)
        relacion = self.__relacion_service.get_relacion_by_numero_menu(numero_menu)
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
