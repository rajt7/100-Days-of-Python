# Create the data
from data import data
import random

# Create a function to compare follower counts
def calculate_answer(dict_a, dict_b):
    """ Takes two dictionaries and returns 'A' if first dictionary has higher value than
    second dictionary else return 'B'."""
    if dict_a['follower_count'] >= dict_b['follower_count']:
        return 'A'
    else:
        return 'B'

# Create a function to check the answer
def check_answer(original_answer, user_answer):
    if original_answer == user_answer:
        return True
    else:
        return False

# Get random items from data.
value_1 = random.choice(data)

continue_game = True
score = 0

while continue_game:
    value_2 = random.choice(data)

    original_answer = calculate_answer(value_1, value_2)

    print(f"Compare A: {value_1['name']}, a {value_1['description']}, from {value_1['country']}")
    print(f"Against B: {value_2['name']}, a {value_2['description']}, from {value_2['country']}")

    user_answer = input("Who has more followers? Type 'A' or 'B': ")
    answer = check_answer(original_answer, user_answer)

    if answer == False:
        print(f"Oops.. You are wrong. Your score is {score}.")
        continue_game = False
    else:
        score = score + 1
        if user_answer == 'A':
            value_1 = value_2
        print(f"You're right. Current score: {score}.")
        print("----------------------------------------------------------------")