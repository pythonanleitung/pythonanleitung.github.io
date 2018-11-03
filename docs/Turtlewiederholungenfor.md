# Wiederholungen mit Turtles

[Zurück zu Kapitel 13: Wiederholungen mit for](Wiederholungenfor.md) |  [Inhaltsverzeichnis](README.md) |  [Weiter zu Kapitel 15: Zufall](Zufall.md) | 

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



[Zurück zu Kapitel 13: Wiederholungen mit for](Wiederholungenfor.md) |  [Inhaltsverzeichnis](README.md) |  [Weiter zu Kapitel 15: Zufall](Zufall.md) | 
