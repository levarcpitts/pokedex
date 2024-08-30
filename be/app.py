from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def convert_height_to_feet_and_inches(height_dm):
    """Convert height from decimeters to feet and inches."""
    total_inches = height_dm * 3.937
    feet = int(total_inches // 12)
    inches = int(total_inches % 12)
    return f"{feet}’{inches}”"

def convert_weight_to_pounds(weight_hg):
    """Convert weight from hectograms to pounds."""
    pounds = weight_hg * 0.220462
    return f"{pounds:.1f} lbs"

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
        
        # Extract required information
        species = pokemon_details['species']['name']
        height = convert_height_to_feet_and_inches(pokemon_details['height'])
        weight = convert_weight_to_pounds(pokemon_details['weight'])
        abilities = [ability['ability']['name'] for ability in pokemon_details['abilities']]
        
        # Create a detailed Pokémon dictionary
        detailed_pokemon = {
            'name': pokemon_details['name'],
            'number': pokemon_details['id'],  # Pokédex number
            'types': [type_info['type']['name'] for type_info in pokemon_details['types']],  # List of types
            'image': pokemon_details['sprites']['front_default'],  # Pokémon image URL
            'species': species,
            'height': height,
            'weight': weight,
            'abilities': abilities
        }
        detailed_pokemon_list.append(detailed_pokemon)

    return jsonify({
        'results': detailed_pokemon_list,
        'count': data['count']
    })

if __name__ == '__main__':
    app.run(debug=True)