# Zusammenfassung der Turtle Befehle

[Zurück: Kapitel 20 - Turtle Beispielaufgaben](Turtlebeispielaufgaben.md) |  [Home](README.md) |  [Weiter: Kapitel 22 - Computerspiele](Computerspiel.md) | 

Erstellen eines Turtle-Fensters mit:

```python
import turtle
t = turtle.Turtle()
t.shape("turtle")
```

Eine Auswahl zu möglichen Funktionen des Turtle-Moduls. Eine vollständige Liste aller Funktionen gibt es unter:
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
t.width(width=5)        # Strich dicke
t.pencolor("red")       # Stiftfarbe setzen
t.begin_fill()          # Ausgemalten Umriss starten
t.end_fill()            # Ausgemalten Umriss beenden
t.fillcolor("blue")     # Ausmal-Farbe setzen
t.screen.bgcolor("pink")# Die Hintergrundfarbe setzen
```

# Turtle:
```python
t.shape()               # Auswählen einer Form
t.hideturtle()          # Verstecken der Schildkröte
t.showturtle()          # zeigen der Schildkröte
t.exitonclick()         # schließen wenn ins Fenster geklickt wird
turtle.numinput("", "") # Turtle Fragt nach einer Zahl mit `title` und `promt`
turtle.textinput("", "")# Turtle Fragt nach einem Text mit `title` und `promt`
```

[Zurück: Kapitel 20 - Turtle Beispielaufgaben](Turtlebeispielaufgaben.md) |  [Home](README.md) |  [Weiter: Kapitel 22 - Computerspiele](Computerspiel.md) | 
