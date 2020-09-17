import turtle
t = turtle.Pen()

def geschmückt():
    while 1 == 1:
        t.forward(90)
        t.circle(-5)
        t.circle(5)
        t.forward(90)
        t.circle(10,72)
        t.circle(-5)
        t.circle(10,72)
    
def einfach():
    while 1 == 1:
        t.forward(100)
        t.left(60)
        
def einfach2():
    while 1 == 1:
        t.forward(50)
        t.right(60)
        t.forward(10)
        t.left(120)
        t.forward(10)
        t.right(60)
        t.forward(50)
        
        t.left(60)
        t.circle(-10)
    


#einfach()
#einfach2()
geschmückt()
