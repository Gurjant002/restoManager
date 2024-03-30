function editarFila(params) {
    var fila = document.getElementById(params);

    const spliteParam = params.split("-")

    /**
     * TODO:
     * 1.- Inicializar variables para cada uno de los campos que hay... CHECK 💚
     * 2.- Una vez guardado todos los valores de cada campo, eliminar la fila de la lista. CHECK 💚
     * 3.- Se modificara el boton con la id 'btn-submit, en el atributo value se pondra: 'update_plate' y el texto del btn a 'Actualizar Plato' CHECK 💚
     * 4.- Los datos guardados se mostraran en los campos de la parte superior del navegador,
     * donde se editaran y se enviaran con el metodo post al servidor para que lo actualize en la base de datos. CHECK 💚
     * 
     */

    var campoId = document.getElementById("campo-id-"+spliteParam[1])
    const campoNumPlato = document.getElementById("campo-num-"+spliteParam[1])
    const campoNombre = document.getElementById("campo-nombre-"+spliteParam[1])
    const campoDescripcion = document.getElementById("campo-descripcion-"+spliteParam[1])
    const campoCategoria = document.getElementById("campo-categoria-"+spliteParam[1])
    const campoEstado = document.getElementById("campo-estado-"+spliteParam[1])
/* 
    var hijos = fila.children
    for(var i = hijos.length-1; i >= 0; i--) {
        var hijo = hijos[i];
        hijo.parentNode.removeChild(hijo)
    }
 */

    // Esta seccion hace desaparecer el boton de añadir y activar el de actualizar.
    const btnSave = document.getElementById("btn-submit")
    btnSave.style.display = "none"
    const btnUpdate = document.getElementById("btn-update_plate")
    btnUpdate.style.display = "block"

    // En esta seccion añadimos los datos de la tabla a las etiquetas Inputs para que luego el usuario pueda editarlas.
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

columna = document.querySelectorAll('.col-num')

// for (var i = 0; i < columna.length; i++)
//     newNum = parseInt(columna[i].textContent)

newNum = parseInt(columna[columna.length - 1].textContent)

inputNum = document.querySelector('#floatingNum')
inputNum.value = 1+newNum