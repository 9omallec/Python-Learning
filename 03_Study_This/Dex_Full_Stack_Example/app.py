"""
Dex: A Modern, Feature-Rich Pokedex Web Application
Built with Flask, PokeAPI, HTML, CSS, and JavaScript

Advanced Features:
- Team Builder (save up to 6 Pokemon)
- Favorites System
- Shiny Sprite Toggle
- Type Effectiveness Chart
- Pokemon Moves Display
- Dark Mode
- Advanced Stats Visualization
- Search History
"""

from flask import Flask, render_template, jsonify, request
import requests
from io import BytesIO
import base64

# Initialize Flask application
app = Flask(__name__)


# ============================================
# TYPE EFFECTIVENESS DATA
# ============================================

TYPE_EFFECTIVENESS = {
    'normal': {'weak_to': ['fighting'], 'resistant_to': [], 'immune_to': ['ghost']},
    'fire': {'weak_to': ['water', 'ground', 'rock'], 'resistant_to': ['fire', 'grass', 'ice', 'bug', 'steel', 'fairy'], 'immune_to': []},
    'water': {'weak_to': ['electric', 'grass'], 'resistant_to': ['fire', 'water', 'ice', 'steel'], 'immune_to': []},
    'electric': {'weak_to': ['ground'], 'resistant_to': ['electric', 'flying', 'steel'], 'immune_to': []},
    'grass': {'weak_to': ['fire', 'ice', 'poison', 'flying', 'bug'], 'resistant_to': ['water', 'electric', 'grass', 'ground'], 'immune_to': []},
    'ice': {'weak_to': ['fire', 'fighting', 'rock', 'steel'], 'resistant_to': ['ice'], 'immune_to': []},
    'fighting': {'weak_to': ['flying', 'psychic', 'fairy'], 'resistant_to': ['bug', 'rock', 'dark'], 'immune_to': []},
    'poison': {'weak_to': ['ground', 'psychic'], 'resistant_to': ['grass', 'fighting', 'poison', 'bug', 'fairy'], 'immune_to': []},
    'ground': {'weak_to': ['water', 'grass', 'ice'], 'resistant_to': ['poison', 'rock'], 'immune_to': ['electric']},
    'flying': {'weak_to': ['electric', 'ice', 'rock'], 'resistant_to': ['grass', 'fighting', 'bug'], 'immune_to': ['ground']},
    'psychic': {'weak_to': ['bug', 'ghost', 'dark'], 'resistant_to': ['fighting', 'psychic'], 'immune_to': []},
    'bug': {'weak_to': ['fire', 'flying', 'rock'], 'resistant_to': ['grass', 'fighting', 'ground'], 'immune_to': []},
    'rock': {'weak_to': ['water', 'grass', 'fighting', 'ground', 'steel'], 'resistant_to': ['normal', 'fire', 'poison', 'flying'], 'immune_to': []},
    'ghost': {'weak_to': ['ghost', 'dark'], 'resistant_to': ['poison', 'bug'], 'immune_to': ['normal', 'fighting']},
    'dragon': {'weak_to': ['ice', 'dragon', 'fairy'], 'resistant_to': ['fire', 'water', 'electric', 'grass'], 'immune_to': []},
    'dark': {'weak_to': ['fighting', 'bug', 'fairy'], 'resistant_to': ['ghost', 'dark'], 'immune_to': ['psychic']},
    'steel': {'weak_to': ['fire', 'fighting', 'ground'], 'resistant_to': ['normal', 'grass', 'ice', 'flying', 'psychic', 'bug', 'rock', 'dragon', 'steel', 'fairy'], 'immune_to': ['poison']},
    'fairy': {'weak_to': ['poison', 'steel'], 'resistant_to': ['fighting', 'bug', 'dark'], 'immune_to': ['dragon']}
}


# ============================================
# HELPER FUNCTIONS (API Integration Logic)
# ============================================

