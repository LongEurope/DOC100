#Hirst Painting
from turtle import Turtle, Screen
import random

# rgb_colors = []
# colors = colorgram.extract(r"C:\Users\glenn\OneDrive\Documents\Python\DOC100\Intermediate (15-\Day18\hirst.png", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(190, 172, 128), (157, 177, 191), (188, 164, 176), (214, 204, 135), (152, 183, 174), (167, 205, 190), (205, 182, 194), (182, 158, 59), (179, 190, 209), (169, 200, 206), (212, 183, 176), (105, 120, 180), (92, 109, 141), (208, 207, 41), (152, 122, 114), (162, 109, 117)]
turtle_color_list = []

def set_brush():
    for _ in range(2):
        brush.up()
        brush.right(90)
        brush.forward(user_side*20)
    brush.right(180)

def color_from_list():
    global turtle_color_list
    if len(turtle_color_list) < 1:
        turtle_color_list.clear()
        for color in color_list:
            turtle_color_list.append(color)
    chosen_color = random.choice(turtle_color_list)
    turtle_color_list.remove(chosen_color)
    return chosen_color


def start_hirsting():
    for side in range(user_side):
        for side in range(user_side):
            brush.pencolor(color_from_list())
            brush.dot(20)
            brush.up()
            brush.forward(40)
        brush.right(180)
        brush.forward(user_side * 40)
        brush.right(90)
        brush.forward(40)
        brush.right(90)

user_side = int(input('How many side would you like: '))

brush = Turtle()
brush.speed('fastest')
window = Screen()
window.colormode(255)

brush.hideturtle()
set_brush()
start_hirsting()

window.exitonclick()