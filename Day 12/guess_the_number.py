#Guess the Number Game

from random import randint

print("Welcome to the Guess the Number Game!!!")

#Choose the number between 1 to 100
print("I am thinking of a number from 1 to 100.")
guess_number = randint(1, 100)

#Let the user decide the difficulty level
difficulty = input("Choose a difficulty. Take 'easy' or 'hard': ")

#If user selects 'easy' then he/she has 10 attempts to guess the number and 
#if user selects 'hard' then he/she has 5 attempts to guess the number.
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    print("Select from easy or hard.")


#Comparing the user number and computer's guess. If user has guess higher value than
#show too high or if user guess lower value than show too low. User wins as soon as
#he/she guesses correctly.
continue_game = True

while continue_game:
    print(f"You have {attempts} attempts remaining.")
    user_guess = int(input("Make a guess: "))
    attempts = attempts - 1
    if attempts <= 0:
        continue_game = False
        print("Oops.. Game Over!!")
    elif user_guess == guess_number:
        print("You have guessed right.")
        print("Hurray! You won.")
        continue_game = False
    elif user_guess < guess_number:
        print("Too low")
    elif user_guess > guess_number:
        print("Too high")