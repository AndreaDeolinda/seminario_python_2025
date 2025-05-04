#!/usr/bin/env python3
from flask import Flask
from login import login

app = Flask(__name__)

## Servicios REST
app.register_blueprint(login)

@app.route('/', methods=['GET'])
def hello():
    return 'Hola Mundo'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)
