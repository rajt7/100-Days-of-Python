from tkinter import *

window = Tk()
window.title("Miles to Km Conversion")
window.minsize(width=500, height=500)


def button_clicked():
    choice = clicked.get()
    if choice == 'miles':
        kms = float(input_taken.get()) * 1.60934
        answer_label.config(text=kms)
    elif choice == 'meters':
        kms = float(input_taken.get()) / 1000
        answer_label.config(text=kms)


# Dropdown menu options
options = ['miles', 'meters']

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("miles")

# Create Dropdown menu
drop = OptionMenu(window, clicked, *options)
drop.grid(column=3, row=0)


# Labels
empty_label = Label()
empty_label.grid(column=0, row=0)

label1 = Label(text="is equal to", font=("Arial", 18))
label1.grid(column=0, row=1)

# miles_label = Label(text="miles", font=("Arial", 18))
# miles_label.grid(column=3, row=0)

km_label = Label(text="km", font=("Arial", 18))
km_label.grid(column=3, row=1)

answer_label = Label(text="0", font=("Arial", 18))
answer_label.grid(column=2, row=1)

# Text
input_taken = Entry(width=20)
input_taken.grid(column=2, row=0)
input_taken.focus()

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=2)

window.mainloop()
