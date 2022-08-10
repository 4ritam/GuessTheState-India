from turtle import Screen, Turtle

import pandas

screen = Screen()
screen.setup(width=720, height=840)
screen.bgpic("map.gif")
screen.title("States of India")
screen.tracer(0)

dataset = pandas.read_csv("states.csv")
data = dataset.set_index("state")


def add_name(name, x, y):
    t = Turtle()
    t.hideturtle()
    t.up()
    t.goto(x, y)
    t.write(name, font=("ariel", 10, "normal"))


correct_guess = []

while len(correct_guess) < len(dataset.state.to_list()):
    prompt = screen.textinput(
        prompt="Name of the state : ",
        title=f"{len(correct_guess)}/{len(dataset.state.to_list())} guessed"
    ).title()
    if prompt in dataset.state.to_list() and prompt not in correct_guess:
        correct_guess.append(prompt)
        add_name(prompt, data.loc[prompt]["x"], data.loc[prompt]["y"])
        screen.update()

screen.exitonclick()
