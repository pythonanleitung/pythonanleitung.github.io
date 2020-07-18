import turtle
screen = turtle.Screen()
t=turtle.Turtle()
screen.bgcolor("black")
colors=["blue","purple","red","yellow"]
t.screen.tracer(0,0)
 
for x in range(200):
    t.color(colors[x%4])
    t.fd(x)
    t.left(91)

screen.exitonclick()
screen.mainloop()