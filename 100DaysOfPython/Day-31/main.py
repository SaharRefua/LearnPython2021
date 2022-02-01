from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"


def right_answer():
    print("right button was clicked")


def wrong_answer():
    print("wrong button was clicked")


window = Tk()
window.title("Flashy")
window.config(width=1000, height=1200, padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=400, height=212)
front_card_image = PhotoImage(file="images/card_front.png")
canvas.create_image(100, 100, image=front_card_image)
canvas.grid(column=1, row=0, columnspan=2)

right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, padx=50, pady=50, command=right_answer)
right_button.grid(column=2, row=1)

wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, padx=50, pady=50, command=wrong_answer)
wrong_button.grid(column=1, row=1)

window.mainloop()
