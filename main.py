import turtle
import pandas
import pyarrow

screen = turtle.Screen()
screen.title("Quiz Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

user_correct_answer = 0
game_on = True
user_answer = screen.textinput("Guess the state", "Enter the satate")
user_answer.title()
# Extract the states from de csv
data = pandas.read_csv("50_states.csv")

# Get the states in a list
states = data.state.to_list()
# print(states)
num_states = len(states)
states_left = []
while game_on:

  # Check if the user answer is in the list of the states
  if user_answer == "Exit":
    break
  if user_answer in states:
    user_correct_answer += 1
    if user_correct_answer == 50:
      game_on = False
    states_left.append(user_answer)
    states.remove(user_answer)
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

  user_answer = screen.textinput(f"{user_correct_answer} / {num_states}", "Enter the satate").title()

states_csv = {'states': states}
df = pandas.DataFrame(states_csv)
df.to_csv('States_left.csv')
screen.exitonclick()
