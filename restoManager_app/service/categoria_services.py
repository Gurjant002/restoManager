from restoManager_app.models import Categoria

class CategoriaService:
    __categoria: Categoria
    
    def __init__(self):
        self.__categoria = Categoria

    def get_categoria_by_name(self, nombre_categoria) -> Categoria | None:
        categoria=self.__categoria.objects.filter(nombre_categoria).first

    def get_categoria_by_id(self, id:int) -> Categoria | None:
        categoria=self.__categoria.objects.filter(id)

    def crear_categoria(self, nombre: str) -> Categoria | None:
        categoria=self.__categoria.objects.create(nombre=nombre)
        return categoria

    def actualizar_categoria(self, id_categoria, nombre) -> Categoria | None:
        categoria=self.__categoria.objects.filter(id=id_categoria).update(nombre)