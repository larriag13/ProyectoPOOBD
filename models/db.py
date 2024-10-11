import mysql.connector
from mysql.connector import Error
#pip install mysql-connector-python, debe instalar este paquete para poder importar la librería mysql.connector
def conectar():
    try:#Intentamos conectar a la base de datos
        conn = mysql.connector.connect(#Conectamos a la base de datos
            host='localhost',#Nombre del host, en este caso localhost
            database='bdpooejemplo',#Nombre de la base de datos, en este caso bdpooejemplo
            user='root',#Usuario, en este caso root
            password=''#Contraseña, en este caso no tiene   
        )
        return conn
    except Error as e:#Si hay un error al conectar a la base de datos, se imprime un mensaje
        print(f"Error al conectar a MariaDB: {e}")
        return None

def crear_tablas():#Función para crear las tablas en la base de datos
    conn = conectar()
    if conn is None:
        return

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            edad INT NOT NULL,
            carrera VARCHAR(255) NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS profesores (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            edad INT NOT NULL,
            materia VARCHAR(255) NOT NULL
        )
    ''')

    conn.commit()
    cursor.close()
    conn.close()