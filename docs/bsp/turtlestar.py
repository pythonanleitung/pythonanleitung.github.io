import turtle

canvas = turtle.Screen()

t = turtle.Turtle()

t.shape("turtle")

import math

innen = math.sqrt(20**2*2)
width = 160

t.pu()
t.goto(-80,30)
t.pd()

def stern(größe):
    t.forward(größe)
    t.left(144)
    t.forward(größe)
    t.left(144)
    t.forward(größe)
    t.left(144)
    t.forward(größe)
    t.left(144)
    t.forward(größe)
    t.left(144)

t.right(36)
stern(160)


canvas.exitonclick()