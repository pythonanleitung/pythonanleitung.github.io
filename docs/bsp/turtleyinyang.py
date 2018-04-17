import turtle

canvas = turtle.Screen()

t = turtle.Turtle()

t.shape("turtle")

t.speed(0)

t.pu()
t.goto(0,-90)
t.pd()

t.circle(90,180)
t.begin_fill()
t.circle(90,180)
t.circle(45,180)
t.circle(-45,180)
t.pu()
t.right(90)
t.forward(37)
t.left(90)
t.pd()
t.circle(-8)
t.pu()
t.right(90)
t.forward(90)
t.left(90)
t.pd()
t.circle(-8)
t.end_fill()

t.ht()