import turtle
import pandas


def get_mouse_click_cor(x, y):
    print(x, y)


def move_state(state_found_param, answer_state_param):
    state_name = turtle.Turtle()
    state_name.penup()
    state_name.hideturtle()
    state_name.goto(int(state_found_param["x"]), int(state_found_param["y"]))
    state_name.write(answer_state_param)

    # state_name.goto(state_found_param["x"], state_found_param["y"])


screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_count = 0
number_of_states_in_csv = len(data)
correct_answers = []
while states_count <= number_of_states_in_csv:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/{number_of_states_in_csv} correct", prompt="What's another state's name")
    answer_state = answer_state.title()
    state_found = data[data.state == answer_state]
    if len(state_found) > 0 and answer_state not in correct_answers:
        correct_answers.append(answer_state)
        move_state(state_found, answer_state)
    states_count += 1

    print(correct_answers)

turtle.onscreenclick(get_mouse_click_cor)
turtle.mainloop()

# screen.exitonclick()
