from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    print("Failed to load words_to_learn.csv and try french_words.csv")
    df = pandas.read_csv("data/french_words.csv")
    to_learn = df.to_dict(orient="records")
    print(to_learn)

else:
    to_learn = df.to_dict(orient="records")
    print(to_learn)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=front_card_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=english_translation)
    #window.after(3000, func=english_translation)


def english_translation():
    global current_card
    canvas.itemconfig(canvas_image, image=back_card_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def remove_card():
    # to_delete = to_learn.index(current_card)
    # print(f"Deleting the next card {to_delete} {current_card}....")
    # to_learn.pop(to_delete)
    to_learn.remove(current_card)

    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(width=4000, height=4200, padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=front_card_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# Buttons
right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, padx=50, pady=50, command=remove_card)
right_button.grid(column=1, row=1)

wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, padx=50, pady=50, command=next_card)
wrong_button.grid(column=0, row=1)

flip_timer = window.after(3000, func=english_translation)
next_card()


print(flip_timer)
#window.after(3000, func=english_translation)

window.mainloop()
