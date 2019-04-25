# Listen

{back} {inhalt} {chapter} {next}

Python kann neben einem einzelnen Wert auch eine Liste von Werten in einer Variablen abspeichern.

Ein Beispiel:

```python
a = [3,4,2,1,-155,7]
```

Die so erstellte Liste kann nun verwendet werden. Soll zum Beispiel die erste Zahl der Liste verwendet werden, so schreibt man z.B. `print(a[0])`, für die `-155`, `print(a[4])` und für die letzte Zahl `print(a[5])`

Mit zahlen ist das noch relativ uninteressant aber zum Beispiel eine Liste mit Farben:

```python
b = ["red", "blue", "green", "yellow", "purple", "pink"]
i = 0
while i <= 5:
    t.color(b[i])
    t.forward(30)
    t.left(45)
    i = i + 1
```

Auch Wörter lassen sich wie Listen behandeln. Man kann zum Beispiel ein "Wort" machen, welches den Richtungen, die die Schlange gehen soll entspricht und eine Schlange dann den entsprechenden Richtungen entlang gehen lassen.

```python
wort = "lrllrrrlrlrrlrr"
i=0
while i <= 14:
    if wort[i] == "l":
        t.left(90)
    if wort[i] == "r":
        t.right(90)
    t.forward(30)
    i = i + 1
```

Statt die Länge des Wortes händisch zu zählen (also die 15), kann auch die Funktion `len(wort)` verwendet werden.

{back} {inhalt} {chapter} {next}
