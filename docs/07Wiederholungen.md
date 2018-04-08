# Wiederholungen

[Zurück zum sechsten Abschnitt](06Zufall.md) | [Zurück zur ersten Seite](/)

Oftmals in einem Computerprogramm soll der Computer Dinge wiederholen. Dies kann eine bestimmte Anzahl sein oder es kann etwas wiederholt werden so lange bis eine Bedingung nicht mehr zutrifft.

## While
Für den zweiten Fall ist der Befehl `while` vorgesehen. While wiederholt einen Programmteil so oft, bis die Bedingung nicht mehr zutrifft. Ein abstraktes Beispiel:

```python
while <Bedingung>:
    print("ich werde wiederholt")
```

Ein konkretes Beispiel, welches immer wieder nach einer Eingabe fragt, bis `"ende"` eingegeben wurde:

```python
eingabe = input("Eingabe: ")
while not (eingabe == "ende"):
    eingabe = input("Eingabe: ")
```

Wird dieses Programm ausgeführt so muss man irgendwann ende eingeben, sonst beendet sich das Programm nicht.

> ### Aufgabe
> Verändere das Zahlen-Rate-Programm so, dass man beliebig viele Versuche hat beim Raten. Verwende hierzu `while`.
> Erweitere das Programm so, dass es Zufallszahlen zwischen `0` und `100` verwendet.
