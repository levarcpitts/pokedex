from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"

@app.route('/pokemon/<name>', methods=['GET'])
def get_pokemon(name):
    response = requests.get(f"{POKEAPI_URL}{name.lower()}")
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Pokemon not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)