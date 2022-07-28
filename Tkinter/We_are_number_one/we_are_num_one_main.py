# This code is not very clean. At all. I might clean it up later.
import time
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

window = tk.Tk()
window.title('We are number one! (Hey!)')
# width & height don't need to be there explicitly, but improves readability
window.minsize(width=800, height=450)
# window.maxsize(width=800, height=600)  # By default monitor size

# Label
top_text = tk.Label(text="Here's a little lesson in trickery", font='Arial 18 bold')
top_text.pack(pady=5, side=tk.TOP)

bottom_text = tk.Label(text='This is going down in history', font='Arial 18 bold')
bottom_text.pack(pady=5, side=tk.BOTTOM)

# Image loading
file_name = 'images/we are number one.webp'

load = Image.open(file_name)
thickness = 2
CANVAS_WIDTH = load.width - (thickness * 2)
CANVAS_HEIGHT = load.height - (thickness * 2)
canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
                   highlightcolor='black', highlightbackground='black',
                   highlightthickness=thickness)
image_container = canvas.create_image(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
canvas.pack(padx=5, pady=5)

img = ImageTk.PhotoImage(load)
canvas.itemconfig(image_container, image=img)
canvas.imgref = img

# This must be at the end of your program
window.mainloop()
