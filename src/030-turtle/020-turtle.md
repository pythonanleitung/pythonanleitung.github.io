# Schildkröten



Nachdem Nun die gröbsten Grundlagen der Programmiersprache gelernt sind, fängt es jetzt an (noch mehr) Spaß zu machen.

## Schultern von Giganten

Bedenken Sie, dass beim Programmieren die eigene Arbeit immer auf der Arbeit von ganz vielen anderen beruht. Zum Beispiel um Python zu entwickeln müsste eine Person ca. 285 Jahre arbeiten. Um Python entwickeln zu lassen müsste man 13.5 Millionen Euro veranschlagen. Im Folgenden Wird ein relativ kleines Modul verwendet mit welchem man eine bestimmte Art von Grafiken erstellen kann. Auch für dieses Modul wurden über 4000 Zeilen programmiert.

## Erstellen des Fensters

1. Erstellen Sie in `thonny` eine neue Datei durch Klick auf das weiße Symbol ganz links.
2. Schreiben sie die 3 Zeilen aus dem folgenden Beispiel in diese Datei. Die Zeilen werden danach einzeln besprochen.
   ```python
   import turtle

   t = turtle.Pen()
   t.shape("turtle")
   ```

3. Speichern Sie die Datei unter dem Namen `meine-kröte.py` ab.
4. Klicken Sie auf "Play". Es sollte ein Fenster mit einer kleinen Schildkröte in der Mitte erscheinen.

![Leeres Turtle Fenster](img/leerturtle.png)

Erklärungen der Zeilen:

1. Zunächst muss mit `import turtle` das `turtle`-Modul geladen werden.

2. Danach erzeugt man eine Schildkröte mit dem Befehl `turtle.Pen()`. Hierbei wird das Fenster, in dem die Zeichnung entsteht, geöffnet.

   Damit später auf diese Schildkröte zugegriffen werden kann, muss sie in einer Variablen (hier `t`) gespeichert werden.

3. Wenn man möchte, kann man auch noch das aussehen der "Schildkröte" verändern. Die Standardeinstellung ist ein Dreieck, dessen Spitze in Laufrichtung zeigt. Mit dem Befehl `t.shape("turtle")` wird diese Form zu einer Schildkrötensilhouette.

Diese drei Zeilen sind die Grundlage jedes turtle-Programms. Immer, wenn sie turtle verwenden wollen müssen diese Zeilen zu Beginn ihrer Datei stehen.

> ### Achtung
> **Beim Speichern der Datei darf nicht der Name `turtle.py` gewählt werden.** Dieser Name wird quasi von dem `turtle`-Modul reserviert.

## Das Turtle bewegen und dabei zeichnen

Nun können Sie der Schildkröte Befehle geben. Es gibt unter anderem: `forward`, `left` und `right`. Dabei sind alle Befehle in Fahrtrichtung.Die Schildkröte steht zu Begin in der mitte, so dass sie nach rechts läuft, wenn man ihr zum Beispiel den Befehl `t.forward(100)` gibt. Das heißt wenn am Anfang `t.left(90)` angegeben wird:  wird sie gegen den Uhrzeigersinn um 90° gedreht, sodass sie nach oben schaut.

> ### Merke
> * Die Befehle werden Zeile für Zeile ausgeführt.
> * Drückt man auf den grünen "Play-Knopf" wird alles neu gestartet, dann der Befehl in der ersten Zeile ausgeführt, dann der in der zweiten und so weiter.

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

> ### Übung
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
> Tipp: Wenn Sie die [Kommentarfunktion](030-kommentare.md) benutzen, dann ist es einfacher die Übersicht zu behalten.
>
> Ergebnis:
>
> ![Quadrate](img/turtlequadrate.png)

## Rechnen in Python

Wenn Sie bestimmte Formen zeichnen wollen, so müssen Sie bestimmte Winkel und Längen berechnen. Im rechtwinkligen Dreieck lässt sich das sehr einfach durch die Formel von Pythagoras `a² + b² = c²` lösen. Also die beiden kürzeren Seitenlängen eines rechtwinkligen Dreiecks quadriert und zusammengezählt ergeben das Quadrat der längsten Seitenlänge.

Um aus dieser Zahl die Quadratwurzel (engl. _square root_) zu berechnen benötigen Sie die Wurzelfunktion. Diese ist in dem `math`-Modul enthalten.

Berechnen des Pythagoras:

```python
import math
a = 5
b = 7
c = math.sqrt(a * a + b * b)
```

Es wird hier in `c` die Wurzel aus `a² + b²` also `a*a + b*b` gespeichert.

Passen Sie `a` und `b` so an, dass sie damit die Diagonalen der folgenden Übungen ausrechnen können. Um die Länge einer Diagonalen zu zeichnen, gehen sie um `c` vorwärts: `t.forward(c)`


> ### Übung
>
> Speichern Sie dies in die Datei `nikolaushaus-uebung.py`
>
> 1. Zeichnen Sie das Haus vom Nikolaus. Berechnen Sie dabei die Länge der diagonalen in Python. Verwenden Sie ein gleichseitiges Dreieck als Dach.
>
>    ![Haus vom Nikolaus](img/nikolaushaus.png)
> 2. Speichern Sie diese Datei zusätzlich unter dem Namen `nikolaushaus-uebung-rechtwinklig.py`. Hierzu klicken sie auf "File->Save as" oder "Datei->Speichern unter"
> 2. Verändern Sie in dieser neuen Datei die Zeichnung so, dass das Dach rechtwinklig ist. Hier können Sie bemerken, dass die [Kommentarfunktion](030-kommentare.md) sehr hilfreich sein kann.
>
>    ![Haus vom Nikolaus](img/nikolaushaus2.png)
