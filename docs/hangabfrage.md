# Die Abfrage des Hangman

[Zurück: 2.1 - Eine Funktion für jeden Galgenschritt](hangschritte.md) |  [Inhalt](README.md) |  [Kapitel](hangman.md) |  [Weiter: 2.3 - Geheimwortliste](hanggeheimliste.md) | 

Nachdem wir jetzt das Bild zeichnen können kommt nun die Abfrage. Der Computer soll den Menschen nach einem Buchstaben fragen, welcher dann in einem späteren Schritt weiter verarbeitet wird.

Die dafür verwendete Funktion `turtle.textinput()` kennen Sie schon aus vorherigen Kapiteln.

Es soll jetzt aber nicht nur einmal gefragt werden, sondern immer wieder. Der `turtle.textinput()` muss also mit `for` wiederholt werden. Die Anzahl der Wiederholungen der Frage ist genau die Anzahl der Zeichenschritte.

Das heißt zuerst schreiben wir alle Zeichenschritte in eine Liste:

```python
schritte = [hügel, senkrechte, waagerechte, stütze, seil, kopf, körper, beine, arme]
```

Zunächst können die Funktionsaufrufe (die am Anfang mit `#` begonnen haben) gelöscht werden. Diese waren nur zum Testen der Zeichnungen.

Für jeden Zeichenschritt fragen wir einmal. Gleichzeitig können wir für jede Frage auch gleich das entsprechende zeichnen:

```python
for schritt in schritte:
  turtle.textinput("Hangman", "Welchen Buchstaben tippen Sie?")
  schritt()
```

Erstmal wird, egal was man eingibt, immer der nächste Schritt gezeichnet.

[Zurück: 2.1 - Eine Funktion für jeden Galgenschritt](hangschritte.md) |  [Inhalt](README.md) |  [Kapitel](hangman.md) |  [Weiter: 2.3 - Geheimwortliste](hanggeheimliste.md) | 
