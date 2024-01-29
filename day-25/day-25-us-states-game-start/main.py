from turtle import Turtle, Screen
import pandas

screen = Screen()
turtle = Turtle()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []
states_file = pandas.read_csv("50_states.csv")
all_state = states_file["state"].to_list()


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50 States Correct", prompt="What's another state's name").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_state if state not in guessed_states]

        data = pandas.DataFrame(missing_states)
        data.to_csv("missing_states.csv")
        break
    if answer_state in all_state:
        guessed_states.append(answer_state)
        fresh_state = states_file[states_file['state'] == answer_state]
        t = Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(fresh_state.x.iloc[0]), int(fresh_state.y.iloc[0]))
        t.write(answer_state)







