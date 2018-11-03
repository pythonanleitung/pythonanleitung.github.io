# For Schleifen

{back} {inhalt} {next}

Möchte man etwas eine bestimmte Anzahl oft wiederholen, so könnte man dies mit einer
`while` schleife tun, muss dann aber mit zählen und aufhören, wenn die gewünschte Anzahl von Durchläufen erreicht ist.

Deutlich einfacher geht dies mit `for`:

```python
for x in range(5):
    print("Durchlauf Nummer:", x)
```

Dieses Programm wiederholt 5 mal den `print`-Befehl. Dabei ist das x im ersten durchlauf `0`, dann `1` usw. bis `4`. Die Nummer `5` wird nie erreicht.

Das `for` kann auch dazu verwendet werden, etwas für jedes Element einer Liste einmal aufzurufen. Zum Beispiel so:

```python
for el in ["blue", "green", "yellow"]:
    print("A ", el, "bird")
```

Es wird also ausgegeben: `A blue bird`, `A green bird`, `A yellow bird`


{back} {inhalt} {next}
