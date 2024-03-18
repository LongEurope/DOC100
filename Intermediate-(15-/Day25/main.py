#State quiz
import pandas as pd
import turtle

#General setting
screen = turtle.Screen()
screen.title('U.S. States Game')
image = r'DOC100\Intermediate-(15-\Day25\blank_states_img.gif'


screen.addshape(image)
turtle.shape(image)

data = pd.read_csv(r'DOC100\Intermediate-(15-\Day25\50_states.csv')
all_states = data.state.to_list()
guessed_states = []

#Main loop
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Guessed', prompt='Input a state\'s name.').title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(state_data.state.item())
    elif answer_state == 'Exit':
        break

#Making a csv to learn
states_to_learn = []

for each_state in all_states:
    if each_state not in guessed_states:
        states_to_learn.append(each_state)

new_csv = {
    'States to learn': states_to_learn
}

new_csv = pd.DataFrame(new_csv)
new_csv.to_csv('states_to_learn.csv')