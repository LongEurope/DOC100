from turtle import Turtle, Screen

def move_forward():
    brush.forward(10)

def move_backward():
    brush.backward(10)

def turn_right():
    new_heading = brush.heading() - 10
    brush.setheading(new_heading)

def turn_left():
    new_heading = brush.heading() + 10
    brush.setheading(new_heading)

brush = Turtle()
window = Screen()

window.listen()

window.onkey(key='w', fun=move_forward)
window.onkey(key='s', fun=move_backward)
window.onkey(key='a', fun=turn_left)
window.onkey(key='d', fun=turn_right)

window.exitonclick()