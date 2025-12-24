import mysql.connector
from mysql.connector import Error

def crear_base_de_datos():
    try:
        # Conexión inicial al servidor (sin especificar base de datos)
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='ds00videojueg0-'
        )
        
        if conexion.is_connected():
            cursor = conexion.cursor()
            
            cursor.execute("CREATE DATABASE IF NOT EXISTS flodilac_db")
            print("Base de datos 'flodilac_db' verificada/creada.")
            
            cursor.execute("USE flodilac_db")
            
            tabla_usuarios = """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre_usuario VARCHAR(50) NOT NULL UNIQUE,
                correo VARCHAR(100) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
            cursor.execute(tabla_usuarios)
            print("Tabla 'usuarios' verificada/creada correctamente.")

    except Error as e:
        print(f"Error al crear la base de datos: {e}")
        print("Asegúrate de que XAMPP/WAMP esté encendido y MySQL esté en verde.")
        
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("🔌 Conexión cerrada.")

if __name__ == "__main__":
    crear_base_de_datos()