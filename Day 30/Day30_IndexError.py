fruits = ["apple", "pear", "orange"]


def make_pie(index):
    try :
        fruit = fruits[index]
    except IndexError :
        print("Fruit pie")
    else :
        print(fruit + " pie")
        
make_pie(1)


