from PIL import Image, ImageTk
import tkinter as tk
import requests

root = tk.Tk()
root.title("Image Randomizer")

# Widgets...
message = "Choose Image Size"
message = tk.Label(root, text = message)
message.config(fg = 'purple')
message.grid(row = 0, column = 0, columnspan = 2)

#Height Lable/Input
height = tk.Label(root, text = "Height", fg = 'purple').grid(row=2)
height = tk.Entry(root)
height.config(fg = 'purple')
height.grid(row = 2, column = 1)

#Width Label/Input
width = tk.Label(root, text = "Width", fg = 'purple').grid(row = 3)
width = tk.Entry(root)
width.config(fg = 'purple')
width.grid(row = 3, column = 1)

#Button
image_label = tk.Label(root)
image_label.grid(row = 5, column = 0, columnspan = 2)
def test():
    h = height.get()
    w = width.get()
    #Input validation
    if h == "" or w == "":
        message.config(text = "Enter both Height & Width!", fg = 'red')
        return
    if not h.isdigit() or not w.isdigit():
        message.config(text = "Enter Numbers Only!", fg = 'red')
        return
    if int(h) >= 2000 or int(w) >= 2000:
        message.config(text = "Dimension of 2,000 or more is too large", fg = 'red')
        return
    if int(h) <= 10 or int(w) <= 10:
        message.config(text = "Dimensions of 10 or smaller is too small", fg = 'red')
        return
    #Validation passed
    message.config(text = "Choose Image Size", fg = 'purple')

    response = requests.get(f"https://picsum.photos/{w}/{h}")
    from io import BytesIO
    image_data = BytesIO(response.content)
    img = Image.open(image_data)
    photo = ImageTk.PhotoImage(img)
    image_label.config(image = photo)
    image_label.image = photo

button = tk.Button(root, text = 'Randomize', fg = 'purple', width = 25, command = test)
button.grid(row = 4, column = 1)


root.mainloop()