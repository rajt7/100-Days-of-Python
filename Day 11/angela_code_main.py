import random

def deal_cards():
    """" Returns random card to user or computer. """
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """" Take a list of cards and return the score calculated from the cards. """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, Opponent has blackjack"
    elif user_score == 0:
        return "Win with a blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    #giving two cards to user as well as computer at the starting of the game
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        #Calculating the score of user and computer
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, Current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        # if user or computer is having blackjack or user's score is greater than 21 then 
        # game is finished.
        # Else ask user to get another card or not.
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    #Once the user is done, it's time to let the computer play. The computer should keep 
    #drawing cards as long as it has score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")

    print(compare(user_score, computer_score))

while input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == 'y':
    play_game()


