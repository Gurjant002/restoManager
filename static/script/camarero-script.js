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
    const datosOcultosID = document.querySelector("#input-mesa-id")
    mesaSeleccionada.forEach(element => {
        element.innerText = `#${numeroMesa}: ${lugar}, ${camarero}`
        element.value = id
        datosOcultosID.value = id
        element.tagName = 'mesa-seleccionada'
    });

}
/* 
function selectPlato(id, numPlato, nombre, categoria) {
    const platoSeleccionado = document.querySelector("#plato-seleccionado")
    platoSeleccionado.innerText = `#${numPlato}: ${nombre}, ${categoria}`
    platoSeleccionado.value = id
    platoSeleccionado.tagName = 'plato-seleccionado'
    
} */

function seleccionarProducto(producto, idProducto, nombreProdcuto, categoria) {
    const contenedorProducto = document.querySelector(`#lista-${producto}`);
    const productosList = contenedorProducto.querySelector(`#${producto}-${idProducto}`);
    
    if (!productosList) {
        const newProduct = document.createElement('fieldset');
        const newItem = document.createElement('li');
        const product = document.createElement('div');
        const inputName = document.createElement('input');
        const quantity = document.createElement('div');
        const addButton = document.createElement('button');
        const subButton = document.createElement('button');
        const deleteButton = document.createElement('button');
        const amountInput = document.createElement('input');
        
        newProduct.className = 'my-1';
        newItem.className = 'list-group-item rounded d-flex justify-content-between align-items-center';
        newItem.id = `${producto}-${idProducto}`;
        product.className = 'd-flex justify-content-between align-items-center rounded text-break text-dark';
        product.id = 'producto';
        inputName.type = 'hidden';
        inputName.name = producto;
        inputName.value = idProducto;
        quantity.className = 'd-flex justify-content-between align-items-center';
        addButton.type = 'button';
        addButton.className = 'btn btn-outline-success';
        addButton.textContent = '+';
        addButton.addEventListener('click', () => {
            cantidad(idProducto, producto, 'add');
        });
        subButton.type = 'button';
        subButton.className = 'btn btn-outline-danger';
        subButton.textContent = '-';
        subButton.addEventListener('click', () => {
            cantidad(idProducto, producto, 'sub');
        });
        deleteButton.type = 'button';
        deleteButton.className = 'btn btn-outline-danger';
        deleteButton.innerHTML = '<i class="bi bi-trash"></i>';
        deleteButton.addEventListener('click', () => {
            eliminarProducto(idProducto, producto);
        });
        amountInput.type = 'number';
        amountInput.className = 'form-control';
        amountInput.name = `cantidad-${producto}-${idProducto}`;
        amountInput.id = `cantidad-${producto}-${idProducto}`;
        amountInput.value = 1;
        amountInput.min = 1;
        amountInput.style.width = '50px';
        
        product.appendChild(document.createTextNode(`${nombreProdcuto}, ${categoria}`));
        quantity.appendChild(amountInput);
        quantity.appendChild(addButton);
        quantity.appendChild(subButton);
        quantity.appendChild(deleteButton);
        newItem.appendChild(product);
        newItem.appendChild(inputName);
        newItem.appendChild(quantity);
        newProduct.appendChild(newItem);
        
        contenedorProducto.appendChild(newProduct);
    }
    
}

function eliminarProducto(id, seccion) {
    const plato = document.querySelector(`#${seccion}-${id}`)
    plato.remove()
}

function filterPlato(categoria) {
    const rows = document.querySelectorAll("#tabla-platos")
    rows.forEach(element => {
        console.log(element.id);
    });
}

function cantidad(id, seccion, op) {
    const contador = document.querySelector(`#cantidad-${seccion}-${id}`)
    if (op === 'add') {
        contador.value = parseInt(contador.value) + 1
    }else {
        console.log(parseInt(contador.value));
        if (parseInt(contador.value) > 0) {
            contador.value = parseInt(contador.value) - 1
        }
    }
    
}

document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#formulario").addEventListener('submit', function(event) {
        const mesa = document.querySelector("#input-mesa-id")
        if (mesa.value === "") {
            alert("Debe seleccionar una mesa")
            event.preventDefault();
        }
    });
});

function toggleNotas(display) {
    const notas = document.getElementById('notas');
    notas.style.display = display ;
}
