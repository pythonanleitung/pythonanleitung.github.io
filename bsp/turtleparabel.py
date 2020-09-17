import turtle
screen = turtle.Screen()
t=turtle.Turtle()
#t.screen.tracer(0,0)

t.pu()
t.goto(-100,200)
t.pd()
    
t.hideturtle()

for x in range(-100,150,1):
    t.goto(x, x*x/50)

t.pu()
t.goto(-150,1.3*-150 + 10-120)
t.pd()

for x in range(-150,150,1):
    t.goto(x, 1.3*x + 10 )

screen.exitonclick()