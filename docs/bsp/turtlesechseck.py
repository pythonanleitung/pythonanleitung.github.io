import turtle
screen = turtle.Screen()
t=turtle.Turtle()
screen.bgcolor("black")
colors=["blue","purple","red","yellow","orange","brown"]
#t.screen.tracer(0,0)
 
for x in range(100):
    t.color(colors[x%6])
    t.fd(x)
    t.left(59)

screen.exitonclick()
screen.mainloop()