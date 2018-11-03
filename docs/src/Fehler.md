# Fehler

{back} {inhalt} {next}

Vermutlich ist schon aufgefallen, wie kleinlich python auf die Korrektheit
achtet. Sobald auch nur ein einzelner Buchstabe falsch ist, bekommt man einen
Fehler zu sehen. Die Fehler geben meistens einen Hinweis darüber was falsch
sein könnte.

Der Fehler ist so aufgebaut, dass er zuerst die Position des Fehlers angibt. Hierzu werden einige Dateien gelistet. Erst in der letzten Zeile erscheint der eigentliche Fehler. Meistens reicht es die letzten beiden Zeilen des Fehlers zu betrachten.

Im Folgenden sind ein paar Beispiele von Fehlern:

### NameError

Mögliche Gründe:

  * Eine Variable wurde nicht definiert
  * Es wurden Anführungszeichen um Text vergessen
  * Ein Befehl wurde falsch geschrieben (Achtung auch Groß- und Kleinschreibung
    ist wichtig)

Beispiel:

```python
>>> print(z)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'z' is not defined
```

### SyntaxError
Dieser Fehler ist relativ allgemein. Netterweise zeigt Python manchmal mit einem `^` auf die Stelle an der es den Fehler vermutet.

Ursachen:

  * Doppelpunkt vergessen
  * Klammerfehler
  * Anführungszeichenfehler
  * Erwartete, aber nicht vorhandene Einrückung (intendation), also zu wenig Leerzeichen am Anfang der Zeile.
  * Vorhandene, aber nicht erwartete Einrückung (intendation), also zu viele Leerzeichen am Anfang der Zeile
  * ...

Im folgenden Beispiel wurden Doppelpunkte vergessen:

```python
>>> if True
  print("True")
  
  File "<pyshell>", line 1
    if True
          ^
SyntaxError: invalid syntax
```

### TypeError

Dieser Fehler sagt, dass der Computer zum Beispiel eine Zahl und einen Buchstaben nicht zusammen addieren kann. (Zahl mit Zahl, und Buchstabe mit Buchstabe funktioniert).

Ursachen:

  * Vergessen ein Wort zu einer Zahl zu verwandeln - Siehe nächste Überschrift.
  * Vergessen eine Variable zu aktualisieren
  * ...

Im folgenden Beispiel wird versucht eine Zahl `1` und einen Buchstaben `'i'` zu addieren:

```python
>>> 1 + 'i'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

{back} {inhalt} {next}
