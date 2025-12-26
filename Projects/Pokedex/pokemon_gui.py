import tkinter as tk
import requests
import json

url = "https://pokeapi.co/api/v2/pokemon/"

#Search Functionality
def search_pokemon():
    pokemon_name = name_entry.get().lower()
    url = "https://pokeapi.co/api/v2/pokemon/"
    
    response = requests.get(url + pokemon_name)

    if response.ok:
        data = response.json()
        result_text = f"Name: {data['name'].capitalize()}\nID: #{data['id']}"
        result_label.config(text=result_text)
    else:
        result_label.config(text="Pokemon not found!")


#Main Window
window = tk.Tk()
window.title("Pokemon Info Generator")
window.geometry("500x600")

#Input Field
name_label = tk.Label(window, text = "Enter Pokemon Name: ")
name_label.pack()
name_entry = tk.Entry(window, width = 30)
name_entry.pack()
#Search Button
search_button = tk.Button(window, text = "Search Pokemon", command = search_pokemon)
search_button.pack()
# Create a label to display results
result_label = tk.Label(window, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=20)




#Run Application
window.mainloop()






