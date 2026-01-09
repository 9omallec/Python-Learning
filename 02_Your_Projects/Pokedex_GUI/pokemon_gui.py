import tkinter as tk
import requests
import json
import random
from PIL import Image, ImageTk
from io import BytesIO

# Search Functionality
def search_pokemon(pokemon_id=None):
    if pokemon_id is None:
        pokemon_name = name_entry.get().lower()
        url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon_name
    else:
        url = 'https://pokeapi.co/api/v2/pokemon/' + str(pokemon_id)

    response = requests.get(url)

    if response.ok:
        data = response.json()
        species_url = data['species']['url']
        species_response = requests.get(species_url)
        species_data = species_response.json()

        # Get flavor text (description)
        flavor_text = ""
        for entry in species_data['flavor_text_entries']:
            if entry['language']['name'] == 'en':
                flavor_text = entry['flavor_text'].replace('\n', ' ').replace('\f', ' ')
                break

        # Evolution chain
        evolution_chain_url = species_data['evolution_chain']['url']
        evolution_response = requests.get(evolution_chain_url)
        evolution_data = evolution_response.json()

        # Evolution Chain -> Pokemon Name
        evolution_chain = []
        current = evolution_data['chain']
        evolution_chain.append(current['species']['name'])
        while current['evolves_to']:
            current = current['evolves_to'][0]
            evolution_chain.append(current['species']['name'])

        # Sprite
        sprite = data['sprites']['front_default']
        sprite_response = requests.get(sprite)
        img_data = BytesIO(sprite_response.content)
        img = Image.open(img_data)
        photo = ImageTk.PhotoImage(img)
        sprite_label.config(image = photo)
        sprite_label.image = photo

        if len(data['types']) == 1:
            type_name = data['types'][0]['type']['name'].capitalize()
        else:
            type1 = data['types'][0]['type']['name'].capitalize()
            type2 = data['types'][1]['type']['name'].capitalize()
            type_name = (f"{type1}/{type2}")
        height_m = data['height'] / 10             # Decimeters -> Meters
        weight_kg = data['weight'] / 10            # Hectograms -> Kilograms
        height_ft = int(height_m * 3.28084)        # Kilograms  -> Feet
        height_in = int((height_m * 39.3701) % 12) # Decimeters -> Remainder of Inches
        weight_lb = round(weight_kg * 2.20462)     # Kilograms  -> Pounds

        # Stats
        statistics = []
        for stats in data['stats']:
            stat_name = stats['stat']['name'].replace('-', ' ').title()
            stat_value = stats['base_stat']
            statistics.append((stat_name, stat_value))

        # Abilities
        abilities = []
        for ability in data['abilities']:
            ability_name = ability['ability']['name'].replace('-', ' ').title()
            if ability['is_hidden']:
                abilities.append(f"{ability_name} (Hidden)")
            else:
                abilities.append(ability_name)




        # Clear and populate name/ID text widget with bold labels
        name_id_label.config(state='normal')
        name_id_label.delete('1.0', 'end')
        name_id_label.insert('end', 'Name: ', 'bold')
        name_id_label.insert('end', f"{data['name'].title()}\n")
        name_id_label.insert('end', 'ID: ', 'bold')
        name_id_label.insert('end', f"#{data['id']}")
        name_id_label.config(state='disabled')
        # Clear and populate info text widget with bold labels
        info_label.config(state='normal')
        info_label.delete('1.0', 'end')
        info_label.insert('end', 'Type: ', 'bold')
        info_label.insert('end', f'{type_name}\n')
        info_label.insert('end', 'Stats:\n', 'bold')

        for stat_name, stat_value in statistics:
            info_label.insert('end', f'  {stat_name}: {stat_value}\n')
        info_label.insert('end', 'Abilities:\n', 'bold')
        for ability in abilities:
            info_label.insert('end', f'  {ability}\n')

        info_label.insert('end', 'Height: ', 'bold')
        info_label.insert('end', f"{height_ft}'{height_in}\"\n")
        info_label.insert('end', 'Weight: ', 'bold')
        info_label.insert('end', f'{weight_lb}lbs.\n')
        info_label.config(state='disabled')

        # Display flavor text
        flavor_text_label.config(state='normal')
        flavor_text_label.delete('1.0', 'end')
        flavor_text_label.insert('end', 'Description: ', 'bold')
        flavor_text_label.insert('end', flavor_text)
        flavor_text_label.config(state='disabled')

        # Display evolution chain sprites
        # Clear previous sprites
        evo_sprite1.config(image='')
        evo_sprite2.config(image='')
        evo_sprite3.config(image='')
        arrow1.config(text='')
        arrow2.config(text='')

        # Load and display evolution sprites
        if len(evolution_chain) >= 1:
            evo1_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{evolution_chain[0]}')
            if evo1_response.ok:
                evo1_data = evo1_response.json()
                evo1_sprite_url = evo1_data['sprites']['front_default']
                evo1_sprite_response = requests.get(evo1_sprite_url)
                evo1_img_data = BytesIO(evo1_sprite_response.content)
                evo1_img = Image.open(evo1_img_data)
                evo1_photo = ImageTk.PhotoImage(evo1_img)
                evo_sprite1.config(image=evo1_photo)
                evo_sprite1.image = evo1_photo

        if len(evolution_chain) >= 2:
            arrow1.config(text='→')
            evo2_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{evolution_chain[1]}')
            if evo2_response.ok:
                evo2_data = evo2_response.json()
                evo2_sprite_url = evo2_data['sprites']['front_default']
                evo2_sprite_response = requests.get(evo2_sprite_url)
                evo2_img_data = BytesIO(evo2_sprite_response.content)
                evo2_img = Image.open(evo2_img_data)
                evo2_photo = ImageTk.PhotoImage(evo2_img)
                evo_sprite2.config(image=evo2_photo)
                evo_sprite2.image = evo2_photo

        if len(evolution_chain) >= 3:
            arrow2.config(text='→')
            evo3_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{evolution_chain[2]}')
            if evo3_response.ok:
                evo3_data = evo3_response.json()
                evo3_sprite_url = evo3_data['sprites']['front_default']
                evo3_sprite_response = requests.get(evo3_sprite_url)
                evo3_img_data = BytesIO(evo3_sprite_response.content)
                evo3_img = Image.open(evo3_img_data)
                evo3_photo = ImageTk.PhotoImage(evo3_img)
                evo_sprite3.config(image=evo3_photo)
                evo_sprite3.image = evo3_photo

    else:
        info_label.config(state='normal')
        info_label.delete('1.0', 'end')
        info_label.insert('end', "Pokemon not found!")
        info_label.config(state='disabled')

