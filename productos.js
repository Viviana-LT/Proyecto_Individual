const modal = document.getElementById("modalPrecio");
const closeBtn = document.querySelector(".close-btn");

// Datos de ejemplo por categoría
const precios = {
    "YOGURT": `<tr><td>Personal</td><td>250ml</td><td>S/ 3.50</td></tr>
               <tr><td>Familiar</td><td>1L</td><td>S/ 11.00</td></tr>`,
    "MANTEQUILLA": `<tr><td>Barra</td><td>200g</td><td>S/ 8.50</td></tr>`,
    "MANJAR": `<tr><td>Pote</td><td>250g</td><td>S/ 7.00</td></tr>
               <tr><td>Pote Grande</td><td>500g</td><td>S/ 13.00</td></tr>`,
    "QUESO": `<tr><td>Grande</td><td>700g</td><td>S/ 12.00</td></tr>
               <tr><td>Pequeño</td><td>400g</td><td>S/ 8.00</td></tr>`
};

// Asignar evento a cada tarjeta de producto
document.querySelectorAll('.product-card').forEach(card => {
    card.style.cursor = "pointer";
    card.addEventListener('click', () => {
        const nombre = card.querySelector('h3').innerText;
        document.getElementById("modalTitle").innerText = nombre;
        
        // Buscamos si es yogurt, manjar o mantequilla para poner su precio
        if(nombre.includes("YOGURT")) {
            document.getElementById("modalTableBody").innerHTML = precios["YOGURT"];
        } else if(nombre.includes("MANTEQUILLA")) {
            document.getElementById("modalTableBody").innerHTML = precios["MANTEQUILLA"];
        } else if(nombre.includes("MANJAR")) {
            document.getElementById("modalTableBody").innerHTML = precios["MANJAR"];
        } else {
            document.getElementById("modalTableBody").innerHTML = precios["QUESO"];
        }
        
        modal.style.display = "block";
    });
});

// Cerrar modal
closeBtn.onclick = () => modal.style.display = "none";
window.onclick = (event) => { if (event.target == modal) modal.style.display = "none"; }