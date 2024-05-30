/**
 * Función para editar un plato en la tabla de platos.
 * @param {string} params - Parámetros de la fila del plato a editar.
 */
function editarPlato(params) {
    // Obtener la fila de la tabla correspondiente al plato a editar.
    var fila = document.getElementById(params);

    // Dividir los parámetros para obtener el número de plato.
    const spliteParam = params.split("-");

    // Obtener los campos de la fila del plato a editar.
    var campoId = document.getElementById("campo-id-"+spliteParam[1]);
    const campoNumPlato = document.getElementById("campo-num-"+spliteParam[1]);
    const campoNombre = document.getElementById("campo-nombre-"+spliteParam[1]);
    const campoDescripcion = document.getElementById("campo-descripcion-"+spliteParam[1]);
    const campoCategoria = document.getElementById("campo-categoria-"+spliteParam[1]);
    const campoEstado = document.getElementById("campo-estado-"+spliteParam[1]);

    // Ocultar el botón de guardar y mostrar el botón de actualizar.
    const btnSave = document.getElementById("btn-submit");
    btnSave.style.display = "none";
    const btnUpdate = document.getElementById("btn-update_plate");
    btnUpdate.value = "update_plate_"+campoId.textContent;
    btnUpdate.style.display = "block";

    // Añadir los datos de la tabla a las etiquetas de entrada para que el usuario los pueda editar.
    const inptNumPlato = document.getElementById("floatingNum");
    inptNumPlato.value = campoNumPlato.innerText;

    const inptNombre = document.getElementById("floatingPlato");
    inptNombre.value = campoNombre.innerText;
    
    const inptDescripcion = document.getElementById("floatingDescripcion");
    inptDescripcion.value = campoDescripcion.innerText;

    const inptCategoria = document.getElementById("floatingCategoria");
    inptCategoria.value = campoCategoria.innerText;
    
    const inptEstado = document.getElementById("floatingEstado");
    if (campoEstado.innerText === "Activado") {
        inptEstado.value = 1;
    } else {
        inptEstado.value = 0;
    }

    // Cambiar el título de la sección superior de la página.
    const titulo = document.getElementById("titulo-seccion-superior");
    titulo.innerText = "Actualizar plato: " + campoId.innerText;

    // Añadir un campo oculto con el ID del plato.
    const divInpts = document.getElementById("inptNumId");
    divInpts.innerHTML = "<input type='number' id='id-plato' required='false' name='id-plato'>";
    const inptId = document.getElementById("id-plato");
    inptId.style.display = 'none';
    inptId.value = campoId.innerText;
}

/**
 * Función para editar una bebida en la tabla de bebidas.
 * @param {string} params - Parámetros de la fila de la bebida a editar.
 */
function editarBebida(params) {
    // Obtener los campos de la fila de la bebida a editar.
    const campoId = document.getElementById("campo-id-"+params);
    const campoNombre = document.getElementById("campo-nombre-"+params);
    const campoDescripcion = document.getElementById("campo-descripcion-"+params);
    const campoAlcohol = document.getElementById("campo-alcohol-"+params);
    const campoEstado = document.getElementById("campo-estado-"+params);

    // Esta sección hace desaparecer el botón de añadir y activa el de actualizar.
    const btnSave = document.getElementById("btn-submit");
    btnSave.style.display = "none";
    const btnUpdate = document.getElementById("btn_update_bebida");
    btnUpdate.value = "update_bebida_"+campoId.textContent;
    btnUpdate.style.display = "block";

    // En esta sección se añaden los datos de la tabla a las etiquetas Inputs para que el usuario pueda editarlas.
    const inptNombre = document.getElementById("floatingBebida");
    inptNombre.value = campoNombre.innerText;
    
    const inptEstado = document.getElementById("floatingEstado");
    if (campoEstado.innerText === "Activado") {
        inptEstado.value = 1;
    } else {
        inptEstado.value = 0;
    }
    
    const inptAlcohol = document.getElementById("floatingAlcohol");
    if (campoAlcohol.innerText === "Si") {
        inptAlcohol.value = 1;
    } else {
        inptAlcohol.value = 0;
    }
    
    const inptDescripcion = document.getElementById("floatingDescripcion");
    inptDescripcion.value = campoDescripcion.innerText;

    // Esta sección cambia el título a "Actualizar bebida: #".
    const titulo = document.getElementById("titulo-seccion-superior");
    titulo.innerText = "Actualizar bebida: #" + campoId.innerText;
}


/**
 * Función para editar una categoría en la tabla de categorías.
 * @param {string} params - Parámetros de la fila de la categoría a editar.
 */
function editarCategoria(params) {
    const campoId = document.getElementById("campo-id-"+params)
    const campoNombre = document.getElementById("campo-nombre-"+params)

    const inptNombre = document.getElementById("floatingCategoria")
    inptNombre.value = campoNombre.innerText

    const btnSave = document.getElementById("btn-submit")
    btnSave.style.display = "none"
    const btnUpdate = document.getElementById("btn_update_categoria")
    btnUpdate.value = "update_categoria_"+campoId.textContent
    btnUpdate.style.display = "block"
}