def fetch_pokemon_data(pokemon_identifier):
    """
    Fetch comprehensive Pokemon data from PokeAPI with extended information.

    Args:
        pokemon_identifier (str): Pokemon name or ID number

    Returns:
        dict: Complete Pokemon data including stats, sprites, moves, and type effectiveness
        None: If Pokemon not found or API error
    """
    try:
        # 1. Get basic Pokemon data
        base_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_identifier.lower()}'
        response = requests.get(base_url, timeout=10)

        if not response.ok:
            return None

        pokemon_data = response.json()

        # 2. Get species data
        species_url = pokemon_data['species']['url']
        species_response = requests.get(species_url, timeout=10)
        species_data = species_response.json()

        # 3. Extract English description
        description = get_english_description(species_data)

        # 4. Get evolution chain
        evolution_chain = get_evolution_chain(species_data)

        # 5. Get moves (limit to first 8 learned by level-up)
        moves = get_pokemon_moves(pokemon_data)

        # 6. Get type effectiveness
        types_list = [t['type']['name'] for t in pokemon_data['types']]
        type_effectiveness = calculate_type_effectiveness(types_list)

        # 7. Get generation
        generation = species_data['generation']['name'].replace('generation-', 'Gen ').upper()

        # 8. Get habitat (if available)
        habitat = species_data.get('habitat')
        habitat_name = habitat['name'].title() if habitat else 'Unknown'

        # 9. Get gender ratio
        gender_rate = species_data.get('gender_rate', -1)
        gender_ratio = calculate_gender_ratio(gender_rate)

        # 10. Process and format the data
        processed_data = {
            'id': pokemon_data['id'],
            'name': pokemon_data['name'].title(),
            'sprite': pokemon_data['sprites']['front_default'],
            'sprite_shiny': pokemon_data['sprites']['front_shiny'],
            'sprite_back': pokemon_data['sprites']['back_default'],
            'sprite_animated': pokemon_data['sprites']['versions']['generation-v']['black-white']['animated']['front_default'] if pokemon_data['sprites']['versions']['generation-v']['black-white']['animated']['front_default'] else pokemon_data['sprites']['front_default'],
            'types': format_types(pokemon_data['types']),
            'types_array': types_list,
            'stats': format_stats(pokemon_data['stats']),
            'abilities': format_abilities(pokemon_data['abilities']),
            'height': convert_height(pokemon_data['height']),
            'weight': convert_weight(pokemon_data['weight']),
            'description': description,
            'evolution_chain': evolution_chain,
            'moves': moves,
            'type_effectiveness': type_effectiveness,
            'generation': generation,
            'habitat': habitat_name,
            'gender_ratio': gender_ratio,
            'base_experience': pokemon_data.get('base_experience', 0),
            'capture_rate': species_data.get('capture_rate', 0)
        }

        return processed_data

    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None


def get_english_description(species_data):
    """Extract the first English flavor text from species data."""
    for entry in species_data.get('flavor_text_entries', []):
        if entry['language']['name'] == 'en':
            return entry['flavor_text'].replace('\n', ' ').replace('\f', ' ')
    return "No description available."


def get_evolution_chain(species_data):
    """Fetch and parse the evolution chain for a Pokemon."""
    try:
        evo_chain_url = species_data['evolution_chain']['url']
        evo_response = requests.get(evo_chain_url, timeout=10)
        evo_data = evo_response.json()

        evolution_list = []
        current = evo_data['chain']

        while current:
            species_name = current['species']['name']
            sprite = get_pokemon_sprite(species_name)

            # Get evolution details
            evolution_detail = None
            if current.get('evolution_details') and len(current['evolution_details']) > 0:
                detail = current['evolution_details'][0]
                if detail.get('min_level'):
                    evolution_detail = f"Level {detail['min_level']}"
                elif detail.get('item'):
                    evolution_detail = detail['item']['name'].replace('-', ' ').title()
                elif detail.get('trigger'):
                    evolution_detail = detail['trigger']['name'].replace('-', ' ').title()

            evolution_list.append({
                'name': species_name.title(),
                'sprite': sprite,
                'method': evolution_detail
            })

            if current.get('evolves_to'):
                current = current['evolves_to'][0]
            else:
                break

        return evolution_list

    except Exception as e:
        print(f"Evolution Chain Error: {e}")
        return []


def get_pokemon_sprite(pokemon_name):
    """Fetch the sprite URL for a given Pokemon."""
    try:
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
        response = requests.get(url, timeout=10)
        if response.ok:
            data = response.json()
            return data['sprites']['front_default']
    except Exception:
        pass
    return ""


def get_pokemon_moves(pokemon_data):
    """
    Extract Pokemon moves (limit to level-up moves).

    Args:
        pokemon_data (dict): Pokemon data from PokeAPI

    Returns:
        list: List of move objects with name and learn method
    """
    moves_list = []

    for move_entry in pokemon_data.get('moves', []):
        # Only include moves learned by level-up
        for version_detail in move_entry['version_group_details']:
            if version_detail['move_learn_method']['name'] == 'level-up':
                level = version_detail['level_learned_at']
                move_name = move_entry['move']['name'].replace('-', ' ').title()
                moves_list.append({
                    'name': move_name,
                    'level': level
                })
                break  # Only add once per move

    # Sort by level and limit to first 12
    moves_list.sort(key=lambda x: x['level'])
    return moves_list[:12]


