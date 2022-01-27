#Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
all_names = []


def get_all_names():
    with open("Input/Names/invited_names.txt") as names:
        all_names = names.readlines()
        return  all_names


def get_letter_text():
    with open("./Input/Letters/starting_letter.txt") as letter:
        let = letter.read() #"".join(letter.readlines())
    return let


def create_all_letters(names, text):
    for name in names:
        new_name = name.strip("\n")
        print(new_name)
        new_file=f"./Output/ReadyToSend/letter_for_{new_name}.txt"
        with open(new_file,"w")as new_letter:
            new_letter.write(text.replace("[name]", new_name))


letter = get_letter_text()
all_names = get_all_names()
#print(all_names)

create_all_letters(all_names ,letter)


#
# PLACEHOLDER = "[name]"
#
#
# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()
#
# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_letter)


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp