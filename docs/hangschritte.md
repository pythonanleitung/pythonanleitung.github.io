# Schrittweises Zeichnen des Galgenmännchens

 [Inhalt](README.md) |  [Kapitel](hangman.md) |  [Weiter: 22 - Immer wieder abfragen](hangabfrage.md) | 

Zunächst müssen die einzelnen Schritte des Galgenmännchens einzeln von jeweils einer Funktion gezeichnet werden.

### Eine Funktion für den Hügel

Als Beispiel wird zunächst der Hügel gezeichnet.

```python

def hügel():
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

### Jeder Schritt brauch eine Funktion

Nachdem nun der Hügel gezeichnet werden kann muss für jeden Der Schritte eine Funktion geschrieben werden. Es ist sinnvoll, am Ende jeder Funktion zu dem Punkt zu fahren, wo die nächste Funktion weiter machen muss.

Die zu schreibenden Funktionen sind:

  * `hügel`
  * `senkrechte`
  * `waagerrechte`
  * `stütze` (kleiner diagonaler Stützbalken zwischen senkrechter und waagerechter)
  * `seil`
  * `kopf` (mit Gesicht)
  * `körper`
  * `arme`
  * `beine`

Um das schon erstellte zu testen müssen die Funktionen jeweils aufgerufen werden. Die Zeilen außer Kopf sind noch mit einer `#` auskommentiert (also deaktiviert). Sobald die entsprechende Funktion geschrieben ist kann das `#` entfernt werden:

```python
hügel()
#senkrechte()
#waagerechte()
#stütze()
#seil()
#kopf()
#körper()
#arme()
#beine()
```

### Die Funktion für die senkrechte

Diese Funktion ist viel einfacher:

```python
def senkrechte():
    t.forward(300)
    t.right(90)
```

Die Funktionen müssen alle vor den Aufrufen sein. Das heißt am einfachsten ist, man importiert turtle usw. dann definiert man die Funktionen und erst danach kommen die Aufrufe. Wurde auch die Senkrechte Funktion definiert kann das `#` vor `senkrechte()` entfernt werden.

Definieren Sie nun alle Funktionen.

Wenn alles gezeichnet ist sollte das Ganze so aussehen:

![Hangman Schritte](img/hangmansteps.png)

Natürlich darf diese Grafik nach belieben angepasst werden, sodass jeder etwas anderes aufhängt... oder es kann die gewaltfreie Version gemacht werden, indem man eine Blume zeichnet.

 [Inhalt](README.md) |  [Kapitel](hangman.md) |  [Weiter: 22 - Immer wieder abfragen](hangabfrage.md) | 
