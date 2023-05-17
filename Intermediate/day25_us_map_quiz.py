import turtle
import pandas
screen = turtle.Screen()
screen.title("US game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_on = True
data = pandas.read_csv("50_states.csv")
data["state_lower"] = data["state"].str.lower()
user_state = []
while game_on:
    answer_state = screen.textinput(title = "Guess the State", prompt="Enter the state name")
    answer_state = answer_state.lower()
    states_to_learn = []
    if len(data[data.state_lower == answer_state])> 0:
        state_entered = data[data.state_lower  == answer_state].state
        print(state_entered)
        x_coord = float(data.x[data.state_lower == answer_state])
        y_coord = float(data.y[data.state_lower == answer_state])
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(x_coord, y_coord)
        tim.write(arg = f"{state_entered.item()}")
        user_state.append(state_entered.item())
    print(f"USER_STATES: {user_state}")
    if answer_state == "exit":
        for state in data.state.to_list():
            print(f"STATE: {state}")
            if state not in user_state:
                states_to_learn.append(state)
                df = pandas.DataFrame(states_to_learn)
                print(len(df))
                df.to_csv("states_to_learn.csv")
        break
