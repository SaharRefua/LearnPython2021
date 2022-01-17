# random and lists

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random as random
computer_choise = random.randint(0,2)
user_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print("My chose is: \n")
# if user_choise == 0:
#     print(rock)
# if user_choise == 1:
#     print(paper)
# if user_choise == 2:
#     print(scissors)

# print("Computer chose: \n")
# if computer_choise == 0:
#     print(rock)
# if computer_choise == 1:
#     print(paper)
# if computer_choise == 2:
#     print(scissors)

game_images=[rock , paper , scissors]

if user_choise >= 3 or user_choise < 0:
    print("you type invalid number ")
else:
    print(game_images[user_choise])
    print("computer chose: \n")
    print(game_images[user_choise])

if user_choise == 0 and computer_choise == 2:
    print("You win!")
elif user_choise == 2 and computer_choise == 0:
    print("You lose")
elif user_choise > computer_choise:
    print("You lose")
elif user_choise < computer_choise:
    print("You Win")

elif user_choise == computer_choise:
    print("It's a draw")

#
# if user_input==0 and rand==0:
#     print("draw")
# elif user_input==0 and rand==1:
#     print("You lose")
# elif user_input == 0 and rand == 1:
#     print("You win")
#
#
# if user_input==1 and rand == 0:
#     print("You win")
# elif user_input==1 and rand == 1:
#     print("draw")
# elif user_input == 1 and rand == 2:
#     print("You lose")
#
# if user_input==2 and rand==0:
#     print("You lose")
# elif user_input==2 and rand==1:
#     print("You Win")
# elif user_input == 2 and rand == 2:
#     print("draw")
