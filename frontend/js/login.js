const API_URL = "http://127.0.0.1:8000";

const formulario = document.getElementById("login-form");
const botonLogin = document.getElementById("login-button");
const mensaje = document.getElementById("login-message");


formulario.addEventListener("submit", async (evento) => {

    evento.preventDefault();

    const usuario = document.getElementById("usuario").value.trim();
    const contrasena = document.getElementById("contrasena").value;


    mensaje.textContent = "";
    botonLogin.disabled = true;
    botonLogin.textContent = "Iniciando sesión...";


    try {

        const respuesta = await fetch(`${API_URL}/api/login`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                usuario: usuario,
                contrasena: contrasena
            })

        });


        const datos = await respuesta.json();


        if (!respuesta.ok || !datos.exito) {

            mensaje.textContent =
                datos.mensaje || "Usuario o contraseña incorrectos.";

            return;
        }


        // Guardamos los datos del usuario
        localStorage.setItem(
            "usuario",
            JSON.stringify(datos.usuario)
        );


        // Redirigir al dashboard
        window.location.href = "dashboard.html";


    } catch (error) {

        console.error("Error de conexión:", error);

        mensaje.textContent =
            "No se pudo conectar con el servidor.";


    } finally {

        botonLogin.disabled = false;
        botonLogin.textContent = "Iniciar sesión";

    }

});