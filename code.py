from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

root = Tk()
def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + "png"
    url = pyqrcode.create(link)
    url.png(file_name,scale=8)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    Canvas.create_window(200,250,window=image_label)



Canvas = Canvas(root, width=400, height=600)
Canvas.pack()

app_label = Label(root, text="OR Code Generator", fg='green', font=("Arial", 30))
Canvas.create_window(200, 50, window=app_label)

name_label = Label(root, text="Link name")
link_label = Label(root, text="link")
Canvas.create_window(200, 100, window=name_label)
Canvas.create_window(200, 160, window=link_label)

name_entry = Entry(root)
link_entry = Entry(root)
Canvas.create_window(200, 130, window=name_entry)
Canvas.create_window(200, 180, window=link_entry)

button = Button(text="Generate QO code", command=generate)
Canvas.create_window(200, 230, window=button)


root.mainloop()
