# Zusammenfassung der Turtle Befehle

{back} {inhalt} {next}

Erstellen eines Turtlefensters mit:

```python
import turtle
t = turtle.Turtle()
t.shape("turtle")
```

Eine Auswahl zu möglichen Funktionen des Turtlemoduls. Eine vollständige Liste aller funktionen gibt es unter:
[Turtle Dokumentation](https://docs.python.org/3.6/library/turtle.html)

# Bewegungen:

```python
t.forward(distance=90)  # gehe vorwärts
t.backward(distance=90) # gehe zurück
t.right(angle=60)       # drehe rechts
t.left(angle=60)        # drehe links
t.goto(x=0,y=0)         # gehe zu Koordinaten
t.home()                # gehe zur Mitte
t.circle(radius, extent, steps) # Male einen (Teil-)Kreis
```

# Malen:

```python
t.penup()               # Aufhören zu zeichnen
t.pendown()             # Anfangen zu zeichnen
t.width(width=5)        # Strichdicke
t.pencolor("red")       # Stiftfarbe setzen
t.begin_fill()          # Ausgemalten Umris starten
t.end_fill()            # Ausgemalten Umris beenden
t.fillcolor("blue")     # Ausmalfarbe setzen
t.screen.bgcolor("pink")# Die Hintergrundfarbe setzen
```

# Turtle:
```python
t.shape()               # Auswählen einer Form
t.hideturtle()          # Verstecken der Schildkröte
t.showturtle()          # zeigen der Schildkröte
t.exitonclick()         # schließen wenn ins fenster geklickt wird
```

{back} {inhalt} {next}
