document.addEventListener("DOMContentLoaded", () => {
    const productos = document.querySelectorAll(".producto");

    productos.forEach(contenedor => {
        contenedor.style.cursor = "pointer";

        contenedor.addEventListener("click", () => {
            const enlace = contenedor.querySelector("a");
            
            if (enlace) {
                window.location.href = enlace.href;
            }
        });
    });
});