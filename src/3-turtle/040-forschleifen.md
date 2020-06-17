# For Schleifen



## Wiederholung für eine bestimmte Anzahl

Möchte man etwas eine bestimmte Anzahl oft wiederholen, so könnte man dies mit einer
`for`-Schleife tun:

```python
for x in range(5):
    print("Durchlauf Nummer: ", x)
```

Das Ergebnis dieses Programms ist:

```
Durchlauf Nummer: 0
Durchlauf Nummer: 1
Durchlauf Nummer: 2
Durchlauf Nummer: 3
Durchlauf Nummer: 4
```

Dieses Programm wiederholt 5 mal den `print`-Befehl. Dabei ist das `x` im ersten Durchlauf `0`, dann `1` usw. bis `4`. Die Nummer `5` wird nie erreicht.

Man kann natürlich auch das turtle "automatisieren":

```python
for i in range(30):
    t.forward(100)
    t.left(170)
t.circle(30)
```
Es ist hier Wichtig zu sehen, dass nur die Zeilen wiederholt werden, die eingerückt sind. Also die die zu Beginn der Zeile vier Leerzeichen enthalten.

Der eingerückte Teil wird also genau 30 mal wiederholt. Diesmal ist die Variable `i` genannt, man kann statt `x` oder `i` beliebige andere (passende) Namen verwenden.

Man kann mit dieser Art zu wiederholen zum Beispiel ein Sechseck zeichnen:

```python
for x in range(6):
    t.forward(100)
    t.left(60)
```

![Turtlesechseck](img/sechseck.png)

> ### Übung
>
> Speichern Sie Ihre Lösung in die Datei `TurtleFor.py`
>
> 1. Zeichnen Sie ein Quadrat mit `for`
> 2. Zeichnen Sie einen Kreis ohne dass Sie `t.circle` verwenden
> 3. Zeichnen Sie einen Stern mit `for`
>
> Die folgende Übung wird in Datei `sechseck.py` gespeichert.
>
> 1. Programmieren Sie ein turtle Sechseck.
> 2. Verzieren Sie dieses mit einem **eigenen** "Muster". Achten Sie darauf, dass das Sechseck noch zu erkennen ist.
>
> ![Turtlesechseck fancy](img/sechseckverziert.png)
>
> Die nächste Übung wird in `fünfstern.py` gespeichert.
>
> 1. Programmieren Sie einen Fünfstern mit einem turtle. Der Innenwinkel einer Fünfstern-Spitze ist `36` Grad.
> 2. Verzieren Sie diesen mit eigenen Ideen. Achten Sie auch hier darauf, dass es ein Fünfstern bleibt.
>
> Beispiel:
>
> ![TurtleFünfstern fancy](img/Turtlewiederholungenwhile3.png)
