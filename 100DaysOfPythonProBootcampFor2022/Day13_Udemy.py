############DEBUGGING#####################

# Describe Problem
def my_function():
  for i in range(1, 21): # TODO - update the range to 1,21
    if i == 20:
      print("You got it")
my_function()

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)#TODO update randint range to 0 ,5
print(dice_imgs[dice_num])

# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:#TODO add '=' to the elif
  print("You are a Gen Z.")

# Fix the Errors
age = int(input("How old are you?"))#TODO add int func to input in oder to convert it to integer
if age > 18:
  print(f"You can drive at age {age}.")#TODO add f in order to change in to f string

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) # TODO remove on '=' so the input will save the value to word_per_page
total_words = pages * word_per_page
print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)#TODO and one spec to line 41 in order to add it to the for loop
  print(b_list)

mutate([1,2,3,5,8,13])