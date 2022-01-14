from art_day14 import logo, vs
from game_data import data
import random

print(logo)

user_choose_correct_answer = True
number_of_correct_answers = 0

def genert_2_option(first_option ):
    print(f"Compare A: {first_option.get('name')} ,{first_option.get('description')} from {first_option.get('country')}  followers:{first_option.get('follower_count')}")
    print(vs)
    second_option = random.choice(data)
    if second_option == first_option:
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


