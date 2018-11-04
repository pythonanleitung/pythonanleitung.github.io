# Der Befehl for

{back} {inhalt} {next}

For ist der Befehl, der "für jedes" wiederholt. Also zum Beispiel für jeden Buchstaben, oder für jede Zahl in einer Liste `[1,2,3,4,5]`.

```python
for i in "hallo":
    print(i * 5)
```

Produziert die folgende Ausgabe:

```
>>> %Run forletter.py
hhhhh
aaaaa
lllll
lllll
ooooo
```

Wie man am Ergebnis sehen kann speichert das `for` den ersten Buchstaben von `"hallo"` in die Variable `i` und führt dann damit das `print` aus. Es wird also fünf mal `h` ausgegeben.

Im nächsten Durchgang speichert das `for` in die selbe Variable `i` den zweiten Buchstaben von `"hallo"` und führt damit das `print` aus. Es erscheint `aaaaa`. Und so weiter.

Ziemlich gleich funktioniert das mit Zahlenlisten:

```python
for i in [1,2,3,4,5,6,7,8,9,524]:
    print(i * 5)
```

Ergibt die Ausgabe:

```
>>> %Run forletter.py
5
10
15
20
25
30
35
40
45
2620
```

{back} {inhalt} {next}
