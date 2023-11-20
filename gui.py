from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog
from PIL import Image, ImageTk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Matias\CODE\Tkinter-Designer-master\Tkinter-Designer-master\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("WaterMark")

window.geometry("700x700")
window.configure(bg="#FFFFFF")


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=700,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.pack()

def open_file():
    global file_path
    file_path = filedialog.askopenfilename(title="Select file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    if file_path:
        image = Image.open(file_path)
        image = image.resize((image_image_1.width(), image_image_1.height()), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(image)
        canvas.itemconfig(image_1, image=new_image)
        canvas.image = new_image
        
image_image_1 = PhotoImage(file="assets/frame0/image_1.png")
image_1 = canvas.create_image(348.0, 296.0, image=image_image_1)

from PIL import ImageTk

def open_overlay_image():
    global file_path2
    file_path2 = filedialog.askopenfilename(title="Select overlay file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    if file_path2:
        image = Image.open(file_path2)
        image = image.resize((image_image_1.width(), image_image_1.height()), Image.ANTIALIAS)
        overlay_image = ImageTk.PhotoImage(image)
        canvas.create_image(348.0, 296.0, image=overlay_image)
        canvas.overlay_image = overlay_image  # keep a reference to the image

def save_combined_image():
    if file_path and file_path2:
        original_image = Image.open(file_path)
        overlay_image = Image.open(file_path2)
        overlay_image = overlay_image.resize(original_image.size, Image.ANTIALIAS)  # resize overlay image
        combined_image = Image.alpha_composite(original_image.convert('RGBA'), overlay_image.convert('RGBA'))
        
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=(("PNG files", "*.png"), ("All files", "*.*")))
        if save_path:
            combined_image.save(save_path)



button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_file,
    relief="flat"
)
button_1.place(
    x=27.0,
    y=619.0,
    width=202.385009765625,
    height=34.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_overlay_image,
    relief="flat"
)
button_2.place(
    x=248.0,
    y=619.0,
    width=202.385009765625,
    height=34.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=save_combined_image,
    relief="flat"
)
button_3.place(
    x=471.0,
    y=619.0,
    width=202.385009765625,
    height=34.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    348.0,
    296.0,
    image=image_image_1
)
window.resizable(False, False)

window.mainloop()
