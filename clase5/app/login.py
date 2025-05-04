from flask import Blueprint, request, jsonify

login = Blueprint('login', __name__)

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


@login.route('/login', methods=['POST'])
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

