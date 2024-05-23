
function addMesas() {
    const mesaNueva = document.querySelectorAll("#mesa-nueva")
    mesaNueva.forEach(element => {
        element.classList.toggle("d-none");
        element.classList.toggle("d-block");
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const resizer = document.getElementById('resizer');
    const panel = document.getElementById('resizable-panel');
    let isResizing = false;
    let initialHeight = 0;
    let startY = 0;
    const resizerHeight = 7.5;
    resizer.style.height = resizerHeight+'px';

    resizer.addEventListener('touchstart', function(e) {
        isResizing = true;
        initialHeight = panel.getBoundingClientRect().height;
        startY = e.touches[0].clientY;
        resizer.style.height = resizerHeight+'px';
        document.addEventListener('touchmove', onTouchMove);
        document.addEventListener('touchend', onTouchEnd);
    });

    function onTouchMove(e) {
        if (!isResizing) return;
        let currentY = e.touches[0].clientY;
        let newHeight = initialHeight + (startY - currentY); // Cambiar la lógica
        if (newHeight > 50 && newHeight < 625) {
            panel.style.height = newHeight + 'px';
            resizer.style.height = resizerHeight+'px';
        }
    }

    function onTouchEnd(e) {
        isResizing = false;
        document.removeEventListener('touchmove', onTouchMove);
        document.removeEventListener('touchend', onTouchEnd);
        resizer.style.height = resizerHeight+'px';
    }
});

function selectMesa(id, numeroMesa, lugar, camarero) {
    const mesaSeleccionada = document.querySelectorAll("#mesa-seleccionada")
    mesaSeleccionada.forEach(element => {
        element.innerText = `#${numeroMesa}: ${lugar}, ${camarero}`
        element.value = id
        element.tagName = 'mesa-seleccionada'
    });
}

function selectPlato(id, numPlato, nombre, categoria) {
    const platoSeleccionado = document.querySelector("#plato-seleccionado")
    platoSeleccionado.innerText = `#${numPlato}: ${nombre}, ${categoria}`
    platoSeleccionado.value = id
    platoSeleccionado.tagName = 'plato-seleccionado'
    
}

function filterPlato(categoria) {
    const rows = document.querySelectorAll("#tabla-platos")
    rows.forEach(element => {
        console.log(element.id);
    });
}