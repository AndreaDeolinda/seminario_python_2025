from flask import Blueprint, request, jsonify
import mysql.connector
from mysql.connector import Error

login2 = Blueprint('login', __name__)

#configuración de la base de datos 
DB_CONFIG = {
    'host':'localhost',
    'user':'Andrea_Deolinda',
    'password':"unida123",
    'database':'jaguarete',
    'port':'3302'

}
def verificar_credenciales(user, password):
    connection = mysql.connector.connect(DB_CONFIG)
    cursor = connection.cursor(dictionary=True)

    query = "SELECT username FROM users WHERE username= %s AND pass = %s"
    cursor.execute(query,(user, password))
    #obtener el resultado
    result = cursor.fetchone()


def inicializarVariables(user, password):
    userLocal = "Andrea_Deolinda"
    passLocal = "unida123"
    codRes = "SIN_ERROR"
    menRes = "OK"
    accion = ""
    try:
        print("Verificar login")
        if password == passLocal and user == userLocal:
            print("Usuario y contraseña OK")
            accion = "Success"
        else:
            print("Usuario o contraseña incorrecta")
            accion = "Usuario o contraseña incorrecta"
            codRes = "ERROR"
            menRes = "Credenciales o usuario incorrectas"
    except Exception as e:
        print("ERROR", str(e))
        codRes = "ERROR"
        menRes = "Msg: " + str(e)
        accion = "Error interno"

    return codRes, menRes, accion


@login2.route('/login2', methods=['POST'])
def llamarServicioSet():
    user = request.json.get('user')
    password = request.json.get('password')
  
    
    codRes, menRes, accion = inicializarVariables(user, password)

    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'usuario': user,
        'accion': accion
    }
    return jsonify(salida)

