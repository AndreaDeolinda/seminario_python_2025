# main.py

from flask import Flask, request, jsonify
from cliente import buscar_cliente

app = Flask(__name__)

@app.route('/cliente', methods=['POST'])
def consultar_cliente():
    datos = request.get_json()
    ci = datos.get("ci")

    cliente = buscar_cliente(ci)
    
    if cliente:
        return jsonify({
            "accion": "Success",
            "codRes": "SIN_ERROR",
            "menRes": "OK",
            "ci": ci
        })
    else:
        return jsonify({
            "accion": "Cliente no está en el sistema",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": ci
        })

if __name__ == '__main__':
    # Ejecutar en localhost y puerto 5003 como se solicita
    app.run(host="127.0.0.1", port=5003, debug=True)
