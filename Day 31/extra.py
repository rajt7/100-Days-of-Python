from tkinter import *


def display_str():
    extra_label.config(text="Extra change...")


window = Tk()
window.config(width=200, height=200)

extra_label = Label(text="Extra", font=("Ariel", 50, "bold"))
extra_label.pack()
window.after(2000, display_str)

window.mainloop()
