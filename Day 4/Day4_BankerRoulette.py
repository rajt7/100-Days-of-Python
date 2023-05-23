import random

names_String = input("Give me everybody's names, separated by a comma: ")
names = names_String.split(", ")
# print(names)

random_name = names[random.randint(0, len(names) - 1)]
print(f"{random_name} is going to buy the meal today.")