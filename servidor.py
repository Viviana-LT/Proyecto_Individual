from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import mysql.connector

# Configuración de la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='ds00videojueg0-',
        database='flodilac_db'
    )

class FlodilacHandler(BaseHTTPRequestHandler):

    # 1. SERVIR LOS ARCHIVOS (GET)
    def do_GET(self):
        if self.path == '/' or self.path == '/login.html':
            self.servir_archivo('login.html', 'text/html')
        elif self.path == '/registro.html':
            self.servir_archivo('registro.html', 'text/html')
        elif self.path.endswith('.css'):
            self.servir_archivo(self.path[1:], 'text/css')
        elif self.path.endswith('.js'):
            self.servir_archivo(self.path[1:], 'text/js')
        elif self.path.endswith('.html'):
            self.servir_archivo(self.path[1:], 'text/html')
        elif self.path.endswith('.png') or self.path.endswith('.jpg'):
            self.servir_archivo(self.path[1:], 'image/png')
        else:
            self.send_error(404, "Archivo no encontrado")

    def servir_archivo(self, nombre, tipo):
        try:
            with open(nombre, 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', tipo)
                self.end_headers()
                self.wfile.write(file.read())
        except:
            self.send_error(404)

    # 2. PROCESAR FORMULARIOS (POST)
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        datos = urllib.parse.parse_qs(post_data)

        if self.path == '/registro':
            self.handle_registro(datos)
        elif self.path == '/login':
            self.handle_login(datos)

    def handle_registro(self, datos):
        nombre = datos.get('nombre_usuario')[0]
        correo = datos.get('correo')[0]
        password = datos.get('password')[0]

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (nombre_usuario, correo, password) VALUES (%s, %s, %s)", 
                           (nombre, correo, password))
            conn.commit()
            self.responder_exito("Registro exitoso. Ya puedes iniciar sesión.")
        except Exception as e:
            self.responder_error(f"Error al registrar: {e}")
        finally:
            conn.close()

    def handle_login(self, datos):
        correo = datos.get('correo')[0]
        password = datos.get('password')[0]

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE correo = %s AND password = %s", (correo, password))
            user = cursor.fetchone()

            if user:
                # ÉXITO: Redirigir a la página principal de productos
                self.send_response(303) # Código de redirección
                self.send_header('Location', '/dashboard.html')
                self.end_headers()
            else:
                self.responder_error("Correo o contraseña incorrectos.")
        except Exception as e:
            self.responder_error(f"Error en el servidor: {e}")
        finally:
            conn.close()

    def responder_exito(self, mensaje):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(f"<h1>{mensaje}</h1><a href='/login.html'>Volver</a>".encode('utf-8'))

    def responder_error(self, mensaje):
        self.send_response(401)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(f"<h1>Error</h1><p>{mensaje}</p><a href='/login.html'>Reintentar</a>".encode('utf-8'))

# Iniciar el servidor
puerto = 8000
print(f"Servidor Flodilac corriendo en http://localhost:{puerto}")
server = HTTPServer(('localhost', puerto), FlodilacHandler)
server.serve_forever()