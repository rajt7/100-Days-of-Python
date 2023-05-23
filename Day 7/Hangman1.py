import random

word_list = ['pushpa', 'conda', 'keshav']

#choose the random word from list and assign it to a variable called word_chosen
word_chosen = random.choice(word_list)

#Ask the user to guess a letter and make it to lower case.
guess = input('Guess a letter: ').lower()

#check the guessed letter with the chosen word letters
for letter in word_chosen :
    if guess == letter :
        print('Right')
    else :
        print('Wrong')