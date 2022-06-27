import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S. State Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Aflarea coordonatelor tuturor statelor, atunci cand apas pe ele
#Pe urma am logat trecut in fisierul 50_states.csv toate statele cu coordonatele
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data=pandas.read_csv("50_states.csv")
states=data.state.to_list()

guessed_states=[]

while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States ", prompt="What's another state's name?")
    #Convert the guess to title
    new_answer=answer_state.title()
    if new_answer == "Exit":
        missing_states=[state for state in states if state not in guessed_states]
        # for state in states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    #Check if the guess is among the 50 states
    if new_answer in states:
        if new_answer not in guessed_states:
            guessed_states.append(new_answer)
            t=turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data=data[data.state == new_answer]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(new_answer)
        else:
            pass

#states to learn.csv
