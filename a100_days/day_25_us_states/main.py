import turtle
import pandas
from a100_days.day_25_us_states.state_title import StateTitle


def load_csv(name):
    data = pandas.read_csv(name)
    print(data[data.state == "Texas"])


def start():
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)

    turtle.shape(image)

    guessed_states = []

    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()

    while len(guessed_states) < 50:
        # answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                        prompt="What's another state's name?").title()
        if answer_state in all_states and answer_state not in guessed_states:
            state_data = data[data.state == answer_state]
            state_name = state_data.state.item()
            state_x = int(state_data.x)
            state_y = int(state_data.y)
            StateTitle(state_name, state_x, state_y)

            guessed_states.append(answer_state)
        elif answer_state == "exit".title():
            missed_states = [state for state in all_states if state not in guessed_states]
#           missed_states = data[~data.state.isin(guessed_states)]
            new_data = pandas.DataFrame(missed_states)
            new_data.to_csv("learn.csv")
            break


if __name__ == "__main__":
    start()
