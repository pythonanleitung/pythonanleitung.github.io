import turtle

canvas = turtle.Screen()

t = turtle.Turtle()

t.shape("turtle")

import random

import math

innen = math.sqrt(20**2*2)
width = 160

t.speed(0)
t.width(4)

def herz(größe):
    t.left(45)
    t.forward(größe)
    t.circle(radius=größe/2,extent=180)
    t.right(90)
    t.circle(größe/2,180)
    t.forward(größe)

t.pu()
t.goto(0, -50)
t.pd()
t.color("red")

herz(100)
    
t.ht()

canvas.exitonclick()