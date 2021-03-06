from tkinter import *  # import all classes
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website_value=website_input.get()
    try:
        with open("data.json", "r")as data_file:
            data = json.load(data_file)
            if website_value in data:
                password_value = data[website_value]["password"]
                email_value =  data[website_value]["email"]
                messagebox.showinfo(title=website_value, message=f"Email: {email_value}\nPassword: {password_value}\n")
            else:
                messagebox.showerror(title="Error", message="No details for the website exists.")
    except KeyError as error:
            messagebox.showerror(title="Error",message=f"Key Error: {error}")

    except FileNotFoundError:
        messagebox.showerror(title="Error",message="No Data File Found.")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = randint(8, 10)
    # nr_symbols = randint(2, 4)
    # nr_numbers = randint(2, 4)

    # password_list = []
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    shuffle(password_list)
    password= "".join(password_list)
    # password = ""
    # for char in password_list:
    #     password += char

    print(f"Your password is: {password}")
    if password_input.get() == "":
        password_input.insert(0, password)
    else:
        password_input.delete(0, END)
        password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email_username_value = email_username_input.get()
    password_value = password_input.get()
    website_value = website_input.get()
    new_data = {
        website_value: {
            "email": email_username_value,
            "password": password_value,
        }
    }



    if len(password_value) == 0 or len(website_value) == 0:
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # FYI convert the json data to python dictionaries
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating  old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            password_input.delete(0, END)
            website_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries:
website_input = Entry(width=32)
website_input.grid(column=1, row=1)
website_input.focus()

email_username_input = Entry(width=51)
email_username_input.grid(column=1, row=2, columnspan=3)
email_username_input.insert(END, "my_email@gmail.com")

password_input = Entry(width=32)
password_input.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password, width=14)
generate_password_button.grid(column=2, row=3)

search_button = Button(text="Search", command=find_password, width=14)
search_button.grid(column=2, row=1)


add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

# example of 'columnspan' in grid


# from tkinter import *
#
# window = Tk()
#
# r = Label(bg="red", width=20, height=5)
# r.grid(row=0, column=0)
#
# g = Label(bg="green", width=20, height=5)
# g.grid(row=1, column=1)
#
# b = Label(bg="blue", width=40, height=5)
# b.grid(row=2, column=0, columnspan=2)
#
#
# window.mainloop()
