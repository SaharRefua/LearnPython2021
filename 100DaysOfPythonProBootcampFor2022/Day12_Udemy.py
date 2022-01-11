#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

logo = """


   _____                                  _   _                 _                
  / ____|                         /\     | \ | |               | |               
 | |  __ _   _  ___  ___ ___     /  \    |  \| |_   _ _ __ ___ | |__   ___ _ __  
 | | |_ | | | |/ _ \/ __/ __|   / /\ \   | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| 
 | |__| | |_| |  __/\__ \__ \  / ____ \  | |\  | |_| | | | | | | |_) |  __/ |    
  \_____|\__,_|\___||___/___/ /_/    \_\ |_| \_|\__,_|_| |_| |_|_.__/ \___|_|    
                                                                                 
                                                                                 



"""
import random as rd

HARD = 5
EASY = 10
print(logo)
number = rd.randint(1 , 100)
still_guessing = True
print("Welcome to the Number Guessing Game!")
print("I'm thinking on a number between 1 and 100 ")

def set_difficulty():
    difficulty = input("Choose a difficulty Hard or Easy:").lower()
    if difficulty == "easy":
        return EASY
    elif difficulty == "hard":
        return  HARD


user_total_guess=set_difficulty()


while still_guessing:
    user_guess = int(input("Make a guess: "))
    if user_guess == number:
        print(f"You right , the number is {number}")
        still_guessing = False
    elif user_guess > number and user_total_guess > 1:
        print("Too high.\nGuess again.")
        user_total_guess -= 1
        print(f"User total guess remaining is {user_total_guess}")
    elif user_guess < number and user_total_guess > 1:
        print("Too low.\nGuess again.")
        user_total_guess -= 1
        print(f"User total guess remaining is {user_total_guess}")
    elif user_total_guess == 1:
        print(f"You run out the guess You lose , the number is {number}")
        still_guessing = False








# from random import randint
# from art import logo
#
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5
#
# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")
#
# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS
#
# def game():
#   print(logo)
#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}")
#
#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")
#
#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))
#
#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")
#
#
# game()

