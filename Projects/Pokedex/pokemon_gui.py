import tkinter as tk
import requests
import json
from PIL import Image, ImageTk
from io import BytesIO

# Search Functionality
def search_pokemon():
    pokemon_name = name_entry.get().lower()
    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url + pokemon_name)

    if response.ok:
        data = response.json()
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
    else:
        info_label.config(state='normal')
        info_label.delete('1.0', 'end')
        info_label.insert('end', "Pokemon not found!")
        info_label.config(state='disabled')



# Main Window
window = tk.Tk()
window.title("Pokemon Info Generator")
window.geometry('500x600')
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

# Search Frame (centered)
search_frame = tk.Frame(window, bg='light blue', relief='sunken', borderwidth=4, highlightbackground='black', highlightthickness=2)
search_frame.pack(pady=10)
# Input Field
name_label = tk.Label(search_frame, text="Enter Pokemon Name: ", bg='light blue')
name_label.pack()
name_entry = tk.Entry(search_frame, width=30)
name_entry.pack()
# Search Button
search_button = tk.Button(search_frame, text="Search Pokemon", command=search_pokemon)
search_button.pack()
# Decorative separator line
separator_canvas = tk.Canvas(window, width=500, height=60, bg='red', highlightthickness=0)
separator_canvas.place(x=0, y=90)
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

# Data display frame
data_frame = tk.Frame(window, bg='light blue', relief='sunken', borderwidth=4, highlightbackground='black', highlightthickness=2)
data_frame.pack(pady=(30, 10))
    # Name/ID text widget
name_id_label = tk.Text(data_frame, font=('Arial', 13), bg='light blue', width=15, height=2, borderwidth=0, highlightthickness=0)
name_id_label.grid(row=0, column=0, sticky='nw', padx=10, pady=(10, 5))
name_id_label.tag_configure('bold', font=('Arial', 13, 'bold'))
    # Sprite label
sprite_label = tk.Label(data_frame, bg='light blue')
sprite_label.grid(row=1, column=0, padx=10, pady=(5, 10))
    # Info text widget
info_label = tk.Text(data_frame, font=('Arial', 12), bg='light blue', width=28, height=14, borderwidth=0, highlightthickness=0)
info_label.grid(row=0, column=1, rowspan=2, sticky='n', padx=10, pady=10)
info_label.tag_configure('bold', font=('Arial', 12, 'bold'))
    # Bottom decorative separator line
bottom_separator = tk.Canvas(window, width=500, height=20, bg='red', highlightthickness=0)
bottom_separator.place(x=0, y=440)
    # Shadow line (darker, above main line - reversed)
bottom_separator.create_line(
    0, 2,
    500, 2,
    fill='dark red', width=3, smooth=True
)
    # Main line
bottom_separator.create_line(
    0, 4,
    500, 4,
    fill='black', width=2, smooth=True
)



# Run Application
window.mainloop()
