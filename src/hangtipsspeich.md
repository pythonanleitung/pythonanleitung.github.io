
{back} {inhalt} {chapter} {next}

# Speichern und verwenden der Tipps

Zunächst müssen die Tipps immer abgespeichert werden, dass das Programm immer später auch noch weiß, was schon getippt wurde. Hierzu verwenden wir die in der `for`-Schleife verwendete `turtle.textinput` Funktion.

Der eingegebene Buchstabe muss zunächst in eine Variable gespeichert werden. Dann muss diese Variable zu der Liste der gefundenen Buchstaben hinzu gefügt werden.

```python
gefunden = ""
for schritt in schritte:
  buchstabe = turtle.textinput("Hangman", "Welchen Buchstaben tippen Sie?")
  if buchstabe in wort:
    gefunden = gefunden + buchstabe
  else:
    schritt()
```

{back} {inhalt} {chapter} {next}
