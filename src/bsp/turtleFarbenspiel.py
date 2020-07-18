import turtle

canvas = turtle.Screen()

t = turtle.Turtle()

t.shape("turtle")

import random

b = ["red", "blue", "green", "yellow", "purple", "pink"]

i = 0

while i < 6:
    t.color(b[i])
    t.forward(30)
    t.left(45)
    i = i+1

canvas.exitonclick()