import turtle
screen = turtle.Screen()
t=turtle.Turtle()
t.screen.tracer(0,0)
 
for x in range(0,300,2):
    t.fd(x)
    t.left(89)

screen.exitonclick()
screen.mainloop()