def random_pokemon():
    random_id = random.randint(1, 151)
    search_pokemon(random_id)


# Main Window
window = tk.Tk()
window.title("Pokemon Info Generator")
window.geometry('500x850')
window.config(bg='red')

# Blue circle (Pokedex light)
circle_canvas = tk.Canvas(window, width=60, height=60, bg='red', highlightthickness=0)
circle_canvas.place(x=10, y=10)
    # Outer shadow
circle_canvas.create_oval(10, 10, 58, 58, fill='#000033', outline='')
    # Mid shadow
circle_canvas.create_oval(8, 8, 56, 56, fill='navy', outline='')
# Base circle with border
circle_canvas.create_oval(5, 5, 55, 55, fill='dodger blue', outline='dark grey', width=2)
    # Inner lighter layer
circle_canvas.create_oval(8, 8, 52, 52, fill='deep sky blue', outline='')
    # Bright highlight
circle_canvas.create_oval(12, 12, 35, 35, fill='light blue', outline='')
    # Secondary highlight
circle_canvas.create_oval(15, 15, 28, 28, fill='light cyan', outline='')
    # Sharp reflection spot
circle_canvas.create_oval(18, 14, 25, 21, fill='white', outline='')
# Red circle
red_circle = tk.Canvas(window, width=20, height=20, bg='red', highlightthickness=0)
red_circle.place(x=80, y=13)
red_circle.create_oval(3, 3, 18, 18, fill='dark red', outline='')  # Shadow
red_circle.create_oval(2, 2, 17, 17, fill='red', outline='dark grey', width=2)
red_circle.create_oval(4, 3, 9, 8, fill='#ff6666', outline='')
# Yellow circle
yellow_circle = tk.Canvas(window, width=20, height=20, bg='red', highlightthickness=0)
yellow_circle.place(x=102, y=13)
yellow_circle.create_oval(3, 3, 18, 18, fill='gold', outline='')  # Shadow
yellow_circle.create_oval(2, 2, 17, 17, fill='yellow', outline='dark grey', width=2)
yellow_circle.create_oval(4, 3, 9, 8, fill='#ffff99', outline='')
# Green circle
green_circle = tk.Canvas(window, width=20, height=20, bg='red', highlightthickness=0)
green_circle.place(x=124, y=13)
green_circle.create_oval(3, 3, 18, 18, fill='dark green', outline='')  # Shadow
green_circle.create_oval(2, 2, 17, 17, fill='green', outline='dark grey', width=2)
green_circle.create_oval(4, 3, 9, 8, fill='light green', outline='')

