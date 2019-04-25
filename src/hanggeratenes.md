# Eintragen der richtig geratenen Buchstaben

{back} {inhalt} {chapter} {next}

Da jetzt die schon geratenen Buchstaben abgespeichert sind kann man nun die Buchstaben auch nur anzeigen, wenn die Buchstaben schon erraten sind. Hierzu muss nochmals die Funktion `drawlines` verändert werden. Zuerst müssen die gefundenen Buchstaben an die Funktion weiter gegeben werden. Dann muss die Funktion jedes Mal zuerst die kompletten Sachen von dieser Schildkröte löschen. Das ist mit `s.clear()` möglich. Dann müssen die Striche und Buchstaben neu und entsprechend dem aktuellen Stand gezeichnet werden.

```python
def drawlines(geratenes):
  s.clear()
  s.penup()
  s.goto(-200, 350)
  s.pendown()
  for buchstabe in wort:
    s.forward(10)
    if buchstabe in geratenes:
      s.write(buchstabe, align="center", font="arial 12 bold")
    s.forward(10)
    s.penup()
    s.forward(20)
    s.pendown()
```

In der `s.write` Zeile sind noch ein paar Parameter hinzu gefügt, sodass jetzt die Buchstaben größer und schöner sind.

Jedesmal nachdem ein Tipp abgegeben wurde muss wieder `drawlines` aufgerufen werden. Da nach einem Tipp erneut gefragt werden muss, ohne dass der nächste Schritt gemacht wird muss die Frage solange wiederholt werden, bis ein Fehler passiert.

```python

for schritt in schritte:
  buchstabe = turtle.textinput("Hangman", "Welchen Buchstaben tippen Sie?") or ""
  while buchstabe in wort:
    gefunden = gefunden + buchstabe
    drawlines(gefunden)
    buchstabe = turtle.textinput("Hangman", "Welchen Buchstaben tippen Sie?") or ""
  else:
    schritt()
```

{back} {inhalt} {chapter} {next}
