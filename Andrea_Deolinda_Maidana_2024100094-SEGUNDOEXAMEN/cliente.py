from flask import Blueprint, request, jsonify

cliente=Blueprint('cliente',__name__)
@cliente.route('/cliente', methods=['POST'])

def llamarServiciosSet():
    ci = request.json.get('ci')

    codRes, menRes, accion = inicializarVariables(ci)

    salida = {
        'codRes': codRes,
        'menRes':menRes,
        'usuario': ci,

    }
    return jsonify(salida)
def inicializarVariables(ci):
    ciLocal = "4133266"
    codRes = 'SIN_ERROR'
    menRes = 'OK'
   
    try:
        print("Verificar login")
        if ci == ciLocal:
            accion = "Success"
            codRes = 'SIN_ERROR'
            menRes = 'OK' 
            ci ='4113266'

        else:
            accion= "Cliente no está en el sistema"
            codRes = 'ERROR'
            menRes = 'Error cliente'

    except Exception as e:
        print("ERROR", str(e))
        codRes = 'ERRROR'
        menRes = 'Msg: '+ str(e)
        accion = "Error interno"

    return codRes , menRes, accion

