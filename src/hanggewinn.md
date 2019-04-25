
# Gewinnen und Verlieren

{back} {inhalt} {chapter} {next}

Um das Spiel "Gewinnen" oder "Verlieren" zu können schreiben wir eine Funktion `gewonnen`, die `True` zurück gibt, wenn das spiel gewonnen ist. Die Funktion nimmt die tipps und das Geheimwort und Prüft, ob alle Buchstaben aus dem Geheimwort schon getippt wurden. `pass` ist ein Befehl der an eine Stelle geschrieben wird, an die ein Befehl muss, der Computer aber nichts tun soll.

```python
def gewonnen(tipps, geheimwort):
  win = True
  for let in geheimwort:
    if let in tipps:
      pass
    else:
      win = False
  return win
```

Diese Funktion muss jetzt noch verwendet werden. Zum einen muss die Fragerei abgebrochen werden, wenn das Wort fertig getippt wurde, zum anderen muss am Ende noch das Ganze Wort in grün angezeigt werden, wenn das Spiel gewonnen ist, oder in rot, wenn es verloren ist. Zunächst das rot und grüne ausgeben ganz am ende der Datei werden folgende Zeilen eingefügt.

```python
if gewonnen(gefunden, wort):
  s.color("green")
  drawlines(wort)
else:
  s.color("red")
  drawlines(wort)
````

Das Abbrechen der Fragerei ist wesentlich schwieriger. Sobald das Spiel gewonnen ist müssen beide Schleifen (`for` und `while`) abgebrochen werden. Der Befehl `break` bricht eine schleife ab. Es muss also in jeder der beiden Schleifen ein `if` welches entscheidet ob das Spiel gewonnen ist und dann das break ausführt.

```python
for schritt in schritte:
  buchstabe = turtle.textinput("Hangman", "Welchen Buchstaben tippen Sie?") or ""
  while buchstabe in wort:
    gefunden = gefunden + buchstabe
    if gewonnen(gefunden, wort):
        break
    drawlines(gefunden)
    buchstabe = turtle.textinput("Hangman", "Welchen Buchstaben tippen Sie?") or ""
  else:
    schritt()
  if gewonnen(gefunden, wort):
      break
```

{back} {inhalt} {chapter} {next}
