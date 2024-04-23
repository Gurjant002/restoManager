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

columna = document.querySelectorAll('.col-num')

// for (var i = 0; i < columna.length; i++)
//     newNum = parseInt(columna[i].textContent)

newNum = parseInt(columna[columna.length - 1].textContent)

inputNum = document.querySelector('#floatingNum')
inputNum.value = 1+newNum