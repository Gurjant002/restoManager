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

    // console.log(campoEstado.innerText);
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

function addMesas() {
    const mesaNueva = document.querySelectorAll("#mesa-nueva")
    mesaNueva.forEach(element => {
        element.classList.toggle("d-none");
        element.classList.toggle("d-block");
    });
}

function goHome() {
    window.location = '/'
}

function seleccionarMesa(id, numMesa, ubicacion) {
    const mesa = document.querySelector("#mesa-seleccionada")
    mesa.innerText = `#${numMesa}: ${ubicacion}`
    mesa.insertAdjacentHTML('beforeend', `<input type="hidden" name="mesa" value="${id}">`);
}

const url = window.location.pathname
if (url == '/config/platos/' ) {
    columna = document.querySelectorAll('.col-num')
    newNum = parseInt(columna[columna.length - 1].textContent)
    inputNum = document.querySelector('#floatingNum')
    inputNum.value = 1+newNum
}

if (url != '/puestos/camarero/' ) {
    let timer = setInterval(function(time) {
        document.getElementById('error-msg').style.display = 'none';
    }, 10000);
}

document.addEventListener('DOMContentLoaded', function() {
    const resizer = document.getElementById('resizer');
    const panel = document.getElementById('resizable-panel');
    console.log(`resizer: ${resizer}, panel: ${panel}`);
    let isResizing = false;

    resizer.addEventListener('touchstart', function(e) {
        isResizing = true;
        document.addEventListener('touchmove', onTouchMove);
        document.addEventListener('touchend', onTouchEnd);
    });

    function onTouchMove(e) {
        if (!isResizing) return;
        let newHeight = panel.getBoundingClientRect().bottom - e.touches[0].clientY;
        if (newHeight > 50) { // Minimum height to prevent it from being too small
            panel.style.height = newHeight + 'px';
        }
    }

    function onTouchEnd(e) {
        isResizing = false;
        document.removeEventListener('touchmove', onTouchMove);
        document.removeEventListener('touchend', onTouchEnd);
    }
});


