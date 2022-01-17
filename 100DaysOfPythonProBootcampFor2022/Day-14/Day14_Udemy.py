from art_day14 import logo, vs
from game_data import data
import random

print(logo)

user_choose_correct_answer = True
number_of_correct_answers = 0
second_option = random.choice(data)


def genert_2_option(first_option ):
    print(f"Compare A: {first_option.get('name')} ,{first_option.get('description')} from {first_option.get('country')}  followers:{first_option.get('follower_count')}")
    print(vs)
    second_option = random.choice(data)
    while second_option == first_option:
        second_option = random.choice(data)
    print(f"Against B: {second_option.get('name')} ,{second_option.get('description')} from {second_option.get('country')} followers: {second_option.get('follower_count')} ")
    first_followers = first_option.get('follower_count')
    second_followers = second_option.get('follower_count')
    user_choice = str(input("Who has more followers Type A or B: "))
    if first_followers > second_followers and user_choice == "A":
        return True
    elif first_followers < second_followers and user_choice == "B":

        return True
    else:
        return False


while user_choose_correct_answer:
    if number_of_correct_answers == 0:
        first_option = random.choice(data)
    # Add one in case the user right or end the game in case the user wrong
    if not genert_2_option(first_option):
        user_choose_correct_answer = False
        print(f"\nSorry that's was wrong. Final score {number_of_correct_answers}")

    else:
        number_of_correct_answers += 1
        print(f"\nyou're right! Correct score:{number_of_correct_answers}")
#
# from game_data import data
# import random
# from art import logo, vs
# from replit import clear
#
#
# def get_random_account():
#     """Get data from random account"""
#     return random.choice(data)
#
#
# def format_data(account):
#     """Format account into printable format: name, description and country"""
#     name = account["name"]
#     description = account["description"]
#     country = account["country"]
#     # print(f'{name}: {account["follower_count"]}')
#     return f"{name}, a {description}, from {country}"
#
#
# def check_answer(guess, a_followers, b_followers):
#     """Checks followers against user's guess
#     and returns True if they got it right.
#     Or False if they got it wrong."""
#     if a_followers > b_followers:
#         return guess == "a"
#     else:
#         return guess == "b"
#
#
# def game():
#     print(logo)
#     score = 0
#     game_should_continue = True
#     account_a = get_random_account()
#     account_b = get_random_account()
#
#     while game_should_continue:
#         account_a = account_b
#         account_b = get_random_account()
#
#         while account_a == account_b:
#             account_b = get_random_account()
#
#         print(f"Compare A: {format_data(account_a)}.")
#         print(vs)
#         print(f"Against B: {format_data(account_b)}.")
#
#         guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#         a_follower_count = account_a["follower_count"]
#         b_follower_count = account_b["follower_count"]
#         is_correct = check_answer(guess, a_follower_count, b_follower_count)
#
#         clear()
#         print(logo)
#         if is_correct:
#             score += 1
#             print(f"You're right! Current score: {score}.")
#         else:
#             game_should_continue = False
#             print(f"Sorry, that's wrong. Final score: {score}")
#
#
# game()
#
# '''
#
# FAQ: Why does choice B always become choice A in every round, even when A had more followers?
#
# Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. Hope that makes sense :-)
#
# '''

# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.