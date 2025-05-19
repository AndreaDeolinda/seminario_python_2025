import mysql.connector
from mysql.connector import Error

def conectar_mysql():
    try:
        conexion = mysql.connector.connect(
            host="localhost", # Cambia esto si tu servidor no está en localhost
            user="Andrea_Deolinda",     # Cambia por tu usuario de MySQL
            password="unida123", # Cambia por tu contraseña
            database="jaguarete", # Cambia por el nombre de tu base de datos
            port=3306
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            cursor = conexion.cursor()
            # Aquí puedes hacer tus consultas
            cursor.execute("SELECT DATABASE()")
            resultado = cursor.fetchone()
            print("Base de datos actual:", resultado)

    except Error as e:
        print("Error al conectar a MySQL:", e)

    finally:
        if 'conexion' in locals() and conexion.is_connected():
            conexion.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    conectar_mysql()

