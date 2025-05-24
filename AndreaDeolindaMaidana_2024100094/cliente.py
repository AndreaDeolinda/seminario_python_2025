# cliente.py

# Simulación de base de datos de clientes
clientes = {
    "4133266": {
        "nombre": "Juan Pérez"
    }
}

def buscar_cliente(ci):
    return clientes.get(ci, None)
