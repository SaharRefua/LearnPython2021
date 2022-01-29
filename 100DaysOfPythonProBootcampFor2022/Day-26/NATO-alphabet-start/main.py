student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # print(key)
    # print(value)
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(row)
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas
# 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(df)
letter_code = {code.letter: code.code for (index, code) in df.iterrows()}
print(letter_code)
#2. Create a list of the phonetic code words from a word that the user inputs.

user_name = input("Enter your name: ").upper()
result2 = [letter_code[letter] for letter in user_name]
print(result2)

