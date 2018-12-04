# Eingaben mit Input

[Zurück: Kapitel 5 - Datentypen](Datentypen.md) |  [Home](README.md) |  [Weiter: Kapitel 7 - Fallunterscheidung](BedingtesAusfuehren.md) | 

Ziel dieses Kapitels ist es die eigenen Programme etwas "interaktiver" zu machen.

> ### Übungen
> 1. Schreiben Sie ein Programm, welches nach einer Kommazahl fragt
> 1. Speichern Sie dieses Programm in der Datei `kommazahl.py`
> 2. Diese Zahl zu einer Kommazahl umwandelt (Vorsicht statt `int` muss ein anderer Befehl verwendet werden)
> 3. Die Kommazahl mit `2.5` multipliziert und ausgibt
> 4. Die Kommazahl in eine ganzzahlige Zahl umwandelt, indem die Kommastellen abgeschnitten werden
> 5. Die Ganze Zahl mit `6` multipliziert und ausgibt
> 6. Geben Sie die Ergebnisse jeweils mit einem Antwortsatz aus.
>
Beispieldurchlauf des Übungsaufgabenprogramms:
```python
>>> %Run hallo.py
Gib eine Kommazahl:
6.7
Das zweieinhalbfache der Kommazahl ist: 16.75
Die ganze Zahl ist: 6
Die ganze Zahl mal sechs ist: 30
```

Bis jetzt waren die Programme so, dass sie immer dasselbe Ergebnis hatten.
Das heißt, wurde ein Programm gestartet, so zeigt es immer dieselben Ausgaben,
es sei denn, das Programm wurde verändert.
Um langsam Richtung sinnvolles Programm zu gehen, kann der Befehl `input`
verwendet werden. Dieser wartet auf eine Eingabe des Benutzers.
Das was der Benutzer eingegeben hat kann zum Beispiel in eine [Variable](Variablen.md) gespeichert werden.

> ### Hinweis
>
> 1. Der obere Teil von Thonny ist zum **erstellen** des Programms da
> 2. der untere Teil ist zur **interaktion** mit dem Programm da.

Zum Beispiel folgendes Programm im **oberen Teil**:
```python
print("Sag fein Hallo: ")
eing = input()
print(eing)
```

Ergibt folgende Ausgabe im **unteren Teil**, wenn das Programm gestartet wurde.

```python
>>> %Run hallo.py
Sag fein Hallo:
```

Zunächst gibt der Computer `Sag fein Hallo: ` aus. Daraufhin wartet er darauf, dass man im **unteren Fenster** eine Eingabe macht und diese mit Enter bestätigt. Es kann nun zum Beispiel `Hallo` eingegeben werden.

```python
>>> %Run hallo.py
Sag fein Hallo:
Hallo
Hallo
```

Was immer man hier eingibt, wird in der Variablen `eing` zwischengespeichert.
Mit der dritten Zeile des Programms im oberen Fenster wird nun dieser zwischengespeicherte Wert ausgegeben.

Statt es direkt wieder auszugeben, kann man das eingegebene auch verwenden zum Beispiel:

```python
print("Sag fein Hallo: ")
eing = input()
print("auch ich sage fünf mal: ", eing * 5)
```

Oder für eine Rechnung verwenden... Die `input`-Funktion gibt das eingegebene als Wort zurück. Soll also die Eingabe zum Beispiel in einer Rechnung verwendet werden, dann muss man die Eingabe erst zu einer Zahl (int - Integer) konvertieren (genauer [hier](03Variablen.md#umwandlung-von-datentypen).

```python
print("Gib eine ganze Zahl: ")
eing = input()
umg = int(eing)
print("Das siebenundfünfzigfache der Zahl ist: ", umg * 57)
```


[Zurück: Kapitel 5 - Datentypen](Datentypen.md) |  [Home](README.md) |  [Weiter: Kapitel 7 - Fallunterscheidung](BedingtesAusfuehren.md) | 
