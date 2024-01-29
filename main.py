import turtle
import pandas
import pyarrow

screen = turtle.Screen()
screen.title("Quiz Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_on = True
while game_on:
  user_answer = screen.textinput("Guess the state", "Enter the satate")

  # Extract the states from de csv
  data = pandas.read_csv("50_states.csv")

  # Get the states in a list
  states = data.state.to_list()
  # print(states)

  # Check if the user answer is in the list of the states
  if user_answer in states:
    # print("There is")
    # Print in the coords
    # print(data[data.state == user_answer])
    coord_data = data[data.state == user_answer]
    # print(coord_data)
    # Get the x and y values
    x_coord = coord_data.x.item()
    # print(x_coord)
    y_coord = coord_data.y.item()

    item_state = turtle.Turtle()
    item_state.hideturtle()
    item_state.penup()
    item_state.goto(x_coord, y_coord)
    item_state.write(f"{user_answer}", align="center", font=("Courier", 9, "normal"))

screen.exitonclick()
