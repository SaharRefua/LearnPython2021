import turtle
import pandas
data = pandas.read_csv("50_states.csv")
states = data.state
print(data)
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
correct_guesses = 0

still_guessing = True
while still_guessing:    #for guess in range(0,50):

    answer_state = screen.textinput(title=f"{correct_guesses}/50 Guess the State", prompt="What's another state's name")
    for state in states:
        #print(state)
        if answer_state.lower() == str(state).lower():
            row = data[data.state == state]
            correct_guesses += 1
            #print(row)
            #print(type(row))
            #turtle.goto(int(row.x),int(row.y) )
            state_name = str(state)
            #turtle.write(state_name, False, align="center")
            turtle.write((0, 0), True)
            #print(f"X:{row[1]} and y:{row[2]}" )

    if correct_guesses == 50:
        still_guessing = False










screen.exitonclick()