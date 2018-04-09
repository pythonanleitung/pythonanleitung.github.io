# Schildkröten

Nachdem Nun die gröbsten Grundlagen der Programmiersprache gelernt sind, fängt es jetzt an Spaß zu machen. Im folgenden wird das Modul `turtle` verwendet. Dieses stellt eine einfache Möglichkeit zur Verfügung ein Fenster zu öffnen und in dieses Fenster mithilfe eines `turtles` zu zeichnen.

## Erstellen des Fensters

Zunächst muss das `turtle`-modul geladen werden. Danach wird das Fenster geöffnet mit dem Befehl `turtle.Pen()`. Damit später in dieses Fenster gezeichnet werden kann, muss es in einer Variablen gespeichert werden.

Die Datei `meine-kröte.py` sieht also bis jetzt so aus:

```python
import turtle

t = turtle.Pen()
```

> ### Achtung
> Beim Speichern der Datei darf nicht der name `turtle.py` gewählt werden. Dieser Name wird quasi von dem `turtle`-Modul reserviert.

Nach dem Speichern und Ausführen, sollte ein Fenster sich öffnen, in dessen Mitte sich die Schildkröte befindet:

![Leeres Turtle Fenster]()

Nun können Sie der Schildkröte Befehle geben. Es gibt unter anderem: `forward`, `left` und `right`. Dabei sind alle Befehle in Fahrtrichtung. Das heißt wenn am Anfang `left(90)` angegeben wird, dann schaut die Schildkröte zuerst nach rechts, und wird dann gegen den Urzeigersinn gedreht, sodass sie nach oben schaut.
