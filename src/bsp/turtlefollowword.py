import turtle
screen = turtle.Screen()
t=turtle.Turtle()
#t.screen.tracer(0,0)

word = "lrllrrrlrlrrlrr"

i=0

while i < 15:
    if word[i] == "l":
        t.left(90)
    if word[i] == "r":
        t.right(90)
    t.forward(30)
    i = i + 1

screen.exitonclick()