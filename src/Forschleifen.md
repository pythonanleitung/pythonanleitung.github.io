# For Schleifen

{back} {inhalt} {next}

## Wiederholung für eine bestimmte Anzahl

Möchte man etwas eine bestimmte Anzahl oft wiederholen, so könnte man dies mit einer
`while` schleife tun, muss dann aber "mitzählen" und aufhören, wenn die gewünschte Anzahl von Durchläufen erreicht ist.

Deutlich einfacher geht dies mit `for`:

```python
for x in range(5):
    print("Durchlauf Nummer:", x)
```

Dieses Programm wiederholt 5 mal den `print`-Befehl. Dabei ist das `x` im ersten durchlauf `0`, dann `1` usw. bis `4`. Die Nummer `5` wird nie erreicht.

Ein zweites Beispiel:

```python
for i in range(30):
    t.forward(100)
    t.left(170)
```

Der eingerückte Teil von wird also genau 30 mal wiederholt. Diesmal ist die Variable `i` genannt, die die Nummer des durchlaufs enthält...

> ### Aufgaben
>
> Speichern Sie Ihre Lösung in die Datei `TurtleFor.py`
>
> 1. Zeichnen Sie ein Quadrat mit `for`.
> 2. Zeichnen Sie einen Kreis ohne dass Sie `t.circle` verwenden.
> 3. Zeichnen Sie einen Stern mit `for`.

## Wiederholungen für jedes Element einer Liste

Das `for` kann auch dazu verwendet werden, etwas für jedes Element einer Liste einmal aufzurufen. Zum Beispiel so:

```python
for el in ["blue", "green", "yellow"]:
    print("A ", el, "bird")
```

Es wird also ausgegeben: `A blue bird`, `A green bird`, `A yellow bird`

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
>    5. Bonus: s für diagonal steigend
>    6. Bonus: f für diagonal fallend
> 2. Denken Sie sich ein schönes Bild aus, welches sie mit obigem for zeichnen.
> 3. Bonus: machen Sie Rechts, Links, Kreis, … in jeweils einer anderen Farbe.

{back} {inhalt} {next}
