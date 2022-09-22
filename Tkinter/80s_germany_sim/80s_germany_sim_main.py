import tkinter as tk

window = tk.Tk()
window.title('80s Germany Simulator')

# Labels
top_text = tk.Label(text="0 Luftballons", font='Impact')
top_text.pack(side=tk.TOP)

bottom_text = tk.Label(text='', font='Impact')
bottom_text.pack(side=tk.BOTTOM)


# Scale
def scale_used(value):
    top_text.config(text=value + ' Luftballons')


my_scale = tk.Scale(from_=0, to=99, command=scale_used, orient=tk.HORIZONTAL, width=10, length=396)
my_scale.pack(pady=5, padx=7)


# Checkbutton
def checkbutton_used():
    if checked_state.get() == 1:
        bottom_text.config(text='The Berlin wall has been torn down')
    else:
        bottom_text.config(text='The Berlin wall is still standing')


checked_state = tk.IntVar()
my_checkbutton = tk.Checkbutton(text='Is after November 9, 1989', variable=checked_state, command=checkbutton_used)
my_checkbutton.pack(pady=2)

window.mainloop()
