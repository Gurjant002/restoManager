class Persona:
    nombre: str
    
    def __init__(self):
        self.nombre='Gurjant Singh'

    def getNombre(self) -> str:
        return self.nombre