# Create new list which increments each item from previous list by 1
# List Comprehension
numbers = [1, 2, 3, 4, 5]
# new_numbers = [new_item for item_in_old_list in list]
new_numbers = [item+1 for item in numbers]

print(new_numbers)


name = "Angela"
new_list = [letter for letter in name ]

print(new_list)

# numbers = range(1,5)
# print(numbers)

numbers_multiply = [n * 2 for n in range(1,5)]
print(numbers_multiply)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) <5 ]
print(short_names)
new_names = [name.upper() for name in names if len(name) >5 ]
print(new_names)
import random
students_scores = {student:random.randint(1,100) for student in names }

print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score >= 60 }
print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

words = {word:len(word) for word in sentence.split() }
print(words)


