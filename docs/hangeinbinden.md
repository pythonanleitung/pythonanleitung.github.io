# Einbinden der Wortlistendatei

[Zurück: 2.3 - Geheimwortliste](hanggeheimliste.md) |  [Inhalt](README.md) |  [Kapitel](hangman.md) |  [Weiter: 2.5 - Abspeichern der Tipps](hangtipsspeich.md) | 

Da nun die Wortlistendatei erstellt ist, kann diese nun in der ursprünglichen `hangman.py`-Datei eingebunden werden. Der Einbindebefehl wurde schon öfter verwendet, ohne dass Sie es wussten. Außer der Wortliste wird nun auch noch das Zufallsmodul eingebunden.

```python
import wortliste
import random
```

da wir beides noch nicht verwenden erscheint noch keine Veränderung. Es sollte aber auch kein Fehler produziert werden, wenn das Programm ausgeführt wird.

Nun kann ein zufälliges Wort ausgewählt werden:

```python
wort = random.choice(wortliste.wörter)
```

Um jetzt für jeden der Buchstaben eine Linie zu erstellen machen wir uns ein zweites turtle, welches nur für das Zeichnen der Linien und das schreiben der Buchstaben zuständig ist. Dieses muss dann für jeden Buchstaben eine kurze Linie zeichnen. Zur späteren einfacheren Wiederverwendung wird hierzu eine Funktion definiert.

```python
s = turtle.Pen()
s.hideturtle()
def drawlines():
  s.penup()
  s.goto(-200, 350)
  s.pendown()
  for buchstabe in wort:
    s.forward(20)
    s.penup()
    s.forward(20)
    s.pendown()

drawlines()
```

Um erstmal zu sehen, was passiert, schreiben wir die Buchstaben einfach noch mit rein.

```python
def drawlines():
  ...
  for buchstabe in wort:
    s.forward(15)
    s.write(buchstabe)
    s.forward(15)
    s.penup()
    ...
```

Im Folgenden sollen natürlich die Buchstaben nur dann erscheinen, wenn sie schon einmal getippt wurden.

[Zurück: 2.3 - Geheimwortliste](hanggeheimliste.md) |  [Inhalt](README.md) |  [Kapitel](hangman.md) |  [Weiter: 2.5 - Abspeichern der Tipps](hangtipsspeich.md) | 
