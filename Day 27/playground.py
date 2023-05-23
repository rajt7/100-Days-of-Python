# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total
#
#
# result = add(3, 4, 5, 6)
# print(result)

# def calculate(**kwargs):
#     print(kwargs.items())
#
#
# calculate(add=3, multiply=5)

from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#F2B90C')

def display_selected(choice):
    choice = variable.get()
    print(choice)

countries = ['Bahamas','Canada', 'Cuba','United States']

# setting variable for Integers
variable = StringVar()
variable.set(countries[3])

# creating widget
dropdown = OptionMenu(
    ws,
    variable,
    *countries,
    command=display_selected
)

# positioning widget
dropdown.pack(expand=True)

# infinite loop
ws.mainloop()
