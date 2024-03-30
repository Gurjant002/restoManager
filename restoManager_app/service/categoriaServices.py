from restoManager_app.models import Categoria, Plato_Categoria

class CategoriaService:
    
    def get_categoria_by_name(nombre_categoria):
        categoria=Categoria.objects.filter(nombre_categoria).first

    def crear_categoria(nombre: str):
        categoria=Categoria.objects.create(nombre=nombre)
        return categoria