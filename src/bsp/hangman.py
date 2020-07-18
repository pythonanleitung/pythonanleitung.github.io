import turtle

t=turtle.Pen()
t.speed(0)

t.hideturtle()
t.width(3)

def hügel():
  t.left(90)
  t.penup()
  t.backward(200)
  t.pendown()
  t.circle(100,180)
  t.right(90)
  t.penup()
  t.backward(100)
  t.right(90)
  t.forward(100)
  t.pendown()
  
def senkrechte():
    t.forward(300)
    t.right(90)
    
def waagerechte():
    t.forward(100)
    t.backward(50)
    t.right(135)
    
def stütze():
    import math
    t.forward(math.sqrt(2*50*50))
    t.backward(math.sqrt(2*50*50))
    t.left(135)
    t.forward(50)
    t.right(90)


def seil():
    t.forward(50)

def kopf():
    t.right(90)
    t.circle(20, 540)
    t.right(90)
    
def körper():
    t.forward(90)
    
def beine():
    t.right(25)
    t.forward(96)
    t.backward(96)
    t.left(50)
    t.forward(96)
    t.backward(96)
    t.right(25)
    t.backward(80)
    
def arme():
    t.right(40)
    t.forward(75)
    t.backward(75)
    t.left(80)
    t.forward(75)
    t.backward(75)
    t.right(40)
    

schritte = [hügel, senkrechte, waagerechte, stütze, seil, kopf, körper, beine, arme]

import wortliste
import random

wort = random.choice(wortliste.wörter)

s = turtle.Pen()
s.hideturtle()
s.width(3)
s.speed(0)

def drawlines(geratenes):
  s.clear()
  s.penup()
  s.goto(-200, 350)
  s.pendown()
  for buchstabe in wort:
    s.forward(10)
    if buchstabe in geratenes:
      s.write(buchstabe, align="center", font="arial 12 bold")
    s.forward(10)
    s.penup()
    s.forward(20)
    s.pendown()

drawlines("")

def gewonnen(tipps, geheimwort):
  win = True
  for let in geheimwort:
    if let in tipps:
      pass
    else:
      win = False
  return win

gefunden = ""
for schritt in schritte:
  buchstabe = turtle.textinput("Hangman", "Welchen Buchstaben tippen Sie?") or ""
  while buchstabe.lower() in wort or buchstabe.upper() in wort:
    gefunden = gefunden + buchstabe.lower() + buchstabe.upper()
    if gewonnen(gefunden, wort):
        break
    drawlines(gefunden)
    buchstabe = turtle.textinput("Hangman", "Welchen Buchstaben tippen Sie?") or ""
  else:
    schritt()
  if gewonnen(gefunden, wort):
      break
    
if gewonnen(gefunden, wort):
  s.color("green")
  drawlines(wort)
else:
  s.color("red")
  drawlines(wort)