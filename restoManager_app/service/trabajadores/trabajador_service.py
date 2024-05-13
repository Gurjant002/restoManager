from django.contrib.auth.models import User

class TrabajadorService:
    _trabajadores: User

    def __init__(self):
        self._trabajadores = User()

    def crear_trabajador(self, usuario: str, nombre: str, apellido: str, email: str, password: str):
        self._trabajadores = User.objects.create_user(password=password, email=email, first_name=nombre, last_name=apellido, username=usuario)
        return self._trabajadores

    def get_trabajadores(self) -> User:
        return User.objects.all()