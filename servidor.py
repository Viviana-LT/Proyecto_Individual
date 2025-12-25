from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import mysql.connector
import os

app = Flask(__name__, template_folder='.')

# Configuración de base de datos
def get_db_connection():
    return mysql.connector.connect(
        host='Viviana667.mysql.pythonanywhere-services.com',
        user='Viviana667',
        password='_3LT58UDFwhwP9Y',
        database='Viviana667$flodilac_db'
    )

# --- RUTAS PARA PÁGINAS HTML ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login.html')
def login_page():
    return render_template('login.html')

@app.route('/registro.html')
def registro_page():
    return render_template('registro.html')

@app.route('/productos.html')
def productos_page():
    return render_template('productos.html')

@app.route('/contacto.html')
def contacto_page():
    return render_template('contacto.html')

@app.route('/dashboard.html')
def dashboard_page():
    return render_template('dashboard.html')

# Agrega rutas para las categorías si las necesitas por separado
@app.route('/yogurt.html')
def yogurt_page(): return render_template('yogurt.html')

@app.route('/mantequilla.html')
def mantequilla_page(): return render_template('mantequilla.html')

@app.route('/manjar.html')
def manjar_page(): return render_template('manjar.html')

@app.route('/queso.html')
def queso_page(): return render_template('queso.html')

# --- LÓGICA DE FORMULARIOS ---
@app.route('/login', methods=['POST'])
def handle_login():
    correo = request.form.get('correo')
    password = request.form.get('contra')
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s AND password = %s", (correo, password))
        user = cursor.fetchone()
        if user:
            return redirect(url_for('dashboard_page'))
        return "<h1>Error</h1><p>Credenciales incorrectas</p><a href='/login.html'>Volver</a>"
    except Exception as e:
        return f"<h1>Error de Conexión</h1><p>{e}</p>"
    finally:
        if conn:
            conn.close()

@app.route('/registro', methods=['POST'])
def handle_registro():
    nombre = request.form.get('nombre_usuario')
    correo = request.form.get('correo')
    password = request.form.get('password')
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre_usuario, correo, password) VALUES (%s, %s, %s)",
                       (nombre, correo, password))
        conn.commit()
        return redirect(url_for('login_page'))
    except Exception as e:
        return f"<h1>Error al registrar</h1><p>{e}</p>"
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(port=8000, debug=True)