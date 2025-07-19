import turtle
from turtle import Turtle,Screen
import pandas

screen = Screen()
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")
data = pandas.read_csv("50_states.csv")
states_guessed = 0
guessed_states = []
turtle.penup()
turtle.hideturtle()
while states_guessed < 50:
    user_answer = screen.textinput(prompt="Guess a state", title=f"States Guessed: {states_guessed}/50").title()
    if user_answer == "Exit":
        break
    for states in data["state"]:
        if user_answer == states and user_answer not in guessed_states:
            print(states)
            guessed_states.append(user_answer)
            states_guessed += 1
            _x = data[data["state"] == states]["x"].item()
            _y = data[data["state"] == states].y.item()
            turtle.goto(_x, _y)
            turtle.write(user_answer)

not_guessed = []
for state in data["state"]:
    if state not in guessed_states:
        not_guessed.append(state)

not_guessed_states = {
    "states": not_guessed
}
data_states = pandas.DataFrame(not_guessed_states)
data_states.to_csv("a.csv")

screen.exitonclick()