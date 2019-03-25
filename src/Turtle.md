# Schildkröten

{back} {inhalt} {next}

Nachdem Nun die gröbsten Grundlagen der Programmiersprache gelernt sind, fängt es jetzt an (noch mehr) Spaß zu machen. Im folgenden wird das Modul `turtle` verwendet. Dieses stellt eine einfache Möglichkeit zur Verfügung ein Fenster zu öffnen und in dieses Fenster mithilfe eines `turtles` zu zeichnen.

Bedenken Sie, dass beim Programmieren die eigene Arbeit immer auf der Arbeit von ganz vielen anderen Beruht. Zum Beispiel um Python zu entwickeln müsste eine Person ca. 285 Jahre arbeiten. Um Python entwickeln zu lassen müsste man 13.5 Millionen Euro veranschlagen. Im Folgenden Wird ein relativ kleines Modul verwendet mit welchem man eine Bestimmte Art von Grafiken erstellen kann. Auch für dieses Modul wurden über 4000 Zeilen programmiert.

Beispiele für solche Grafiken sind im [Kapitel Beispielaufgaben](Turtlebeispielaufgaben.md) zu finden.

## Erstellen des Fensters

Erstellen Sie in `thonny` die Datei `meine-kröte.py` und fügen Sie die folgenden 3 Zeilen ein. Nach einem Klick auf "Play" erscheint ein Fenster mit einem turtle in der Mitte.

> ### Achtung
> **Beim Speichern der Datei darf nicht der Name `turtle.py` gewählt werden.** Dieser Name wird quasi von dem `turtle`-Modul reserviert.

```python
import turtle

t = turtle.Pen()
t.shape("turtle")
```
Erklärungen der Zeilen:

1. Zunächst muss mit `import turtle` das `turtle`-Modul geladen werden.

1. Danach wird das Fenster geöffnet mit dem Befehl `turtle.Pen()`.

   Damit später in dieses Fenster gezeichnet werden kann, muss es in einer Variablen `t` gespeichert werden.

1. Wenn man möchte, kann man auch noch das aussehen der "Schildkröte" verändern. Die Standardeinstellung ist ein Dreieck, dessen Spitze in Laufrichtung zeigt. Mit dem Befehl `t.shape("turtle")` wird diese Form zu einer Schildkrötensiluette.

Nach dem Speichern und Ausführen, sollte ein Fenster sich öffnen, in dessen Mitte sich die Schildkröte befindet:

![Leeres Turtle Fenster](img/leerturtle.png)

## Das Turtle bewegen und dabei zeichnen

Nun können Sie der Schildkröte Befehle geben. Es gibt unter anderem: `forward`, `left` und `right`. Dabei sind alle Befehle in Fahrtrichtung. Das heißt wenn am Anfang `t.left(90)` angegeben wird: Die Schildkröte zuerst nach rechts, und wird dann gegen den Uhrzeigersinn um 90° gedreht, sodass sie nach oben schaut.

> ### Merke
> Die Befehle werden Zeile für Zeile ausgeführt. Drückt man auf den grünen "Play-Knopf" wird alles neu gestartet, dann der Befehl in der ersten Zeile ausgeführt, dann der in der zweiten und so weiter.

Um also mit dem `turtle` einen rechten Winkel zu zeichnen, der zunächst waagerecht verläuft und dann nach unten geht kann man nun folgenden Code eingeben:

```python
import turtle

t = turtle.Pen()
t.shape("turtle")

t.forward(200)
t.right(90)
t.forward(200)
```
Das Ergebnis ist dann folgendes:

![Rechter Winkel Turtle](img/turtlerightangle.png)

Es ist natürlich auch möglich weniger weit zu gehen `t.forward(87)` oder sich um einen anderen Winkel zu drehen `t.left(63)`.

> ### Übungen
>
> Speichern Sie dies in die Datei `geometrische-uebung.py`
>
> 1. Zeichnen Sie ein Quadrat
> 1. Zeichnen Sie ein Rechteck, welches doppelt so breit ist, wie hoch und nur eine Ecke gemeinsam mit dem ersten Quadrat hat.
> 1. Zeichnen Sie ein gleichseitiges Dreieck
>
> Ergebnis der Übung:
>
> ![Übungsresultat](img/turtleshapes.png)

## Das Turtle bewegen, ohne zu zeichnen

Soll das Turtle an eine Position, ohne dabei eine Spur zu hinterlassen, dann kann man folgende Befehle verwenden:

 * `t.penup()`: sagt dem `turtle` höre auf zu zeichnen.
 * `t.pendown()`: sagt dem `turtle` fange wieder an zu zeichnen.

Man kann also dem `turtle` sagen zeichne jetzt nicht, dann kann man es ganz normal mit `forward`, `left` und `right` bewegen, und wenn das `turtle` wieder zeichnen soll, sagt man das einfach mit dem `pendown`-Befehl.

Beispiel einer unterbrochenen Linie (Achtung Die Befehle zum erstellen des `turtles` sind hier weg gelassen):

```python
t.forward(30)
t.penup()
t.forward(30)
t.pendown()
t.forward(30)
t.penup()
t.forward(30)
t.pendown()
t.forward(30)
```

> ### Übung
>
> Speichern Sie dies in die Datei `quadrate-uebung.py`
>
> Zeichnen Sie 3 Quadrate mit dem selben Mittelpunkt wobei jeweils das folgende kleiner ist als das erste.
>
> Tipp: Wenn Sie die [Kommentarfunktion](Kommentare.md) benutzen, dann ist es einfacher die Übersicht zu behalten.
>
> Ergebnis:
>
> ![Quadrate](img/turtlequadrate.png)

## Rechnen in Python

Wenn Sie bestimmte Formen zeichnen wollen, so müssen Sie bestimmte Winkel und Längen berechnen. Im rechtwinkligen Dreieck lässt sich das sehr einfach durch die Formel von Pythagoras `a² + b² = c²` lösen. Also die beiden kürzeren Seitenlängen eines rechtwinkligen Dreiecks quadriert und zusammengezählt ergeben das Quadrat der längsten Seitenlänge.

Um aus dieser Quadratszahl die Wurzel zu berechnen benötigen sie die Wurzelfunktion. Diese ist in dem `math`-Modul enthalten.

Import und Verwendung der `sqrt` Wurzelfunktion:

```python
import math
a = 5
b = 7
c = math.sqrt(a * a + b * b)
```

Es wird hier in `c` die Wurzel aus `a² + b²` also `a*a + b*b` gespeichert. Passen Sie `a` und `b` so an, dass sie damit die Diagonalen der folgenden Übungen ausrechnen können. Um die Länge einer Diagonalen zu zeichnen, gehen sie um `c` vorwärts: `t.forward(c)`

> ### Übung
>
> Speichern Sie dies in die Datei `nikolaushaus-uebung.py`
>
> 1. Zeichnen Sie das Haus vom Nikolaus. Berechnen Sie dabei die Länge der diagonalen in Python. Verwenden Sie ein gleichseitiges Dreieck als Dach.
>
>    ![Haus vom Nikolaus](img/nikolaushaus.png)
>
> 1. Zeichnen Sie ein Nikolaushaus mit einem rechtwinkligen Dach:
>
>    ![Haus vom Nikolaus](img/nikolaushaus2.png)

{back} {inhalt} {next}
