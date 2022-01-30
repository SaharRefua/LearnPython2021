# # Review:
# # Create a function called greet().
# # Write 3 print statements inside the function.
# # Call the greet() function and run your code.
# def greet():
#   print("\nGood Moring Sahar")
#   print("le't learn python")
#   print("Do you need any Coffee break?")
#
# greet()
#
# def greet_with_name(name):
#   print(f"\nGood Morning {name}")
#   print(f"le't learn python {name}")
#   print(f"Do you need any Coffee break? {name}")
#
# greet_with_name("Yoav")
#
#
#
# def greet_with_name_and_loaction(name,location):
#   print(f"\nGood Morning {name}")
#   print(f"What is the weather in {location} ? ")
#   print(f"Do you need any Coffee break? {name}")
#
# greet_with_name_and_loaction("Rea","Tel Aviv")
#
# greet_with_name_and_loaction(location = "Tel Aviv" ,name="Rea" )
#
#
# #Write your code below this line 👇
# import math
#
# def paint_calc(height,width,cover):
#   result = (height * width ) / cover
#   num_of_cans = math.ceil(result)
#   print(f"you'll need {num_of_cans} cans of paint ")
# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


# Write your code below this line 👇
#
# def prime_checker(number):
#   is_prime = True
#   for i in range(2, number):
#     if number % i == 0:
#       is_prime = False
#   if is_prime:
#     print("It's a prime number.")
#   else:
#     print("It's not a prime number.")
# # Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)



#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(user_message, user_shift):
#   encode_message=""
#   for letter in user_message:
#     char_location = alphabet.index(letter)
#     new_index = user_shift + char_location
#     encode_message += alphabet[new_index]
#   print(encode_message)
#     # Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#     #e.g.
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"
#
#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
#
#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
# if direction=="encode":
#   encrypt(text,shift)
# else:
#   print("you type the wrong type please try again later !")
# #Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# #Combine the encrypt() and decrypt() functions into a single function called caesar().
# def caesar(plain_text, shift_amount, direction):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     if direction=="encode":
#       new_position = position + shift_amount
#       #cipher_text += alphabet[new_position]
#     elif direction=="decode":
#       new_position = position - shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The {direction} text is {cipher_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    # What happens if the user enters a number/symbol/space?
    # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    # e.g. start_text = "meet me at 3"
    # end_text = "•••• •• •• 3"
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")


# Import and print the logo from art.py when the program starts.
from decode_art import logo

print(logo)

# Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  # What if the user enters a shift that is greater than the number of letters in the alphabet?
  # Try running the program and entering a shift number of 45.
  # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
  # Hint: Think about how you can use the modulus (%).
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")



