import turtle
import pandas
import pyarrow

screen = turtle.Screen()
screen.title("Quiz Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
user_answer = screen.textinput("Guess the state", "Enter the satate")

# Extract the states from de csv
data = pandas.read_csv("50_states.csv")

# Get the states in a list
states = data.state.to_list()
print(states)


screen.exitonclick()
