from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Ruta para recibir datos del ESP32
@app.route('/api/datos', methods=['POST'])
def recibir_datos():
    datos = request.get_json()
    humedad = datos.get('humedad')
    fecha = datetime.now().isoformat()

    print(f"[{fecha}] Humedad recibida: {humedad}")

    # Lógica simple para decidir riego
    if humedad < 30:
        return "regar"
    else:
        return "no"

# Ruta de prueba
@app.route('/')
def home():
    return "Servidor REGENBOX activo"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
