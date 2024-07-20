from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta de bienvenida
@app.route('/')
def welcome():
    return "Bienvenido al Servicio de Predicción"

# Endpoint de predicción (simulado)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Simulación de una predicción (ejemplo: suma de dos números)
    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)
    prediction = num1 + num2
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
