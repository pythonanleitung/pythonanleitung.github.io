# Der input-Befehl des turtle-Moduls

[Zurück: 1.3 - Schildkröten](Turtle.md) |  [Inhalt](README.md) |  [Kapitel](turtlekapitel.md) |  [Weiter: 1.5 - Wiederholungen mit While](Wiederholungenwhile.md) | 

Wollen Sie ein Programm schreiben, was ein Quadrat nicht immer in der selben Größe zeichnet, sondern bei dem man nach dem Klick auf play die Größe angeben kann und das Programm dann diese Größe verwendet, benötigen Sie eine Funktion mit der das Programm dem Benutzer Fragen stellen kann.

Das `turtle`-modul hat die Möglichkeit ein "Dialogfenster" zu öffnen.

1. `turtle.numinput(title="", prompt="")`
2. `turtle.textinput(title="", prompt="")`

Mit der ersten kann eine Zahl erfragt werden mit der zweiten ein Text.

Das was in diesem Dialogfenster eingegeben wird, wird unter dem Namen vor dem `=` abgespeichert. Später kann man diesen Wert dann verwenden. Zum Beispiel kann dann mit `t.forward(zahl)` eine Linie der eingegebenen Länge gezeichnet werden.

Die Texte zwischen den Anführungszeichen sind als Orientierung für den Benutzer, was er jetzt eingeben soll. Ersetzen Sie die Beispiele durch eigene Texte.

```python
zahl = turtle.numinput(title="was dann im titel des Fensters steht", prompt="Welche Frage vor dem Eingabefeld steht")
text = turtle.textinput(title="was dann im titel des Fensters steht", prompt="Welche Frage vor dem Eingabefeld steht")
```

Zu beachten ist, dass tatsächlich `turtle.` vor `numinput` und `testinput` stehen muss.

Was in `title=` übergeben wird landet im Fenstertitel, was in `prompt=` übergeben wird ist quasi die Frage.

> ### Übung
>
> Gespeichert in der neuen Datei `kleingross.py`
>
> 1. Schreiben Sie ein Turtle-Programm, welches zuerst nach einer Zahl fragt, und dann ein Quadrat in entsprechender Größe, also Seitenlänge zeichnet.
> 2. Erweitern Sie das Programm, so dass es nach dem Zeichnen des Quadrats noch eine Größe für ein gleichseitiges Dreieck fragt, und dieses dann zeichnet.

[Zurück: 1.3 - Schildkröten](Turtle.md) |  [Inhalt](README.md) |  [Kapitel](turtlekapitel.md) |  [Weiter: 1.5 - Wiederholungen mit While](Wiederholungenwhile.md) | 
