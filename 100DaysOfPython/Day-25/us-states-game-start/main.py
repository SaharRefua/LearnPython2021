import turtle
import pandas
data = pandas.read_csv("50_states.csv")
states = data.state
print(data)
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
guessed_states = []
turtle.addshape(image)
turtle.shape(image)
correct_guesses = 0
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
# user_not_guess = []
still_guessing = True
while still_guessing:
    answer_state = screen.textinput(title=f"{correct_guesses}/50 Guess the State", prompt="What's another state's name").title()
    if answer_state == "Exit":
        # for state in states:
        #     if state not in guessed_states:
        #         user_not_guess.append(state)
        # print(user_not_guess)
        user_not_guess = [state for state in states if state not in guessed_states]
        not_guess_data=pandas.DataFrame(user_not_guess)
        not_guess_data.to_csv("states_to_learn.csv")
        break
    for state in states:
        if answer_state.lower() == str(state).lower():
            row = data[data.state == state]
            if state not in guessed_states:
                guessed_states.append(state)
                correct_guesses += 1
                state_name = str(state)
                writer.goto(int(row.x),int(row.y) )
                writer.write(row.state.item(), True)

    if correct_guesses == 50:
        still_guessing = False

#screen.exitonclick()