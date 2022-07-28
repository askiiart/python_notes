import tkinter as tk

from PIL import Image, ImageTk

window = tk.Tk()
window.title('We are number one! (Hey!)')
# width & height don't need to be specified, but they are here for clarity
window.minsize(width=800, height=450)
# window.maxsize(width=800, height=600)  # By default monitor size

# Label(s)
top_text = tk.Label(text="Here's a little lesson in trickery", font='Arial 18 bold')
top_text.pack(pady=5, side=tk.TOP)

bottom_text = tk.Label(text='This is going down in history', font='Arial 18 bold')
bottom_text.pack(pady=5, side=tk.BOTTOM)

# Loading image into a PIL image object
file_name = 'images/we are number one.webp'
load = Image.open(file_name)

# Setting up canvas (and image on it)
thickness = 2
CANVAS_WIDTH = load.width - (thickness * 2)  # Accounts for border around image, makes image overlap with border,
CANVAS_HEIGHT = load.height - (thickness * 2)  # effectively slightly cropping the image.
canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
                   highlightcolor='black', highlightbackground='black',
                   highlightthickness=thickness)
image_container = canvas.create_image(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
canvas.pack(padx=5, pady=5)

# Loading image onto canvas
img = ImageTk.PhotoImage(load)
canvas.itemconfig(image_container, image=img)
canvas.imgref = img

# This must be at the end of your program
window.mainloop()
