# RestoManager (Proyecto Final de Curso)
**En Desarrollo**

RestoManager es una plataforma web diseñada para simplificar y optimizar la gestión de restaurantes. Con características intuitivas y poderosas, RestoManager permite a los propietarios y gerentes de restaurantes coordinar eficientemente las operaciones diarias, desde la gestión de mesas hasta la administración de pedidos y el seguimiento del inventario.

## Guia de instalacion (S.O Windows)
### Prerrequisitos
 - Python 3.12 o superior
 - Mysql 8.0 o superior
 - Git

### Configurar la Mysql

1. Tener MySQL Workbench funcionando

2. Crear una base de datos:

````bash
CREATE DATABASE restoManager;
````

### Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/gurjant-singh/restoManager.git
```

2. Navegar al directorio del proyecto:

```bash
cd restoManager
```

3. Crear un archivo de entorno:

```bash
cp python -m venv nombre_venv
```

Ahora activarlo:

```bash
.\nombre_venv\Scripts\activate
```

4. Editar el archivo de entorno con la información de la base de datos.

5. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

6. Inicializar la base de datos:

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

7. Iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

## Uso

Acceder a la plataforma web en http://localhost:8000. Al intentar acceder algun apartado o inicar sesion
le redrigira a una pagina de registro, esto solo ocurre una vez al iniciar el proyecto.

## Acceso a otros dispositivos

Para dar acceso a los demas usuarios tendras que acceder a:

```
 restoManager > settings.pty
```

Modifica el siguiente lista:
ALLOWED_HOSTS = ['TU.IP.DE.TU.PC']

Debes tener encuenta que si tu red tiene un servidor DHCP se te puede cambiar la ip de tu pc,
por tanto asegurate de tener una IP fija

## Contribuciones

Las contribuciones son bienvenidas. Para obtener más información sobre cómo contribuir, consulte la guía de contribución:

https://github.com/gurjant-singh/restoManager/blob/main/CONTRIBUTING.md

## Licencia

RestoManager se distribuye bajo la licencia MIT. Para obtener más información, consulte el archivo LICENSE.


## Features

- Administrar mesas y pedidos: crear, editar y eliminar mesas y pedidos de manera sencilla y rápida.
- Gestionar menú: crear, editar y eliminar platos de manera fácil y rápida, y actualizar el precio y el estado de los mismos de manera sencilla.
- Multi-restaurante: RestoManager permite almacenar datos de múltiples restaurantes y visualizarlos de manera separada.
- Responsive: el diseño de la plataforma es compatible con dispositivos móviles y tabletas.
- Configuración personalizable: los gerentes de restaurantes pueden personalizar el diseño y comportamiento de la plataforma para adaptarse a sus necesidades específicas.
- Les facilita a los camareros atender mesas.
- Los cocinero y barra pueden visualizar las tareas pendientes de forma mas comoda y detallada.

Autor del projecto: **Gurjant Singh**
