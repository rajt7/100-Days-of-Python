from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Who will win the race? Enter a color: ")
colors = ["red", "blue", "yellow", "green", "purple", "orange"]
turtles = ["urvish", "raj", "kishan", "dharmik", "hemanshi", "dj"]
x, y = -230, -100

for i in range(6):
    turtles[i] = Turtle(shape='turtle')
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x, y)
    y += 40

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
