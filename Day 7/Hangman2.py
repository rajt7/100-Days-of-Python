import random

word_list = ['pushpa', 'conda', 'keshav']

#choose the random word from list and assign it to a variable called word_chosen
word_chosen = random.choice(word_list)
print(word_chosen)

#creating a blank list
blank_list = []
for i in range(0, len(word_chosen)):
    blank_list.append('_')
print(blank_list)

end_of_game = False
while not end_of_game:
    #Ask the user to guess a letter and make it to lower case.
    guess = input('Guess a letter: ').lower()

    #replacing blank list
    count = 0
    for letter in word_chosen:
        if guess == letter:
            blank_list[count] = letter
        count = count + 1

    print(blank_list)

    if '_' not in blank_list:
        end_of_game = True
        print('You win.')