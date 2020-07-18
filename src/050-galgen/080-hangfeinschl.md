# Feinschliff am Spiel



Vielleicht ist schon aufgefallen, dass das Spiel zwischen großen und kleinen Buchstaben unterscheidet. Das ist unüblich beim Galgenmännchenspiel. Darum sollte das noch angepasst werden. Ein Buchstabe hat die Möglichkeit zu einem Großbuchstaben gemacht zu werden indem `upper` verwendet wird.

Beispiel aus `'a'.upper()` wird `'A'`.

Die `while`-Schleife wird also folgendermaßen angepasst:

```python
while buchstabe.lower() in wort or buchstabe.upper() in wort:
    gefunden = gefunden + buchstabe.lower() + buchstabe.upper()
    …
```

Es sind natürlich noch viele Verbesserungen und kleine Anpassungen möglich, die dieses Spiel besser machen können. Fühlen Sie sich frei zu experimentieren!


