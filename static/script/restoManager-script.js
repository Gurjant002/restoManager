function editarPlato(params) {
    var fila = document.getElementById(params);

    const spliteParam = params.split("-")

    var campoId = document.getElementById("campo-id-"+spliteParam[1])
    const campoNumPlato = document.getElementById("campo-num-"+spliteParam[1])
    const campoNombre = document.getElementById("campo-nombre-"+spliteParam[1])
    const campoDescripcion = document.getElementById("campo-descripcion-"+spliteParam[1])
    const campoCategoria = document.getElementById("campo-categoria-"+spliteParam[1])
    const campoEstado = document.getElementById("campo-estado-"+spliteParam[1])

    // Esta seccion hace desaparecer el boton de añadir y activar el de actualizar.
    const btnSave = document.getElementById("btn-submit")
    btnSave.style.display = "none"
    const btnUpdate = document.getElementById("btn-update_plate")
    btnUpdate.value = "update_plate_"+campoId.textContent
    btnUpdate.style.display = "block"

    // En esta seccion añadimos los datos de la tabla a las etiquetas Inputs para que luego el usuario pueda editarlas
    const inptNumPlato = document.getElementById("floatingNum")
    inptNumPlato.value = campoNumPlato.innerText

    const inptNombre = document.getElementById("floatingPlato")
    inptNombre.value = campoNombre.innerText
    
    const inptDescripcion = document.getElementById("floatingDescripcion")
    inptDescripcion.value = campoDescripcion.innerText

    const inptCategoria = document.getElementById("floatingCategoria")
    inptCategoria.value = campoCategoria.innerText
    
    const inptEstado = document.getElementById("floatingEstado")
    if (campoEstado.innerText === "Activado") {
        inptEstado.value = 1
    } else {
        inptEstado.value = 0
        
    }

    const titulo = document.getElementById("titulo-seccion-superior")
    titulo.innerText = "Actualizar plato: " + campoId.innerText

    // <input type="number" id="id-plato" required="false" name="id-plato" style="display: none;">
    const divInpts = document.getElementById("inptNumId")
    divInpts.innerHTML = "<input type='number' id='id-plato' required='false' name='id-plato'>"
    const inptId = document.getElementById("id-plato")
    inptId.style.display = 'none'
    inptId.value = campoId.innerText 

}

function editarBebida(params) {
    const campoId = document.getElementById("campo-id-"+params)
    const campoNombre = document.getElementById("campo-nombre-"+params)
    const campoDescripcion = document.getElementById("campo-descripcion-"+params)
    const campoAlcohol = document.getElementById("campo-alcohol-"+params)
    const campoEstado = document.getElementById("campo-estado-"+params)

    // Esta seccion hace desaparecer el boton de añadir y activar el de actualizar.
    const btnSave = document.getElementById("btn-submit")
    btnSave.style.display = "none"
    const btnUpdate = document.getElementById("btn_update_bebida")
    btnUpdate.value = "update_bebida_"+campoId.textContent
    btnUpdate.style.display = "block"

    // En esta seccion añadimos los datos de la tabla a las etiquetas Inputs para que luego el usuario pueda editarlas
    const inptNombre = document.getElementById("floatingBebida")
    inptNombre.value = campoNombre.innerText
    
    const inptEstado = document.getElementById("floatingEstado")
    if (campoEstado.innerText === "Activado")
        inptEstado.value = 1
    else
        inptEstado.value = 0
    
    const inptAlcohol = document.getElementById("floatingAlcohol")
    if (campoAlcohol.innerText === "Si")
        inptAlcohol.value = 1
    else
        inptAlcohol.value = 0
    
    const inptDescripcion = document.getElementById("floatingDescripcion")
    inptDescripcion.value = campoDescripcion.innerText

    // Esta seccion cambia el titulo a Actualizar bebida...
    const titulo = document.getElementById("titulo-seccion-superior")
    titulo.innerText = "Actualizar bebida: #" + campoId.innerText
}

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


function goHome() {
    window.location = '/'
}

const url = window.location.pathname
if (url == '/config/platos/' ) {
    columna = document.querySelectorAll('.col-num')
    newNum = parseInt(columna[columna.length - 1].textContent)
    inputNum = document.querySelector('#floatingNum')
    inputNum.value = 1+newNum
}

if (url == '/config/ubicaciones/') {
    let timer = setInterval(function(time) {
        document.getElementById('error-msg').style.display = 'none';
    }, 10000);
}

document.addEventListener('DOMContentLoaded', function() {
    const footer = document.querySelectorAll('.eliminar-on-teclado');
    function adjustFooter() {
        const viewportHeight = window.visualViewport.height;
        const windowHeight = window.innerHeight;
        

        for (let i = 0; i < footer.length; i++) {
            if (windowHeight < 400) { // Ajuste para el tamaño de la barra de navegación
                // El teclado está abierto
                footer[i].style.display = 'none';
            } else {
                // El teclado está cerrado
                footer[i].style.display = 'block';
            }

        }
    }

    if (window.visualViewport) {
        window.visualViewport.addEventListener('resize', adjustFooter);
    } else {
        // Fallback para navegadores sin visualViewport API
        window.addEventListener('resize', adjustFooter);
    }
});

document.addEventListener('htmx:afterRequest', function (event) {
    // Verifica si la solicitud HTMX fue a la vista 'pedidos'
    // if (event.detail.xhr.responseURL === "/puestos/cocina/pedidos") {
        // Obtiene los datos de la respuesta JSON
        var datos = JSON.parse(event.detail.xhr.response);
        // Actualiza el contenido de la página con los datos recibidos
        var html = '';
        datos.pedidos_lista.forEach(function(pedido){
            html += `
            <div class="col-lg-3">
                <div class="card mb-3">
                    <div class="card-header bg-dark text-light">
                        Mesa #${pedido.mesa} [${pedido.mesa_ubicacion}]
                    </div>
                    <div class="card-body p-3">
                        <p class="card-text">Total pedidos: #${pedido.pedidosTotal}</p>
                        <p class="card-text">Hora: ${new Date(pedido.tiempo).toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})}</p>
                        <form class="text-center" action="/puestos/cocina/listar" method="GET">
                            <button type="submit" name="listar_mesa" value="${pedido.mesa_id}" class="btn btn-primary w-100 mt-2">Ver detalles</button>
                        </form>
                    </div>
                </div>
            </div>
            `;
        });
        document.getElementById('card-pedidos').innerHTML = html;
    /* } else if (event.detail.xhr.responseURL === "/puestos/cocina/cambiar-estado") {
        // Obtiene los datos de la respuesta JSON
        var datos = JSON.parse(event.detail.xhr.response);
        // Actualiza el contenido de la página con los datos recibidos
        var html = '';
        console.log(datos);
    } */
});