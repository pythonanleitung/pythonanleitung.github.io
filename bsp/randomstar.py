import turtle
import random

t = turtle.Pen()
t.speed(0)
#t.color("darkred")
#t.fillcolor("yellow")
t.width(1)
x = list(range(-80,80,8))

while True:

    random.shuffle(x)

    t.begin_fill()
    for i in range(18):
        for i in x:
            t.forward(30)
            t.left(i)
        t.left(180)
    t.end_fill()
    t.clear()
