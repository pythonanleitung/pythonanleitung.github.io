import turtle

t = turtle.Pen()
t.speed(0)

for i in range(5):
    for i in range(20):
        t.circle(-10)
        t.forward(10)
    
    t.circle(-10)
    t.left(72)
    t.circle(-10)
    t.left(72)

t.hideturtle()

t.pu()
t.backward(400)
t.pd()
for i in range(5):
    for i in range(20):
        t.right(70)
        t.forward(10)
        t.left(70)
        t.forward(10)
    
    t.left(72)
    t.left(72)
    