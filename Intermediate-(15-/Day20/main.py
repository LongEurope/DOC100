from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black') #Background colour
screen.title('Snake') #Title

segments = []

for number in range(3):
    x_value = -20 * (number - 1)
    new_segment = Turtle(shape='square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(x_value, 0)
    segments.append(new_segment)

print(segments)

screen.exitonclick()