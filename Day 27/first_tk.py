from tkinter import *

window = Tk()

window.title("My first GUI Program")
window.minsize(width=500, height=700)

# Setting the label
my_label = Label(text="I am a Label", font=("Arial", 24))
my_label.pack()

my_label.config(text="Label")

# Button
def button_clicked():
    my_label.config(text=input_taken.get())


my_button = Button(text="Click Me", command=button_clicked)
my_button.pack()

# Entry - Entering the inputs and handling it
input_taken = Entry(width=50)
input_taken.insert(END, "Something to start with")
input_taken.pack()

# Text Box
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.0", END))
text.pack()

# Spinbox
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=10, command=spinbox_used)
spinbox.pack()

# Scale
scale = Scale(from_=0, to=100)
scale.pack()

# CheckButton
def checkbutton_used():
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checkbutton.pack()

# Radiobutton
def radiobutton_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radiobutton_used)
radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radiobutton_used)
radiobutton1.pack()
radiobutton2.pack()

# #Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
