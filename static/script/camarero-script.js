/**
 * Alterna la visibilidad de la sección de creación de mesas.
 */
function addMesas() {
    const mesaNueva = document.querySelectorAll("#mesa-nueva")
    mesaNueva.forEach(element => {
        element.classList.toggle("d-none");
        element.classList.toggle("d-block");
    });
}

/**
 * Evento que se dispara cuando se carga el DOM. Agrega eventos a los elementos de la interfaz de usuario.
 */
document.addEventListener('DOMContentLoaded', function() {
    const resizer = document.getElementById('resizer');
    const panel = document.getElementById('resizable-panel');
    let isResizing = false;
    let initialHeight = 0;
    let startY = 0;
    const resizerHeight = 7.5;
    resizer.style.height = resizerHeight+'px';

    /**
     * Evento de inicio de tácto. Inicia el proceso de redimensionamiento.
     * @param {Object} e - Objeto evento.
     */
    resizer.addEventListener('touchstart', function(e) {
        isResizing = true;
        initialHeight = panel.getBoundingClientRect().height;
        startY = e.touches[0].clientY;
        resizer.style.height = resizerHeight+'px';
        document.addEventListener('touchmove', onTouchMove);
        document.addEventListener('touchend', onTouchEnd);
    });

    /**
     * Evento de movimiento de tácto. Calcula la nueva altura del panel y la redimensiona.
     * @param {Object} e - Objeto evento.
     */
    function onTouchMove(e) {
        if (!isResizing) return;
        let currentY = e.touches[0].clientY;
        let newHeight = initialHeight + (startY - currentY); // Cambiar la lógica
        if (newHeight > 50 && newHeight < 625) {
            panel.style.height = newHeight + 'px';
            resizer.style.height = resizerHeight+'px';
        }
    }

    /**
     * Evento final de tácto. Finaliza el proceso de redimensionamiento.
     * @param {Object} e - Objeto evento.
     */
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

/**
 * Selecciona un producto y lo agrega a la lista de productos seleccionados.
 * @param {string} producto - Nombre de la sección de productos (bebidas o platos).
 * @param {number} idProducto - ID del producto seleccionado.
 * @param {string} nombreProdcuto - Nombre del producto seleccionado.
 * @param {string} categoria - Categoría del producto seleccionado.
 */
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

/**
 * Elimina un producto de la lista de productos seleccionados.
 * @param {string} id - ID del producto a eliminar.
 * @param {string} seccion - Sección de productos (bebidas o platos).
 */
function eliminarProducto(id, seccion) {
    const plato = document.querySelector(`#${seccion}-${id}`)
    plato.remove()
}

/**
 * Filtra los platos por categoría.
 * @param {string} categoria - Categoría de los platos a filtrar.
 */
function filterPlato(categoria) {
    const rows = document.querySelectorAll("#tabla-platos")
    rows.forEach(element => {
        console.log(element.id);
    });
}

/**
 * Modifica la cantidad de un producto seleccionado.
 * @param {string} id - ID del producto seleccionado.
 * @param {string} seccion - Sección de productos (bebidas o platos).
 * @param {string} op - Operación a realizar ('add' para aumentar o 'sub' para disminuir).
 */
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

/**
 * Agrega un evento de envío al formulario principal.
 */
document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#formulario").addEventListener('submit', function(event) {
        const mesa = document.querySelector("#input-mesa-id")
        const mesaNumero = document.querySelector("#mesa-seleccionada")
        if (!mesaNumero.value) {
            alert("Debe seleccionar una mesa")
            event.preventDefault();
        }
    });
});

/**
 * Muestra u oculta el campo de notas.
 * @param {string} display - El valor de la propiedad CSS "display" a aplicar.
 */
function toggleNotas(display) {
    const notas = document.getElementById('notas');
    notas.style.display = display ;
}

