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


# Button
def button_clicked():
    # top_text['text'] = 'Button was pressed'  # Another way to change the text (it works like a dict)
    top_text.config(text='Hi')


button = tk.Button(text='Click me!', command=button_clicked)
button.pack(pady=30)

# I don't like these, so I'm commenting them out
# Entry (one line text box)
my_entry = tk.Entry(width=30)
my_entry.focus()
my_entry.insert(index=0, string='Some text to begin with')
my_entry.pack(pady=5, side=tk.LEFT)

# Text
my_text = tk.Text(height=5, width=30)
my_text.focus()
my_text.insert(index=tk.END, chars='Enter input: ')
my_text.pack(pady=5, padx=5, side=tk.RIGHT)


# Spinbox
def spinbox_used():
    top_text.config(text=my_spinbox.get() + ' Luftballons')
    print(my_spinbox.get())


my_spinbox = tk.Spinbox(from_=0, to=99, width=5, command=spinbox_used)
my_spinbox.pack(pady=10)


# Scale
def scale_used(value):
    top_text.config(text=value + ' Luftballons')


my_scale = tk.Scale(from_=0, to=99, command=scale_used, orient=tk.HORIZONTAL, width=10, length=396)
my_scale.pack(pady=5, padx=7)


# Checkbutton (Checkbox)
def checkbutton_used():
    print(checked_state.get())
    if checked_state.get() == 1:
        bottom_text.config(text='The Berlin wall has been torn down')
    else:
        bottom_text.config(text='The Berlin wall is still standing')


checked_state = tk.IntVar()
my_checkbutton = tk.Checkbutton(text='Is after November 9, 1989', variable=checked_state, command=checkbutton_used)
my_checkbutton.pack(pady=2)


# Radiobutton
def radio_used():
    print(radio_state.get())


radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text='Option1', value=1, variable=radio_state, command=radio_used)
radiobutton2 = tk.Radiobutton(text='Option2', value=2, variable=radio_state, command=radio_used)
radiobutton3 = tk.Radiobutton(text='Option3', value=3, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack(pady=(0, 5))  # Puts 5 padding on bottom


# Listbox
def listbox_used(event):
    print(my_listbox.get(my_listbox.curselection()))


my_listbox = tk.Listbox(height=3)
fruits = ['Apple', 'Pear', 'Orange', 'Banana']
for i, fruit in enumerate(fruits):
    my_listbox.insert(i, fruit)
my_listbox.bind(sequence='<<ListboxSelect>>', func=listbox_used)
my_listbox.pack()


# Combobox
def combobox_used(event):
    print(str_value.get())


str_value = tk.StringVar()
my_combobox = ttk.Combobox(width=30, textvariable=str_value)
my_combobox.bind(sequence='<<ComboboxSelect>>', func=combobox_used)
my_combobox['values'] = ('Hast', 'du', 'etwas', 'zeit', 'für', 'mich?')
my_combobox.pack(pady=(5, 108))

# Slideshow presenter
# Load the image file names into a list
file_list = []
for path, subdirs, files in os.walk('my_images'):
    for filename in files:
        f = os.path.join(path, filename)
        file_list.append(f)


def next_image():
    global image_num
    # Get image name and load it
    image_num = (image_num + 1) % len(file_list)
    load = Image.open(file_list[image_num])
    pic_label.config(text=file_list[image_num])

    # Place image on canvas
    img = ImageTk.PhotoImage(load)
    canvas.itemconfig(image_container, image=img)
    canvas.imgref = img


CANVAS_WIDTH = 790
CANVAS_HEIGHT = 440
canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
                   highlightcolor='black', highlightbackground='black',
                   highlightthickness=5)
image_container = canvas.create_image(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
canvas.pack(padx=5, pady=5)
image_num = -1

pic_label = tk.Label(text='')
pic_label.pack(pady=5)

next_image()

next_button = tk.Button(text='Next', command=next_image)
next_button.pack(pady=5)

# This must be at the end of your program
window.mainloop()
