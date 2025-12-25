# 🥛 Flodilac - Productos Lácteos 100% Naturales

![Logo Flodilac](/resourses/LogoFD.png)

**Flodilac** es una plataforma web integral diseñada para la gestión y venta de productos lácteos frescos. Este proyecto combina una interfaz de usuario atractiva con un backend robusto capaz de gestionar registros de usuarios, inicios de sesión y visualización de catálogos de productos.

## 🚀 Características principales
* **Sistema de Autenticación:** Registro e inicio de sesión seguro conectado a una base de datos.
* **Catálogo Dinámico:** Separación de productos por categorías (Yogurt, Mantequilla, Manjar, Queso).
* **Interfaz Responsive:** Diseño adaptativo para dispositivos móviles y escritorio.
* **Panel de Usuario (Dashboard):** Área personalizada para clientes tras iniciar sesión.

## 🛠️ Tecnologías utilizadas

### Frontend:
* **HTML5:** Estructura de las páginas.
* **CSS3:** Diseño personalizado con estilos específicos para login, productos y contacto.
* **JavaScript:** Manejo de interacciones básicas en el lado del cliente.

### Backend:
* **Python (Flask):** Servidor web y gestión de rutas dinámicas.
* **MySQL:** Base de datos relacional para el almacenamiento de usuarios.
* **PythonAnywhere:** Hosting en la nube para el despliegue del proyecto.

## 📁 Estructura del Proyecto

```text
/
├── resourses/          # Imágenes y logotipos de la empresa
├── servidor.py         # Archivo principal de la lógica en Flask
├── crearBD.py          # Script de automatización para la base de datos
├── index.html          # Página principal (Nosotros)
├── login.html          # Formulario de acceso
├── registro.html       # Registro de nuevos clientes
├── dashboard.html      # Panel principal post-login
├── productos.html      # Catálogo general
├── *.css               # Archivos de estilos (styles, contacto, login, etc.)
└── README.md           # Documentación del proyecto
