from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api/pokemon', methods=['GET'])
def get_pokemon():
    limit = int(request.args.get('limit', 8))
    offset = int(request.args.get('offset', 0))
    
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}')
    data = response.json()
    
    # List to store detailed information about each Pokémon
    detailed_pokemon_list = []

    # Fetch additional data for each Pokémon
    for pokemon in data['results']:
        pokemon_details = requests.get(pokemon['url']).json()
        detailed_pokemon = {
            'name': pokemon_details['name'],
            'number': pokemon_details['id'],  # Pokédex number
            'types': [type_info['type']['name'] for type_info in pokemon_details['types']],  # List of types
            'image': pokemon_details['sprites']['front_default']  # Pokémon image URL
        }
        detailed_pokemon_list.append(detailed_pokemon)

    # Log the detailed data
    print("Detailed Pokémon data:", detailed_pokemon_list)

    return jsonify({
        'results': detailed_pokemon_list,
        'count': data['count']
    })

if __name__ == '__main__':
    app.run(debug=True)