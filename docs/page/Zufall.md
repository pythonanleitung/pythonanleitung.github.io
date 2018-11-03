# Zufall

[Zurück zum fünften Abschnitt](BedingtesAusfuehren.md) | [Zurück zur ersten Seite](README.md)

Für das Programm aus der letzten Übung wäre es natürlich schön, wenn sich der Computer die Zahl, die zu erraten ist, selbst ausdenkt, da sonst das Ratespiel recht schnell langweilig wird.

Um eine zufällige Zahl zu generieren, benötigt Python ein Modul. Module sind in Python Pakete mit Zusatzfunktionen, die in der Grundsprache fehlen.

Module werden mit dem `import` Befehl geladen. Das Modul,
welches viele Zufalls relevanten Funktionen beherbergt heißt `random`.
Dieses kann geladen werden mit `import random`.

Möchte man nun eine Funktion des `random`-Moduls nutzen, so muss man immer `random.<funktion>` schreiben. Wobei `<funktion>` natürlich durch den Namen einer Funktion zu ersetzen ist. Dieser `.` bedeutet so etwas wie "aus" oder besser gesagt "dieser Teil". Der Punkt wird auch an anderen Stellen für ähnliche Bedeutungen verwendet.

Die Funktion, die eine zufällige Zahl produziert und zurück gibt, heißt `randint`. Sie nimmt zwei Parameter, also zwei Eingaben entgegen. Beide Eingaben müssen eine Zahl sein. Die erste ist die untere Grenze der Zufallszahlen, die zweite ist die obere mögliche Grenze der Zufallszahlen.

Mit `random.randint(0,100)` erstellt man also eine zufällige
ganze Zahl zwischen `0` und `100` ausgewählt werden.

Beispiel im Ausprobierfenster:

```python
>>> import random
>>> random.randint(0,100)
48
>>> random.randint(0,100)
78
>>> x = random.randint(0,100)
>>> x
17
>>> x = random.randint(0,100)
>>> x
53
```

Diese Zufallszahl kann natürlich auch in eine Variable gespeichert werden mit `zahl = random.randint(0,100)`.

> ### Aufgabe
> 1. Schreiben Sie folgende Aufgaben in die Datei `ratespiel.py`.
> 1. Schreiben Sie ein Programm, welches eine Zufallszahl zwischen `1` und `10` generiert, und diese ausgibt.
> 2. Erweitern Sie dieses Programm so, dass es dreimal nach einem Tipp fragt, für diese Zahl () die Ausgabe der zahl sollte natürlich entfernt werden.
> 3. Speicheren Sie die Zufallszahl zu Beginn in eine Variable und verändern Sie diese dann nicht mehr. Nun geben Sie jedes Mal aus, ob der Tipp zu groß oder zu klein war. Es sollte nun möglich sein die Zahl in 3 Versuchen zu erraten.
> Beispiel:
>
> ```python
> Tipp: 5
> zu klein
> Tipp: 8
> zu groß
> Tipp: 7
> richtig
> ```

[Weiter zum nächsten Abschnitt](Wiederholungen.md) |
