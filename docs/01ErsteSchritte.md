# Ein erstes Beispiel

[Zurück zur Einleitung](README.md) |

Als Erstes wird ein `thonny` geöffnet.

Es muss hierzu:

  1. die `[Windows]`-Taste gedrückt
  2. `thonny` eingegeben
  3. die Auswahl mit `[Enter]` bestätigt werden. (Das ist die "Neue Zeile"-Taste)

Nach dem Start sieht Thonny so aus:

![Screenshot Thonny](./img/ThonnyLeer.png)

Python ist speziell für Schüler und Studenten geschrieben. Es ist in zwei teile aufgeteilt.

Zunächst liegt der Fokus auf dem unteren Teil, welcher den Titel `Shell` hat und den Inhalt `>>>`.

Dieses "Pfeil"-Symbol ist das Zeichen dafür, dass Python gestartet ist und man es nun interaktiv verwenden kann.
Jede Eingabe, die man im unteren Teil macht, muss man mit `Enter` bestätigen.
Sollte einmal die Zeile nicht mit `>>>` beginnen so ist etwas mit Python nicht in Ordnung und man startet am besten nochmal vom Anfang des Beispiels, indem man oben auf das kleine "Stop"-Symbol klickt.

Hat ein Befehl ein Ergebnis, so wird dieses direkt ausgegeben.
Keine Panik nach dem Beispiel werden die Zeilen einzeln erklärt.

Werden einige Befehle in Python eingegeben könnte das so aussehen:
```python
>>> 1
1
>>> 1+1
2
```

In Zeile 1 des Beispiels wurde einfach eine Zahl `1` eingegeben.
Python antwortet darauf einfach, indem es dieselbe Zahl wieder gibt.

In Zeile 3 wird eine einfache Rechenaufgabe in Python gestellt.
Worauf Python diese berechnet und das Ergebnis zurückgibt.

> Der Computer wird auch als Rechner bezeichnet, das liegt daran, dass er nie irgendetwas anderes tut als Berechnungen auszuführen. Wird ein Computerspiel gestartet, so ist das Bild auf dem Bildschirm das Ergebnis einer (sehr komplexen) Berechnung. Das heißt natürlich auch, dass die einfachsten Befehle für einen Computer die Rechenoperationen sind.

Es können so alle Grundrechenarten verwendet wobei die folgenden Rechenzeichen verwendet werden:
  * Plus: `1 + 2`
  * Minus: `2 - 1`
  * Mal: `3 * 4`
  * Geteilt und Brüche: `6 / 3`

Beispiel:
```python
>>> 1 + 2
3
>>> 2 - 1
1
>>> 3 * 4
12
>>> 6 / 3
2.0
```

Auf jede Eingabe reagiert Python mit der berechneten Antwort.

Die Leerzeichen zwischen den Rechenzeichen und den Zahlen sind nicht unbedingt notwendig, dienen aber der besseren Übersicht.

Soweit kann Python wie ein Taschenrechner verwendet werden.

Es können auch mehrere Rechenoperationen in einer einzigen Zeile berechnet werden.
Wird eine andere als die Punkt-vor-Strich-Rechenregel benötigt, so müssen Klammern `(` und `)` gesetzt werden.

Im folgenden Beispiel werden zwei Aufgaben berechnet die durch unterschiedliche Klammern unterschiedliche Ergebnisse liefern.

```python
>>> 6 / 3 + 3
5.0
>>> (6 / 3) + 3
5.0
>>> 6 / (3 + 3)
1.0
```

Die erste Eingabe ist ganz ohne Klammern.
Python macht dann automatisch die klammern so, wie sie in der zweiten Eingabe sind.
Das Ergebnis ist beide Male `5.0`.
In der dritten Eingabe sind die Klammern so, dass sie `3 + 3` umschließen.
Nun rechnet Python zuerst die Klammer aus, um dann 6 durch (3 + 3) = 6 zu teilen.
Das Ergebnis ist nun `1.0`.

> ### Übungen
> 
> Lösen Sie die folgenden Aufgaben mit Python:
> 
> > Wichtig: berechnen Sie das Ergebnis mit dem Computer, nicht im Kopf.
> 
> > Wichtig: Kommazahlen werden mit einem Punkt geschrieben nicht mit einem Komma.
> 
> 
> 1. Dividieren Sie die Zahlen `79` und `13`
> 1. Addieren Sie die Zahlen `2.5` und `11.5`
> 1. Multiplizieren Sie `2.7` mit `5`
> 1. Berechne das Quadrat aus `65`
> 1. Berechnen Sie das Ergebnis von `5` mal `3` und das ganze plus `2`
> 1. Berechnen Sie das Ergebnis von `3` plus `2` und das ganze mal `5`

[Weiter zum nächsten Abschnitt](02Speichern.md) |