# Search Frame
search_frame = tk.Frame(window, bg='light blue', relief='sunken', borderwidth=2, highlightthickness=0)
search_frame.pack(pady=(40, 10))
# Input Field
name_label = tk.Label(search_frame, text="Enter Pokemon Name: ", bg='light blue')
name_label.pack()
name_entry = tk.Entry(search_frame, width=30, bg='white', fg='black', relief='solid', borderwidth=1)
name_entry.pack()
# Search Button
search_button = tk.Button(search_frame, text="Search Pokemon", command=search_pokemon)
search_button.pack(pady=2)
# Random Button
random_button = tk.Button(search_frame, text='Random', command=random_pokemon, bg='gold', fg='black')
random_button.pack(pady=2)
# Decorative separator line
separator_canvas = tk.Canvas(window, width=500, height=60, bg='red', highlightthickness=0)
separator_canvas.place(x=0, y=165)
# Shadow line
separator_canvas.create_line(
    0, 25,
    315, 25,
    325, 22,
    335, 18,
    345, 14,
    355, 10,
    365, 7,
    375, 5,
    385, 3,
    500, 3,
    fill='dark red', width=3, smooth=True
)
# Main line
separator_canvas.create_line(
    0, 23,      # Start at left edge
    315, 23,    # Go straight to the right edge
    325, 20,    # Start curving upward
    335, 16,
    345, 12,
    355, 8,
    365, 5,
    375, 3,
    385, 1,     # Reach top level
    500, 1,     # Continue to right edge at top level
    fill='black', width=2, smooth=True
)

# Data display frame (merged with flavor text)
data_frame = tk.Frame(window, bg='light blue', relief='sunken', borderwidth=4, highlightbackground='black', highlightthickness=2)
data_frame.pack(pady=(75, 10))
    # Name/ID text widget
name_id_label = tk.Text(data_frame, font=('Arial', 13), bg='light blue', fg='black', width=15, height=2, borderwidth=0, highlightthickness=0)
name_id_label.grid(row=0, column=0, sticky='nw', padx=10, pady=(10, 5))
name_id_label.tag_configure('bold', font=('Arial', 13, 'bold'))
    # Sprite label
sprite_label = tk.Label(data_frame, bg='light blue')
sprite_label.grid(row=1, column=0, padx=10, pady=(5, 10))
    # Info text widget
info_label = tk.Text(data_frame, font=('Arial', 12), bg='light blue', fg='black', width=28, height=14, borderwidth=0, highlightthickness=0)
info_label.grid(row=0, column=1, rowspan=2, sticky='n', padx=10, pady=(10, 5))
info_label.tag_configure('bold', font=('Arial', 12, 'bold'))
    # Flavor text widget (below sprite and info, spanning both columns)
flavor_text_label = tk.Text(data_frame, font=('Arial', 10), bg='light blue', fg='black', width=55, height=4, borderwidth=0, highlightthickness=0, wrap='word')
flavor_text_label.grid(row=3, column=0, columnspan=2, padx=10, pady=(5, 10))
flavor_text_label.tag_configure('bold', font=('Arial', 10, 'bold'))

# Separator line between data and evolution
middle_separator = tk.Canvas(window, width=500, height=20, bg='red', highlightthickness=0)
middle_separator.pack(pady=(0, 10))
    # Shadow line (darker, above main line)
middle_separator.create_line(0, 2, 500, 2, fill='dark red', width=3, smooth=True)
    # Main line
middle_separator.create_line(0, 4, 500, 4, fill='black', width=2, smooth=True)

# Evolution Chain Frame
evolution_frame = tk.Frame(window, bg='light blue', relief='sunken', borderwidth=4, highlightbackground='black', highlightthickness=2)
evolution_frame.pack(pady=(10, 10))
evolution_title = tk.Label(evolution_frame, text="Evolution Chain", font=('Arial', 12, 'bold'), bg='light blue', fg='black')
evolution_title.pack(pady=(5, 0))
# Container for evolution sprites and arrows
evolution_container = tk.Frame(evolution_frame, bg='light blue')
evolution_container.pack(pady=(5, 10))
# Evolution sprite labels (we'll create these dynamically)
evo_sprite1 = tk.Label(evolution_container, bg='light blue')
evo_sprite1.pack(side='left', padx=5)
arrow1 = tk.Label(evolution_container, text="→", font=('Arial', 20), bg='light blue', fg='black')
arrow1.pack(side='left', padx=5)
evo_sprite2 = tk.Label(evolution_container, bg='light blue')
evo_sprite2.pack(side='left', padx=5)
arrow2 = tk.Label(evolution_container, text="→", font=('Arial', 20), bg='light blue', fg='black')
arrow2.pack(side='left', padx=5)
evo_sprite3 = tk.Label(evolution_container, bg='light blue')
evo_sprite3.pack(side='left', padx=5)

# Bottom decorative separator line
bottom_separator = tk.Canvas(window, width=500, height=20, bg='red', highlightthickness=0)
bottom_separator.pack(pady=(10, 0))
    # Shadow line (darker, above main line - reversed)
bottom_separator.create_line(0, 2, 500, 2, fill='dark red', width=3, smooth=True)
    # Main line
bottom_separator.create_line(0, 4, 500, 4, fill='black', width=2, smooth=True)



# Run Application
window.mainloop()
