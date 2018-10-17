# Eingaben mit Input

[Zurück zum vorherigen Abschnitt](03ZZDatentypen.md) | [Zurück zur ersten Seite](README.md)

Bis jetzt waren die Programme so, dass sie immer dasselbe Ergebnis hatten.
Das heißt, wurde ein Programm gestartet, so zeigt es immer dieselben Ausgaben,
es sei denn, das Programm wurde verändert.
Um langsam Richtung sinnvolles Programm zu gehen, kann der Befehl `input`
verwendet werden. Dieser nimmt als Argument eine Frage, also einen Text,
welcher auf dem Bildschirm erscheinen soll, danach wartet er auf eine Eingabe.
Das was hier eingegeben wird, gibt er zurück.

Der obere Teil von Thonny ist zum erstellen des Programms da, der untere Teil ist zur Interaktion mit dem Programm da.

Zum Beispiel folgendes Programm im oberen Teil:
```python
eing = input("Sag fein Hallo: ")
print(eing)
```

Ergibt folgende Ausgabe im unteren Teil, wenn das Programm gestartet wurde.

```python
>>> %Run hallo.py
Sag fein Hallo:
```

Zunächst gitb der Computer nur `Sag fein Hallo: ` aus. Daraufhin wartet er darauf, dass man im unteren Fenster eine Eingabe macht und diese mit Enter bestätigt. Es kann nun zum Beispiel `Hallo` eingegeben werden.

```python
>>> %Run hallo.py
Sag fein Hallo: Hallo
Hallo
```

Was immer man hier eingibt, wird in der Variablen `eing` zwischengespeichert.
Mit der zweiten Zeile des Programms im oberen Fenster wird nun dieser zwischengespeicherte Wert ausgegeben.

Statt es direkt wieder auszugeben, kann man das eingegebene auch verwenden zum Beispiel:

```python
eing = input("Sag fein Hallo: ")
print("auch ich sage: ", eing)
```

Oder für eine Rechnung verwenden... Die `input`-Funktion gibt das eingegebene als Wort zurück. Soll also die Eingabe zum Beispiel in einer Rechnung verwendet werden, dann muss man die Eingabe erst zu einer Zahl (int - Integer) konvertieren (genauer [hier](03Variablen.md#umwandlung-von-datentypen).

```python
eing = input("Gib eine ganze Zahl: ")
umg = int(eing)
print("Das siebenundfünfzigfache der Zahl ist: ", umg * 57)
```

> ### Übungen
> 1. Schreiben Sie ein Programm, welches nach einer Kommazahl fragt
> 1. Speichern Sie dieses Programm in der Datei `kommazahl.py`
> 2. Diese Zahl zu einer Kommazahl umwandelt (Vorsicht statt `int` muss ein anderer Befehl verwendet werden)
> 3. Die Kommazahl mit `2.5` multipliziert und ausgibt
> 4. Die Kommazahl in eine ganzzahlige Zahl umwandelt, indem die Kommastellen abgeschnitten werden
> 5. Die Ganze Zahl mit `6` multipliziert und ausgibt
> 6. Geben Sie die Ergebnisse jeweils mit einem Antwortsatz aus.

Beispieldurchlauf des Übungsaufgabenprogramms:
```python
>>> %Run hallo.py
Gib eine Kommazahl: 6.7
Das zweieinhalbfache der Kommazahl ist:  16.75
Die ganze Zahl ist: 6
Die ganze Zahl mal sechs ist: 30
```

[Weiter zum nächsten Abschnitt](05BedingtesAusfuehren.md) |
