from turtle import Turtle, Screen

brush = Turtle()
window = Screen()

def move_forward():
    brush.forward(10)

window.listen()

window.onkey(key='space', fun=move_forward)

window.exitonclick()