const API_URL = "http://127.0.0.1:8000";


// ======================================
// CARGAR MESAS
// ======================================

async function cargarMesas() {

    try {

        const respuesta = await fetch(`${API_URL}/mesas`);

        const mesas = await respuesta.json();

        const contenedor = document.getElementById("mesas-container");

        contenedor.innerHTML = "";

        let libres = 0;
        let ocupadas = 0;

        mesas.forEach(mesa => {

            const estado = mesa.estado.toLowerCase();

            if (estado === "libre") {
                libres++;
            } else {
                ocupadas++;
            }

            const tarjeta = document.createElement("div");

            tarjeta.classList.add("mesa-card");

            if (estado === "libre") {
                tarjeta.classList.add("mesa-libre");
            } else {
                tarjeta.classList.add("mesa-ocupada");
            }

            tarjeta.innerHTML = `
                <div class="mesa-numero">
                    🪑 Mesa ${mesa.numero}
                </div>

                <span class="mesa-estado">
                    ${mesa.estado.toUpperCase()}
                </span>
            `;

            tarjeta.onclick = () => seleccionarMesa(mesa);

            contenedor.appendChild(tarjeta);

        });


        document.getElementById("total-mesas").textContent = mesas.length;

        document.getElementById("mesas-libres").textContent = libres;

        document.getElementById("mesas-ocupadas").textContent = ocupadas;

    } catch (error) {

        console.error("Error cargando mesas:", error);

        document.getElementById("mesas-container").innerHTML = `
            <p>No se pudieron cargar las mesas.</p>
        `;
    }
}



// ======================================
// CARGAR PRODUCTOS
// ======================================

async function cargarProductos() {

    try {

        const respuesta = await fetch(`${API_URL}/platos`);

        const productos = await respuesta.json();

        const contenedor = document.getElementById("productos-container");

        contenedor.innerHTML = "";

        productos.forEach(producto => {

            const tarjeta = document.createElement("div");

            tarjeta.classList.add("producto-card");

            tarjeta.innerHTML = `
                <div class="producto-nombre">
                    🍔 ${producto.nombre}
                </div>

                <div class="producto-categoria">
                    ${producto.categoria || "Sin categoría"}
                </div>

                <div class="producto-precio">
                    $${Number(producto.precio).toLocaleString("es-CO")}
                </div>
            `;

            contenedor.appendChild(tarjeta);

        });


        document.getElementById("total-productos").textContent =
            productos.length;

    } catch (error) {

        console.error("Error cargando productos:", error);

        document.getElementById("productos-container").innerHTML = `
            <p>No se pudieron cargar los productos.</p>
        `;
    }
}



// ======================================
// SELECCIONAR MESA
// ======================================

function seleccionarMesa(mesa) {

    console.log("Mesa seleccionada:", mesa);

    alert(
        `Mesa ${mesa.numero}\nEstado: ${mesa.estado}`
    );
}



// ======================================
// INICIAR SISTEMA
// ======================================

document.addEventListener("DOMContentLoaded", () => {

    cargarMesas();

    cargarProductos();

});