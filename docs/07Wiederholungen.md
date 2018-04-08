# Wiederholungen

[Zurück zum sechsten Abschnitt](06Zufall.md) | [Zurück zur ersten Seite](/)

Oftmals in einem Computerprogramm soll der Computer Dinge wiederholen. Eine Form der Wiederholung ist es etwas so lange zu wiederholen, bis eine Bedingung nicht mehr zutrifft. Die Bedingung wird dabei genauso geschrieben, wie dies bei `if` gemacht wurde.

## Der Befehl While
`while` wiederholt einen Programmteil so oft, bis die Bedingung nicht mehr zutrifft.

Ein abstraktes Beispiel:

```python
while <Bedingung>:
    print("ich werde wiederholt")
```

Der Aufbau des `while` ist identisch dem des `if` Befehls. Die Einleitung mit `while`, danach die Bedingung gefolgt von einem Doppelpunkt. In den nächsten Zeilen eingerückt die Befehle, die wiederholt werden sollen. Sollen mehrere Zeilen wiederholt werden, können auf das while mehrere Zeilen folgen. Die Zugehörigkeit zu diesem while ist wie beim `if` durch die Einrückung definiert. Es kann auch innerhalb eines `while` noch ein `while` vorkommen.

Ein konkretes Beispiel, welches immer wieder nach einer Eingabe fragt, bis `"ende"` eingegeben wurde:

```python
eingabe = input("Eingabe: ")
while not (eingabe == "ende"):
    print("Bei der Eingabe ", eingabe, "konnte ich kein ende finden")
    eingabe = input("Eingabe: ")
print("So, jetzt ist aber fertig.")
```

Hat je nach Eingaben folgende Ausgabe (das Programm wurde zwei mal gestartet):

```python
>>> %Run hallo.py
Eingabe: tut
Bei der Eingabe  tut konnte ich kein ende finden
Eingabe: Ende
Bei der Eingabe  Ende konnte ich kein ende finden
Eingabe: ende
So, jetzt ist aber fertig.
>>>
>>> %Run hallo.py
Eingabe: ende
So, jetzt ist aber fertig.
```

Es wird an diesem 2. Beispiel deutlich, dass die Wiederholung unter Umständen auch Null mal stattfindet. Es wird nämlich vor jedem Schleifenaufruf die Bedingung überprüft. Wird also schon beim ersten Mal eingeben `ende` eingegeben (der `input`-Befehl in der ersten Zeile im Beispiel), dann ist eingabe schon beim allerersten überprüfen gleich `ende` das heißt durch den Vergleich entsteht der Wahrheitswert `True` welcher durch den "nicht"-Befehl `not` zu `False` umgekehrt wird. Solange aus der Bedingung `True` entsteht werden die enthaltenen Befehle wiederholt. Da schon am Anfang `False` entsteht, wird das `print` und das zweite `input` kein einziges Mal ausgeführt, sondern einfach übersprungen und das letzte `print` zeigt seine Ausgabe. Dieses letzte `print` hat weniger Leerzeilen am anfang der Zeile und gehört damit nicht mehr zu dem `while`.

> ### Aufgaben
> Kleine Beispiel `while`:
>
> 1. Schreiben Sie eine `while`-Schleife, die immer fragt "warum soll ich?" erst bei der Eingabe "schluss jetzt!" beendet sich die Schleife.
> 1. **Knobelaufgabe:** Erweitern Sie die vorherige `while`-Schleife um eine weitere, die, sollte man der ersten antworten "du nervst", gestartet wird. Diese zweite Schleife ist innerhalb der ersten und muss mit einem `if` Befehl gestartet werden. Die zweite innere Schleife soll sich nur beenden, wenn auf die Frage "Tu ich nicht - warum sollte ich?" mit "okay" geantwortet wird. Logischerweise wird dann wieder die erste Schleife weiter wiederholt bis man "ende" eingibt.
> 1. Schreiben Sie eine Schleife, die wiederholt solange man "weiter" eingibt.
>
> Ratespiel erweitern:
>
> 1. Verändern Sie das Zahlen-Rate-Programm so, dass man beliebig viele Versuche hat beim Raten. Verwenden Sie hierzu `while`.
> 1. Erweitern Sie das Programm so, dass es Zufallszahlen zwischen `0` und `100` verwendet.
