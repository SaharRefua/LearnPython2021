# variables
# First run the input function
# Second run the print function with value from input function

# print("Hello " + input("Please enter your name: ") +" !")

# Write your code below this line 👇
# print( len(input("What is your name?")))

# ####################################
# # 🚨 Don't change the code below 👇
# a = input("a: ")
# b = input("b: ")
# # 🚨 Don't change the code above 👆
#
# ####################################
# # Write your code below this line 👇
#
# temp=a
# a=b
# b=temp
#
# # Write your code above this line 👆
# ####################################
#
# # 🚨 Don't change the code below 👇
# print("a: " + a)
# print("b: " + b)



# ####################################
# #1. Create a greeting for your program.
#
# #2. Ask the user for the city that they grew up in.
# city_name=input("Please enter the city that they grew up in: \n")
# #3. Ask the user for the name of a pet.
# pet_name=input("Please enter the name of your pet: \n")
# #4. Combine the name of their city and pet and show them their band name.
# print(city_name+ " "+ pet_name)
# #5. Make sure the input cursor shows on a new line, see the example at:
# #   https://replit.com/@appbrewery/band-name-generator-end

# 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆
# #results = float (weight) / (float (height) * float (height) )
# results = float (weight) / float (height) **2
# #Write your code below this line 👇
# print(str(results))
#
#
# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# bmi=round(weight / height ** 2)
#
# if bmi<18.5:
#     print(f"Your BMI is {bmi}, you are underweight")
# elif bmi<25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi<30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi<35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")



#Write your code below this line 👇

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Not leap year.")
else:
    print("Not leap year.")