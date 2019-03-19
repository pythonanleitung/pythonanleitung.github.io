# Der input-Befehl des turtle-Moduls

[Zurück: Kapitel 3 - Schildkröten](Turtle.md) |  [Home](README.md) |  [Weiter: Kapitel 5 - Wiederholungen mit While](Wiederholungenwhile.md) | 

Das `turtle`-modul hat die Möglichkeit ein "Dialogfenster" zu öffnen.  Damit kann nach einem Text oder eine Zahl gefragt werden. Das was in diesem diealogfenster eingegeben wird, wird unter dem Namen vor dem `=` abgespeichert. Später kann man diesen Wert dann verwenden. Zum Beispiel kann dann mit `t.forward(zahl)` eine Linie der Länge die erfragt wurde gezeichnet werden.

Turtle stellt zwei Befehle zur Verfügung:

1. `turtle.numinput(title="", prompt="")`
2. `turtle.textinput(title="", prompt="")`

Zwischen den Anführungszeichen steht der Text der im Dialogfenster angezeigt wird. Ersetzen Sie die Beispiele durch eigene Texte.

```python
zahl = turtle.numinput(title="was dann im titel des Fensters steht", prompt="Welche Frage vor dem Eingabefeld steht")
text = turtle.textinput(title="was dann im titel des Fensters steht", prompt="Welche Frage vor dem Eingabefeld steht")
```

Zu beachten ist, dass tatsächlich `turtle.` vor `*input` stehen muss. Was in `title=` übergeben wird landet im Fenstertitel, was in `promt=` übergeben wird ist quasi die Frage.

> ### Übung
>
> Gespeichert in der neuen Datei `kleingroß.py`
>
> 1. Schreiben Sie ein Turtle-Programm, welches zuerst nach einer Zahl fragt, und dann ein Quadrat in entsprechender Größe, also Seitenlänge zeichnet.
> 2. Erweitern Sie das Programm, dass es nach dem Zeichnen des Quadrats noch eine Größe für ein gleichseitiges Dreieck fragt, und dieses dann zeichnet.

[Zurück: Kapitel 3 - Schildkröten](Turtle.md) |  [Home](README.md) |  [Weiter: Kapitel 5 - Wiederholungen mit While](Wiederholungenwhile.md) | 