def calculate_type_effectiveness(types_list):
    """
    Calculate type effectiveness for a Pokemon based on its types.

    Args:
        types_list (list): List of type names

    Returns:
        dict: Weaknesses, resistances, and immunities
    """
    weak_to = set()
    resistant_to = set()
    immune_to = set()

    for poke_type in types_list:
        if poke_type in TYPE_EFFECTIVENESS:
            effectiveness = TYPE_EFFECTIVENESS[poke_type]
            weak_to.update(effectiveness['weak_to'])
            resistant_to.update(effectiveness['resistant_to'])
            immune_to.update(effectiveness['immune_to'])

    # Remove overlaps (immunities override weaknesses and resistances)
    weak_to -= immune_to
    resistant_to -= immune_to

    # Remove types that appear in both weak and resistant (they cancel out)
    neutral = weak_to & resistant_to
    weak_to -= neutral
    resistant_to -= neutral

    return {
        'weak_to': sorted(list(weak_to)),
        'resistant_to': sorted(list(resistant_to)),
        'immune_to': sorted(list(immune_to))
    }


def calculate_gender_ratio(gender_rate):
    """
    Calculate gender ratio from gender_rate value.

    Args:
        gender_rate (int): -1 for genderless, 0-8 for female ratio

    Returns:
        str: Formatted gender ratio
    """
    if gender_rate == -1:
        return "Genderless"

    female_percent = (gender_rate / 8) * 100
    male_percent = 100 - female_percent

    return f"♂ {male_percent:.0f}% / ♀ {female_percent:.0f}%"


def format_types(types_data):
    """Format Pokemon types into a readable string."""
    type_names = [t['type']['name'].capitalize() for t in types_data]
    return '/'.join(type_names)


def format_stats(stats_data):
    """Format Pokemon stats into a clean list."""
    formatted_stats = []
    stat_abbreviations = {
        'hp': 'HP',
        'attack': 'ATK',
        'defense': 'DEF',
        'special-attack': 'SP.ATK',
        'special-defense': 'SP.DEF',
        'speed': 'SPD'
    }

    for stat in stats_data:
        stat_name = stat['stat']['name']
        stat_display = stat_abbreviations.get(stat_name, stat_name.replace('-', ' ').title())
        stat_value = stat['base_stat']
        formatted_stats.append({
            'name': stat_display,
            'value': stat_value
        })
    return formatted_stats


def format_abilities(abilities_data):
    """Format Pokemon abilities into readable strings."""
    formatted_abilities = []
    for ability in abilities_data:
        ability_name = ability['ability']['name'].replace('-', ' ').title()
        if ability['is_hidden']:
            formatted_abilities.append(f"{ability_name} (Hidden)")
        else:
            formatted_abilities.append(ability_name)
    return formatted_abilities


def convert_height(decimeters):
    """Convert height from decimeters to feet and inches."""
    meters = decimeters / 10
    total_inches = meters * 39.3701
    feet = int(total_inches // 12)
    inches = int(total_inches % 12)
    return f"{feet}'{inches}\""


def convert_weight(hectograms):
    """Convert weight from hectograms to pounds."""
    kilograms = hectograms / 10
    pounds = round(kilograms * 2.20462)
    return f"{pounds} lbs"


# ============================================
# FLASK ROUTES (URL Endpoints)
# ============================================

@app.route('/')
def index():
    """Homepage route - renders the main Pokedex interface."""
    return render_template('index.html')


@app.route('/api/pokemon/<identifier>')
def get_pokemon(identifier):
    """
    API endpoint to fetch Pokemon data.

    Returns comprehensive Pokemon data including moves, type effectiveness, and more.
    """
    pokemon_data = fetch_pokemon_data(identifier)

    if pokemon_data:
        return jsonify({
            'success': True,
            'data': pokemon_data
        })
    else:
        return jsonify({
            'success': False,
            'error': 'Pokemon not found'
        }), 404


@app.route('/api/random')
def get_random_pokemon():
    """API endpoint to fetch a random Pokemon (Gen 1-8: 1-898)."""
    import random
    random_id = random.randint(1, 898)

    pokemon_data = fetch_pokemon_data(str(random_id))

    if pokemon_data:
        return jsonify({
            'success': True,
            'data': pokemon_data
        })
    else:
        return jsonify({
            'success': False,
            'error': 'Could not fetch random Pokemon'
        }), 500


@app.route('/api/search-suggestions/<query>')
def get_search_suggestions(query):
    """
    API endpoint to get Pokemon name suggestions for autocomplete.

    Args:
        query (str): Partial Pokemon name

    Returns:
        JSON: List of matching Pokemon names
    """
    # This is a simplified version - in production you'd cache the full Pokemon list
    # For now, return empty array (can be enhanced later)
    return jsonify({
        'success': True,
        'suggestions': []
    })


# ============================================
# RUN THE APPLICATION
# ============================================

if __name__ == '__main__':
    app.run(debug=True, port=5000)
