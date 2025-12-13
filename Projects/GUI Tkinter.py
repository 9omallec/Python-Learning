
from PIL import Image, ImageTk
import tkinter as tk
import requests

root = tk.Tk()
root.title("Image Randomizer")

# Widgets...
response = requests.get("https://picsum.photos/200/300")

message = "Choose Image Size"
message = tk.Label(root, text = message)
message.config(fg = 'purple')
message.grid(row = 0, column = 0, columnspan = 2)

height = tk.Label(root, text = "Height").grid(row=2) #Height Lable/Input
height = tk.Entry(root)
height.config(fg = 'purple')
height.grid(row = 2, column = 1)


width = tk.Label(root, text = "Width").grid(row = 3) #Width Label/Input
width = tk.Entry(root)
width.config(fg = 'purple')
width.grid(row = 3, column = 1)


button = tk.Button(root, text = 'Stop', width = 25, command = root.destroy) #Stop Button
button.grid(row = 4, column = 1)


root.mainloop()