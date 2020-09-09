# Schrittweises Zeichnen des Galgenmännchens

Zunächst müssen die einzelnen Schritte des Galgenmännchens einzeln von jeweils einer Funktion gezeichnet werden. Erstellen Sie hierfür ein eigenes Modul `hangmanschritte`. Wenn sie sich jetzt fragen, woher sie denn wissen sollen wie das geht? Das heißt so viel wie erstellen Sie eine neue Datei mit dem Namen `hangmanschritte.py` und lösen Sie darin die hier gestellten Aufgaben.

Wenn alles gezeichnet ist sollte das Ganze so aussehen:

![Hangman Schritte](img/hangmansteps.png)

Natürlich darf diese Grafik nach belieben angepasst werden, sodass jeder etwas anderes aufhängt... oder es kann die gewaltfreie Version gemacht werden, indem man eine Blume schrittweise zeichnet.

### Anfangs-Vorlage

```python
import turtle
t = turtle.Pen()
t.shape("turtle")

# Funktionen zwischen diesen beiden Zeilen definieren

# Funktionen Ende

zeichenliste = []

# Testen
if __name__ == "__main__":
    for schritt in zeichenliste:
      schritt()
```

### Eine Funktion für den Hügel

Jede zu erstellende Funktion muss:

1. erstellt werden
2. zu der zeichenliste hinzugefügt werden

Als Beispiel wird zunächst der Hügel gezeichnet.

```python

def huegel():
  t.left(90)
  t.penup()
  t.backward(200)
  t.pendown()
  t.circle(100,180)
  t.right(90)
  t.penup()
  t.backward(100)
  t.right(90)
  t.forward(100)
  t.pendown()
```

Dann der `zeichenliste` hinzu gefügt:

```python
zeichenliste = [huegel]
```

Erst wenn die Funktion der `zeichenliste` hinzugefügt ist, wird sie auch gezeichnet.

### Jeder Schritt des Galgenmännchens braucht eine Funktion

Nachdem nun der Hügel gezeichnet werden kann muss für jeden der Schritte eine Funktion geschrieben werden. Es ist sinnvoll, am Ende jeder Funktion zu dem Punkt zu fahren, wo die nächste Funktion weiter machen muss.

Die zu schreibenden Funktionen sind:

  * `huegel`
  * `senkrechte`
  * `waagerechte`
  * `stütze` (kleiner diagonaler Stützbalken zwischen senkrechter und waagerechter)
  * `seil`
  * `kopf` (mit Gesicht)
  * `körper`
  * `arme`
  * `beine`

> ### Notiz
> Die findigen werden ein seltsames `if` bemerkt haben. Diese bedeutet, dass der Programmcode nur dann ausgeführt wird, wenn das Modul direkt gestartet wird, nicht aber, wenn es in ein anderes Modul eingebunden wird.

### Noch noch eine Lösung für den `senkrechte`-Schritt

Diese Funktion ist viel einfacher:

```python
def senkrechte():
    t.forward(300)
    t.right(90)
```

Die Funktionen müssen alle zwischen den beiden Kommentarzeilen sein. Wurde auch die Senkrechte Funktion definiert kann sie zu `zeichenliste` hinzu gefügt werden:

```python
zeichenliste = [huegel, senkrechte]
```

Es sollte jetzt kein Problem mehr sein alle nötigen Funktionen zu Definieren.
