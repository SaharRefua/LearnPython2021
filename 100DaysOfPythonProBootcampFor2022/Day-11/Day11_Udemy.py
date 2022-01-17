############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
from builtins import complex

from art_blackjack import logo
import random
from replit import clear

from termcolor import colored


still_playing = True
still_valid_cards=True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards=[]
computer_cards=[]

def get_another_card():
    new_card = random.choice(cards)
    return new_card
def cards_sum(cards_list):
    total_sum = 0
    for card in cards_list:
        total_sum += card
    return total_sum

def check_for_ace(cards_list):
    there_is_ace_in_the_list=False
    for card in cards_list:
        if card == 11:
            cards_list[cards_list.index(card)]=1
            there_is_ace_in_the_list=True
    return there_is_ace_in_the_list

def check_cards():
    if cards_sum(computer_cards) == 21:
        still_valid_cards = False
        #print(colored("Your lose = (", 'red'))
        return still_valid_cards
    if cards_sum(user_cards) == 21:
        still_valid_cards = False
        #print(colored("Your win = )", 'green'))
        return still_valid_cards
    if cards_sum(user_cards) > 21:
        if check_for_ace(user_cards):
            check_cards()
        else:
            still_valid_cards=False
            print(colored("you over went , you lose", 'red'))
            return still_valid_cards
    if cards_sum(computer_cards) > 21:
        if check_for_ace(computer_cards):
            check_cards()
        else:
            still_valid_cards = False
            print(colored("Computer is over went , you win", 'green'))
            return still_valid_cards

    elif cards_sum(computer_cards) < 17:
        print(colored("\nComputer get another card!!!!!!", 'yellow'))
        computer_cards.append(get_another_card())
        check_cards()

def check_who_win():
        if cards_sum(user_cards) > cards_sum(computer_cards):
            print(colored("Your win = )", 'green'))
            return
        elif cards_sum(user_cards) == cards_sum(computer_cards):
            print(colored("Is a draw !", 'yellow'))
            return
        else:
            print(colored("Your lose = (", 'red'))
            return

def blackjack():
    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    print(f"Your cards: {user_cards} Current score: {cards_sum(user_cards)}")

    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    print(f"Computer First card: {computer_cards[0]}")
    check_cards()

    while still_valid_cards:
        if still_valid_cards and input("Type 'y' to get another card or 'n' to pass ").lower() == 'y':
            user_cards.append(get_another_card())
            results = check_cards()
            print(f"Your cards: {user_cards} Current score: {cards_sum(user_cards)}")
            print(f"Computer First card: {computer_cards[0]}")
            if results==False:
                # check_cards()1
                # still_valid_cards = False
                print(f"Your final hand: {user_cards} ,final score :{cards_sum(user_cards)}  ")
                print(f"Computer final hand: {computer_cards} ,final score :{cards_sum(computer_cards)}  ")
                break

        else:
            check_who_win()
            print(f"Your final hand: {user_cards} ,final score :{cards_sum(user_cards)}  ")
            print(f"Computer final hand: {computer_cards} ,final score :{cards_sum(computer_cards)}  ")
            break
while still_playing:
    if input("Do you want to play a game of Blackjack ? type 'y' or 'n'").lower() == 'y':
        clear()
        print(colored(logo , 'green'))
        user_cards = []
        computer_cards = []
        blackjack()
    else:
        still_playing = False
        print(colored("See you next time!", 'yellow'))


##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
# ############### Blackjack Project #####################

# #Difficulty Normal 😎: Use all Hints below to complete the project.
# #Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# #Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# #Difficulty Expert 🤯: Only use Hint 1 to complete the project.

# ############### Our Blackjack House Rules #####################

# ## The deck is unlimited in size.
# ## There are no jokers.
# ## The Jack/Queen/King all count as 10.
# ## The the Ace can count as 11 or 1.
# ## Use the following list as the deck of cards:
# ## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# ## The cards in the list have equal probability of being drawn.
# ## Cards are not removed from the deck as they are drawn.

# ##################### Hints #####################

# #Hint 1: Go to this website and try out the Blackjack game:
# #   https://games.washingtonpost.com/games/blackjack/
# #Then try out the completed Blackjack project here:
# #   http://blackjack-final.appbrewery.repl.run

# #Hint 2: Read this breakdown of program requirements:
# #   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# #Then try to create your own flowchart for the program.

# #Hint 3: Download and read this flow chart I've created:
# #   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# #Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# #11 is the Ace.
# import random
# from replit import clear
# from art import logo

# def deal_card():
#   """Returns a random card from the deck."""
#   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#   card = random.choice(cards)
#   return card

# #Hint 6: Create a function called calculate_score() that takes a List of cards as input
# #and returns the score.
# #Look up the sum() function to help you do this.
# def calculate_score(cards):
#   """Take a list of cards and return the score calculated from the cards"""

#   #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
#   if sum(cards) == 21 and len(cards) == 2:
#     return 0
#   #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
#   if 11 in cards and sum(cards) > 21:
#     cards.remove(11)
#     cards.append(1)
#   return sum(cards)

# #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
# def compare(user_score, computer_score):
#   #Bug fix. If you and the computer are both over, you lose.
#   if user_score > 21 and computer_score > 21:
#     return "You went over. You lose 😤"


#   if user_score == computer_score:
#     return "Draw 🙃"
#   elif computer_score == 0:
#     return "Lose, opponent has Blackjack 😱"
#   elif user_score == 0:
#     return "Win with a Blackjack 😎"
#   elif user_score > 21:
#     return "You went over. You lose 😭"
#   elif computer_score > 21:
#     return "Opponent went over. You win 😁"
#   elif user_score > computer_score:
#     return "You win 😃"
#   else:
#     return "You lose 😤"

# def play_game():

#   print(logo)

#   #Hint 5: Deal the user and computer 2 cards each using deal_card()
#   user_cards = []
#   computer_cards = []
#   is_game_over = False

#   for _ in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())

#   #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#   while not is_game_over:
#     #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
#     user_score = calculate_score(user_cards)
#     computer_score = calculate_score(computer_cards)
#     print(f"   Your cards: {user_cards}, current score: {user_score}")
#     print(f"   Computer's first card: {computer_cards[0]}")

#     if user_score == 0 or computer_score == 0 or user_score > 21:
#       is_game_over = True
#     else:
#       #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
#       user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#       if user_should_deal == "y":
#         user_cards.append(deal_card())
#       else:
#         is_game_over = True

#   #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
#   while computer_score != 0 and computer_score < 17:
#     computer_cards.append(deal_card())
#     computer_score = calculate_score(computer_cards)

#   print(f"   Your final hand: {user_cards}, final score: {user_score}")
#   print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
#   print(compare(user_score, computer_score))

# #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#   clear()
#   play_game()
