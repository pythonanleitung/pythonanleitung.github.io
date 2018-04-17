import turtle

canvas = turtle.Screen()

t = turtle.Turtle()

t.shape("turtle")

t.speed(0)
t.width(2)
t.fillcolor("red")

t.pu()
t.goto(0,100)
t.pd()

def herz(größe):
    t.left(45)
    t.begin_fill()
    t.forward(größe)
    t.circle(radius=größe/2,extent=180)
    t.right(90)
    t.circle(größe/2,180)
    t.forward(größe)
    t.end_fill()
    t.left(45)

for i in range(24):
    herz(15)
    t.circle(-100,15)

t.ht()

canvas.exitonclick()