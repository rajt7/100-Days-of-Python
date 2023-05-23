import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# should_continue = True

user_cards = random.sample(cards, 2)
computer_cards = random.sample(cards, 1)

print(f"Your Cards: {user_cards}, Current Score: {sum(user_cards)}")
print(f"Computer's first card: {computer_cards}")

def draw_next_card():
    user_appended = random.sample(cards, 1)
    for i in user_appended:
        user_cards.append(i)
    user_card_sum = sum(user_cards)
    print(f"Your Cards: {user_cards}, Current Score: {user_card_sum}")
    print(f"Computer's first card: {computer_cards}")
    if sum(user_cards) > 21:
        dealers_card()
        print("You Lose...")
    elif sum(user_cards) == 21:
        print("You win...")
    else:
        next_round()

def next_round():
    if sum(user_cards) == 21:
        dealers_card()
        print("You win...")
    if input("Type 'y' to get another round, type 'n' to pass: ") == 'y':
        draw_next_card()
    else:
        dealers_card()
        if (sum(user_cards) < 21) and (sum(computer_cards) < 21):
            if sum(user_cards) > sum(computer_cards):
                print("You Win...")
            elif sum(user_cards) == sum(computer_cards):
                print("Current bet is draw...")
            else:
                print("You Lose...")
        elif (sum(user_cards) > 21) and (sum(computer_cards) > 21):
            print("You Lose...")
        elif (sum(user_cards) < 21) and (sum(computer_cards) > 21):
            print("You Lose...")
        elif (sum(user_cards) > 21) and (sum(computer_cards) < 21):
            print("You Lose...")

def dealers_card():
    counter = len(user_cards) - 1
    computer_appended = random.sample(cards, counter)
    for i in computer_appended:
        computer_cards.append(i)
    print(f"Your final hand: {user_cards}")
    print(f"Computer's final hand: {computer_cards}")


next_round()