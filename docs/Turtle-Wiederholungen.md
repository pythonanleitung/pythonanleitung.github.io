# Wiederholungen mit Turtles

[Zurück zum sechsten Abschnitt](Turtle.md) | [Zurück zur ersten Seite](README.md)

## Wiederholung bis nicht mehr wahr

Mit einer While-Schleife kann ein bestimmter Teil eines Programms wiederholt werden bis eine Bedingung nicht mehr zutrifft.

Beispiel:

```python
varie = 1
while varie < 50:
    t.forward(10)
    t.left(varie)
    varie = varie * 1.02
```

In diesem Beispiel wird die Variable `varie` überprüft, ob sie kleiner ist als 50. Wenn ja, wird der eingerückte folgende Teil wiederholt.

In diesem Teil muss natürlich jetzt die Varieable `varie` verändert werden, sonst endet das Programm nie.

Immer zu begin jeder wiederholung wird die Bedingung erneut überprüft.

> ### Aufgaben
>
> Speichern Sie Ihre Lösung in die Datei `Turtlewhile.py`
>
> 1. Zeichnen Sie ein Quadrat mit `while`.
> 2. Zeichnen Sie einen Kreis indem Sie while, forward, left und variablen verwenden.
> 3. Zeichnen Sie einen Stern mit `while`.

## Wiederholung für eine bestimmte Anzahl

Soll ein Quelltext genau eine bestimmte Anzahl oft wiederholt werden, so gibt es eine einfachere Schreibweise in Python.

Beispiel:

```python
for i in range(30):
    t.forward(100)
    t.left(170)
```

Der eingerückte Teil von wird also genau 30 mal wiederholt in der Variablen `i` ist dann übrigens immer die Nummer des durchlaufs gespeichert...

> ### Aufgaben
>
> Speichern Sie Ihre Lösung in die Datei `TurtleFor.py`
>
> 1. Zeichnen Sie ein Quadrat mit `for`.
> 2. Zeichnen Sie einen Kreis indem Sie `for`, `forward` und `left` verwenden.
> 3. Zeichnen Sie einen Stern mit `for`.

## Wiederholung für jeden Buchstaben eines Wortes.

Soll etwas für jeden Buchstaben ausgeführt werden, kann auch `for` verwendet werden.

```python
for d in "rllrrlllrllrrrll":
    if d == 'r':
        t.right(90)
    if d == 'l':
        t.left(90)
    t.forward(50)
```

Hier wird jetzt die Variable `d` verwendet, um entweder einen 90° winkel im oder gegen den Uhrzeigersinn durchzuführen. Das for macht in der ersten Runde den ersten Buchstaben, also `'r'` in die `d` Variable. Mit `if` wird dies überprüft und das Programm reagiert entsprechend.

Da die Zeile mit `t.forward` wieder weniger eingerückt ist als `t.left` gehört diese Zeile zu dem `for`, nicht aber zu dem `if` das heißt egal ob das if ausgeführt wird oder nicht, das t.forward wird ausgeführt.

> ### Aufgaben
>
> Fügen Sie Ihre Lösung der Datei `TurtleFor.py` hinzu.
>
> 1. Machen Sie ein `for`, welches für jedes
>    1. r rechts geht
>    2. l links geht
>    3. c einen Kreis zeichnet
>    4. d geradeaus geht
> 2. Denken Sie sich ein schönes Bild aus, welches sie mit obigem for zeichnen.
