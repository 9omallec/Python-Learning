
import requests
import json
url = "https://pokeapi.co/api/v2/pokemon/"


def info ():
    while True:
        mon = input("What Pokemon would you like to look up?: ")
        response = requests.get(url + mon)
        if response.ok:
            data = response.json()
            species_url = "https://pokeapi.co/api/v2/pokemon-species/"
            species_response = requests.get(species_url + mon)
            if species_response.ok:
                species_data = species_response.json()
            evolution_url = species_data['evolution_chain'] ['url']
            evolution_response = requests.get(evolution_url)
            if evolution_response.ok:
                evolution_data = evolution_response.json()
            first_stage = evolution_data ['chain'] ['species'] ['name']
            #print(f"Sprites: {data['sprites']}")
            print(f"\nName:        {data['name'].capitalize()}")
            print(f"ID:          #{data['id']}")
            if len(data['types']) == 1:
                print(f"Type:        {data['types'] [0] ['type'] ['name'].capitalize()}")
            else:
                type1 = data['types'] [0] ['type'] ['name'].capitalize()
                type2 = data['types'] [1] ['type'] ['name'].capitalize()
                print(f"Type:        {type1}/{type2}")
            print(f"Height:      {data['height'] / 10} Meters")
            print(f"Weight:      {data['weight'] / 10} Kilograms")
            print(f"|Base Stats: ")
            for stat in data['stats']:
                print(f"| {stat['stat'] ['name'].replace('-', ' ').title()} = {stat['base_stat']}")
            for ability in data['abilities']:
                if ability['is_hidden']:
                    print(f"Hidden Ability: {ability['ability'] ['name'].replace('-', ' ').capitalize()}")
                else:
                    print(f"Ability: {ability['ability'] ['name'].replace('-', ' ').capitalize()}")
            print(f"Total Moves:  {len(data['moves'])}")
            print(f"First Move:   {data['moves'] [0] ['move'] ['name'].title()}")
            evolution_chain = [first_stage.capitalize()]
            if len(evolution_data ['chain'] ['evolves_to']) > 0:
                second_stage = evolution_data ['chain'] ['evolves_to'] [0] ['species'] ['name']
                evolution_chain.append(second_stage)
                if len(evolution_data ['chain'] ['evolves_to'] [0] ['evolves_to']) > 0:
                    third_stage = evolution_data ['chain'] ['evolves_to'] [0] ['evolves_to'] [0] ['species'] ['name']
                    evolution_chain.append(third_stage)
            print(f"Evolutions:  {' -> '.join(evolution_chain).title()}")
            for entry in species_data['flavor_text_entries']:
                if entry['language'] ['name'] == 'en':
                    flavor_text = entry['flavor_text']
                    print(f"Description:  {flavor_text.replace(chr(12), ' ').replace('\n', ' ')}")
                    break
            reroll = input("-------------\nWould you like to look up another Pokemon?: ")
            if reroll.lower() in ["no", "quit", "n", "x"]:
                break
        else:
            print("Please double check spelling / valid Pokemon!")



info()