import turtle

t = turtle.Pen()

import math

def nikolausquadrat(größe):
    t.forward(größe)
    t.left(90)
    t.forward(größe)
    t.left(90)
    t.forward(größe)
    t.left(90)
    t.forward(größe)
    t.left(90)

def nikolausdiag(größe):
    quadrat = größe * größe
    diag = math.sqrt(quadrat + quadrat)
    
    t.left(45)
    t.forward(diag)
    t.left(45)
    nikolausdach(größe)
    t.left(45)
    t.forward(diag)
    t.left(45)
    

def nikolausdach(größe):
    t.left(30)
    t.forward(größe)
    t.left(120)
    t.forward(größe)
    t.left(30)
    

def nikolaus(größe):
    nikolausquadrat(größe)
    nikolausdiag(größe)

#nikolaus(6.25)
#nikolaus(12.5)
#nikolaus(25)
#nikolaus(50)
t.pu()
t.goto(-50,-80)
t.pd()
nikolaus(100)