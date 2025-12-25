
from PIL import Image, ImageTk
import tkinter as tk
import requests
from io import BytesIO

root = tk.Tk()
root.title("Image Randomizer")

# Widgets...
message = "Choose Image Size"
message = tk.Label(root, text = message)
message.config(fg = 'purple')
message.grid(row = 0, column = 0, columnspan = 2)

height = tk.Label(root, text = "Height").grid(row=2) #Height Label/Input
height = tk.Entry(root)
height.config(fg = 'purple')
height.grid(row = 2, column = 1)


width = tk.Label(root, text = "Width").grid(row = 3) #Width Label/Input
width = tk.Entry(root)
width.config(fg = 'purple')
width.grid(row = 3, column = 1)

# Label to display the image
image_label = tk.Label(root)
image_label.grid(row = 5, column = 0, columnspan = 2)

def randomize_image():
    h = height.get()
    w = width.get()

    response = requests.get(f"https://picsum.photos/{w}/{h}")
    img = Image.open(BytesIO(response.content))
    photo = ImageTk.PhotoImage(img)

    image_label.config(image=photo)
    image_label.image = photo

button = tk.Button(root, text = 'Randomize!', width = 25, fg = 'purple', command = randomize_image)
button.grid(row = 4, column = 1)


root.mainloop()
