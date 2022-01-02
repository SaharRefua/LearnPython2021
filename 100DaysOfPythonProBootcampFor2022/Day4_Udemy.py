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
import random
rand= random.randint(0,2)
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("My chose is: \n")
if user_input==0:
    print(rock)
if user_input==1:
    print(paper)
if user_input==2:
    print(scissors)


print("Computer chose: \n")
if rand==0:
    print(rock)
if rand==1:
    print(paper)
if rand==2:
    print(scissors)

if user_input==0 and rand==0:
    print("draw")
elif user_input==0 and rand==1:
    print("You lose")
elif user_input == 0 and rand == 1:
    print("You win")


if user_input==1 and rand == 0:
    print("You win")
elif user_input==1 and rand == 1:
    print("draw")
elif user_input == 1 and rand == 2:
    print("You lose")


if user_input==2 and rand==0:
    print("You lose")
elif user_input==2 and rand==1:
    print("You Win")
elif user_input == 2 and rand == 2:
    print("draw")