/**
 * Función para editar una ubicación en la tabla de ubicaciones.
 * @param {string} params - Parámetros de la fila de la ubicación a editar.
 */
function editarUbicacion(params) {
    const campoId = document.getElementById("campo-id-"+params)
    const campoNombre = document.getElementById("campo-lugar-"+params)

    const inptNombre = document.getElementById("floatingUbicacion")
    inptNombre.value = campoNombre.innerText

    const btnSave = document.getElementById("btn-submit")
    btnSave.style.display = "none"

    const btnUpdate = document.getElementById("btn_update_ubicacion")
    btnUpdate.value = params
    btnUpdate.style.display = "block"
}


/**
 * Función para volver a la página de inicio.
 */
function goHome() {
    window.location = '/'
}

/**
 * Esta función se ejecuta cuando se carga el documento HTML. Su objetivo es ajustar el footer de la página de configuración de platos y ubicaciones según el estado del teclado. Si el teclado está abierto, el footer se oculta; de lo contrario, se muestra. Además, se define un contador regresivo para la página de configuración de ubicaciones que se muestra en la página.
 */
document.addEventListener('DOMContentLoaded', function() {
    const footer = document.querySelectorAll('.eliminar-on-teclado'); // Selecciona todos los elementos con la clase 'eliminar-on-teclado' y los guarda en el array 'footer'.

    /**
     * Esta función ajusta el footer de la página según el estado del teclado. Si el teclado está abierto, el footer se oculta; de lo contrario, se muestra.
     */
    function adjustFooter() {
        const viewportHeight = window.visualViewport.height; // Obtiene la altura visual de la ventana del visual viewport.
        const windowHeight = window.innerHeight; // Obtiene la altura de la ventana.
        
        for (let i = 0; i < footer.length; i++) { // Recorre todos los elementos en el array 'footer'.
            if (windowHeight < 400) { // Ajuste para el tamaño de la barra de navegación
                // El teclado está abierto
                footer[i].style.display = 'none'; // Oculta el elemento.
            } else {
                // El teclado está cerrado
                footer[i].style.display = 'block'; // Muestra el elemento.
            }

        }
    }

    if (window.visualViewport) {
        window.visualViewport.addEventListener('resize', adjustFooter); // Escucha el evento de redimensionamiento del visual viewport y llama a la función 'adjustFooter' cuando ocurre.
    } else {
        // Fallback para navegadores sin visualViewport API
        window.addEventListener('resize', adjustFooter); // Escucha el evento de redimensionamiento de la ventana y llama a la función 'adjustFooter' cuando ocurre.
    }

    const url = window.location.pathname; // Obtiene la URL actual.
    if (url == '/config/platos/') { // Si la URL es la de la página de configuración de platos.
        columna = document.querySelectorAll('.col-num'); // Selecciona todos los elementos con la clase 'col-num' y los guarda en el array 'columna'.
        newNum = parseInt(columna[columna.length - 1].textContent); // Convierte el texto del último elemento en un número y lo guarda en la variable 'newNum'.
        inputNum = document.querySelector('#floatingNum'); // Selecciona el elemento con el id 'floatingNum' y lo guarda en la variable 'inputNum'.
        inputNum.value = 1+newNum; // Aumenta el valor del número en 1 y lo asigna al elemento 'inputNum'.
    } else if (url == '/config/ubicaciones/') { // Si la URL es la de la página de configuración de ubicaciones.
        let countdown = 10; // Define una variable 'countdown' con un valor de 10.
        const cuentaAtras = document.getElementById('cuenta-atras'); // Selecciona el elemento con el id 'cuenta-atras' y lo guarda en la variable 'cuentaAtras'.
        const timer = setInterval(() => { // Crea un intervalo de tiempo que se ejecuta cada segundo.
            if (countdown > 0) { // Si el contador es mayor que 0.
                cuentaAtras.textContent = countdown.toString().padStart(1, '0'); // Convierte el número en una cadena de texto con un espacio en blanco antes de los números menores a 10 y lo asigna al texto del elemento 'cuentaAtras'.
                countdown--; // Reduce el valor del contador en 1.
            } else { // Si el contador es igual a 0.
                clearInterval(timer); // Detiene el intervalo de tiempo.
                cuentaAtras.textContent = '00'; // Asigna el valor '00' al texto del elemento 'cuentaAtras'.
            }
        }, 1000); // Especifica que el intervalo de tiempo debe ejecutarse cada segundo.

        setInterval(function(time) {
            document.getElementById('error-msg').style.display = 'none'; // Oculta el elemento con el id 'error-msg' después de 11 segundos.
        }, 11000); // Especifica que la función se debe ejecutar cada 11 segundos.
    }
});

