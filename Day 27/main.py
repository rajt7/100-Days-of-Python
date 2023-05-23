from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Setting the label
my_label = Label(text="I am a Label", font=("Arial", 24))
my_label.config(text="Label")
my_label.grid(column=0, row=0)
my_label.config(padx=10)

# Button
button1 = Button(text="Click Me")
button1.grid(column=1, row=1)
button1.config(padx=10, pady=20)

button2 = Button(text="Don't click me")
button2.grid(column=3, row=0)
button2.config(padx=10, pady=10)

# Entry - Entering the inputs and handling it
input_taken = Entry(width=30)
input_taken.grid(column=4, row=2)
button2.config(padx=10, pady=10)

window.mainloop()
