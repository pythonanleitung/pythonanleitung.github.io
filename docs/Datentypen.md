# Datentypen

[Zurück: Kapitel 4 - Fehlermeldungen](Fehler.md) |  [Home](README.md) |  [Weiter: Kapitel 6 - Eingaben](Eingaben.md) | 

Ziel dieses Kapitels ist es zu verstehen, wie der Computer die Welt sieht. So wie wir Menschen verschiedene Sprachen sprechen, so gibt es für den Computer auch verschieden interpretierte Inhalte.

Bis jetzt wurden zwei Datentypen verwendet. Zahlen (`1, 2, 3, 445, 1.2`) und Text (`"hallo", "tschüss", "a", 'a', "2"`). Zahlen werden einfach als zahlen geschrieben. Um Gleitkommazahlen zu schreiben, muss man einen Punkt statt ein Komma schreiben: `1.2`. Text ist zwischen einfachen `'` (Auf der Tastatus ein großes `#`) oder doppelten `"` (eine große `2`) Anführungszeichen. Es ist python egal, wie lange ein Text ist. Er muss jedoch in einer Zeile geschrieben sein. Soll ein Text über mehrere Zeilen gehen, so muss man dreifache Anführungszeichen verwenden: `"""`. Der darauf folgende Text ist alles Teil des Textes bis erneut drei Anführungszeichen folgen.

Ein Beispiel hierfür:

```python
a = """Das ist ein Meer,
ein Textmeer,
ein Meer aus Text,
durch mehr Text.
"""
print(a)
```

ergibt ausgeführt:

```python
>>> %Run gru.py
Das ist ein Meer,
ein Textmeer,
ein Meer aus Text,
durch mehr Text.
```

## Umwandlung von Datentypen

Wichtig ist auch noch zu bemerken, dass die zahl `2` verschieden ist von dem Buchstaben `"2"`. Soll etwas zu einem Text verwandelt werden, so kann der Befehl `str` verwendet werden (`str` ist die Kurzform von String, was die englische Bezeichnung für einen solchen Text ist). Etwas in eine ganze Zahl verwandeln funktioniert mit `int` (für Integer). Soll etwas in eine Gleitkommazahl verwandelt werden verwendet man den Befehl `float` (für floating point number).

Beispiele für diese Verwandlungen:

```python
>>> float("13.5")
13.5
>>> int("15")
15
>>> str(23)
'23'
>>> int(str(23))
23
>>> int(5.6)
5
```

In der letzten Umformung ist zu beachten, dass nicht gerundet wird, sondern einfach die Kommastellen abgeschnitten werden.

> ### Beachte
>   * Text hat Anführungszeichen und kann beliebiges enthalten.
>   * Zahlen haben keine Anführungszeichen.
>   * Dezimalzahlen müssen mit Punkten statt Kommas aufgeschrieben werden.



> ### Übungen
>   Speichern Sie diese Übung unter dem Namen `typen.py`.
>   1. Speichern Sie in den Variablen mit den Namen `eis`, `zwerg`, `drache` die Werte `45`, `93`, `"lo"`
>   2. Multiplizieren Sie `eis` und `zwerg`, geben Sie das Ergebnis mit `print` aus.
>   3. Multiplizieren Sie `eis` und `drache`, geben Sie das Ergebnis mit `print` aus.
>   4. Addieren Sie `eis` und `Drache`, und geben Sie das Ergebnis aus. Wenn ein Fehler auftritt schauen Sie nocheinmal oben nach woran es liegen könnte: das Ergebniss sollte `45lo` sein.

[Zurück: Kapitel 4 - Fehlermeldungen](Fehler.md) |  [Home](README.md) |  [Weiter: Kapitel 6 - Eingaben](Eingaben.md) | 
