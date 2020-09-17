import turtle

canvas = turtle.Screen()

t = turtle.Turtle()

t.shape("turtle")

import math

innen = math.sqrt(20**2*2)
width = 160

t.pu()
t.goto(-80,80)
t.pd()

for i in range(3):
    for i in range(4):
        t.forward(width)
        t.right(90)
    width = width - 40
    t.pu()
    t.left(-45)
    t.forward(innen)
    t.right(-45)
    t.pd()


canvas.exitonclick()