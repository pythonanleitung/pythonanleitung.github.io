# Bedingtes ausführen

[Zurück: Kapitel 4 - Eingaben in Turtle](TurtleInput.md) |  [Home](README.md) |  [Weiter: Kapitel 6 - Wiederholungen mit While](Wiederholungenwhile.md) | 

Alle Programmiersprachen bieten die Möglichkeit, einen Befehl nur dann auszuführen, wenn eine bestimmte Bedingung eintritt.

Ein Programm soll einen bestimmten Satz nur sagen, wenn der Benutzer auf einen `input()` Befehl `hallo` sagt:

```python
print("Sagen Sie hallo:")
antwort = input()
if antwort == "hallo":
   print("Einen lieben Gruß")
```

Ausgabe:
```
wird angezeigt
```

Das `if` in diesem Beispiel ist das Kommando, welches den bedingten Aufruf einleitet. Das `antwort == "hallo"` ist die Bedingung, es gibt noch viele [weitere Möglichkeiten Bedingungen zu schreiben](Bedingungen.md). Es vergleicht das, was in der Variablen antwort steht mit dem Wort `"hallo"` ist beides das gleiche wird die folgende Zeile ausgefürt, ist es etwas verschiedenes wird die folgende Zeile übersprungen.

Nach der Bedingung folgt immer ein **Doppelpunkt**. Die nächste Zeile wird ein stück weiter eingerückt als das `if`.

## Kurze Bemerkung zur **Einrückung**

Python verwendet verschieden starke Einrückungen, um die Zusammengehörigkeit von Befehlen zu markieren. Ist also zum Beispiel eine Zeile nach dem `if` Befehl mehr eingerückt als das `if` selbst, so gehört diese Zeile zu diesem `if`. Einrückungen sind immer notwendig nach einem Doppelpunkt und andersherum sind Doppelpunkte immer notwendig vor Einrückungen. Auch innerhalb eines eingerückten Bereiches kann wieder ein `if` vorkommen. Der Eingerückte teil des inneren `if`s muss dann noch weiter eingerückt werden.

> ### Merke
> Immer einrücken nach einem Doppelpunkt und immer wenn `Thonny` nicht automatisch einrückt, wo es eigentlich einrücken sollte, fehlt davor ein Doppelpunkt.

Beispiel:

```python
print("Sagen Sie einen Tag:")
freitag = input()
if freitag == "Montag":
  print("Geben Sie eine Note")
  zeit = input()
  if zeit == "6":
     print("Falsch Montage sind die Besten!")

print("Viel Spass!")
```

Ausgabe:
```
>>> %Run tage.py
Sagen Sie einen Tag:
Montag
Geben Sie eine Note
6
Falsch Montage sind die Besten!
Viel Spass!
```

```
>>> %Run tage.py
Sagen Sie einen Tag:
Dienstag
Viel Spass!
```

In einer grafischen Programmiersprache `scratch` wird ein if als "Klammer" dargestellt.

Dieses Bild ist nur, falls Sie sich das dann besser vorstellen können. Falls nicht ignorieren Sie es.

![Geschachteltes If in Scratch](img/ifInScratch.png)

Das `if`, welches zu falls übersetzt wird, ist eine Klammer. Alles was innerhalb dieses `if`s ist, wird nur ausgeführt, wenn die Bedingung des `if`s zutrifft. Dieses "innerhalb" wird in Python durch "stärker eingerückt", also mehr Leerzeichen am Anfang der Zeile deutlich gemacht. Natürlich kann auch innerhalb eines `if`s ein zweites `if` stehen.

## Wenn → Dann → Ansonsten

Oft wird es benötigt, dass ein bestimmter Befehl ausgeführt wird, wenn eine Bedingung zutrifft, ansonsten ein anderer Befehl. Der Befehl hierzu ist `else`. Auch auf `else` folgt ein Doppelpunkt und weitere eingerückte Befehle.

> Notiz: Sowohl nach `if` als auch nach `else` muss mindestens ein eingerückter Befehl kommen. Also man kann  im folgenden Beispiel **keines** der beiden `print`s weglassen (man kann sie aber durch beliebige andere Befehle ersetzen).

```python
gruß = input()
if gruß == "hallo":
   print("Ich antworte mit Hallo")
else:
   print("Bah! - zu unfreundlich!")
```

Logischerweise ist `else` nur nach einem fertigen `if` sinnvoll.

Man sieht hier, dass dem Computer die Bedeutung der Worte völlig gleichgültig ist er folgt nur der Logik der Befehle:



# Kombinieren mit dem bisher gelernten

Natürlich kann dieses `if` mit allem zuvor gelernten und mit allem kommenden kombiniert werden. Die folgenden Beispiele kombinieren den `input`-Befehl mit den `if`-Abfragen.

# Beispiel: ein Grußprogramm

Ein Programm, das auf `hallo` und `tschüss` unterschiedlich reagiert:

```python
print("Welcher Gruß? ")
gru = input()
if gru == "hallo":
     print("Guten Tag")
elif gru == "tschüss":
     print("Auf Wiedersehen")
else:
     print("Ich habe Sie leider nicht verstanden")
```
In diesem Beispiel wird eine weitere Option der `if`-Ausdrücke verwendet: `elif`. Dieses steht für `else if` und bedeutet: Falls nicht die erste Bedingung dann vielleicht diese Bedingung also am ehesten zu übersetzen mit "oder wenn". Zwischen einem `if` und einem `else` können beliebig viele `elif` stehen, aber vorher muss immer ein `if` und stehen.

Wird dies in eine Datei `gru.py` gespeichert und diese dann (dreimal) ausgeführt, so entsteht folgende Ausgabe:

```bash
>>> %Run gru.py
Welcher Gruß? hallo
Guten Tag
>>> %Run gru.py
Welcher Gruß? tschüss
Auf Wiedersehen
>>> %Run gru.py
Welcher Gruß? tschau
Ich habe Sie leider nicht verstanden
```

> ### Übung Grußprogramm
> Schreiben und testen Sie ein Programm, welches nach einem Gruß fragt und je nach Gruß unterschiedlich reagiert.

> Speichern Sie dieses Programm unter dem Namen `gru.py`.

## Beispiel: ein "Passwortprogramm"

Die nun  gestellte Aufgabe ist es ein Passwort zu erraten, welches im Programm festgelegt wird. Zunächst speichern wir das zu erratende Passwort in einer Variablen.
```python
geheim = "Döner"
```
Es werden drei Versuche gegeben das Passwort zu erraten unter Verwendung des Eingabe-Befehls aus dem vorherigen Abschnitt:
```python
geheim = "Döner"

print("Versuch1: ")
if geheim == input():
    print("geschafft")
else:
    print("Versuch2: ")
    if geheim == input():
        print("geschafft")
    else:
        print("Versuch3: ")
        if geheim == input():
            print("geschafft")
        else:
            print("nicht geschafft")
```

Beispiel:
```
Versuch1:
hi
Versuch2:
Döner
geschafft
```

Dieses Programm ist natürlich nicht so, wie der Computer ein Passwort abfragen würde, da das Passwort für jeden lesbar im Programm steht. Normalerweise wird das Passwort nur verschlüsselt abgespeichert.

> ### Übung Passwortprogramm
>
> Schreiben Sie ein Programm, welches drei Versuche gewährt ein Passwort zu erraten. Speichern Sie dieses Programm in der Datei `passwort.py`.
>


> ### Übung Zahlenratespiel
> Schreiben Sie ein Programm, welches 3 Versuche gewährt eine Zahl zu erraten. Dieses Programm kann sehr ähnlich zu dem Grußprogramm geschrieben werden.
> Speichern Sie dieses Programm unter `ratemal.py`.
>
> Gehen Sie Schrittweise vor:
> 1. Schreiben Sie ein Programm, welches nach einer Zahl fragt und diese ausgibt.
> 2. Testen Sie das Programm ob es tut was es soll.
> 3. entfernen Sie die Ausgabe, und fügen Sie stattdessen ein `if` und `else` ein, welches auf die Eingabe reagiert.
>> Vorsicht beim Vergleichen: der Buchstabe einer Zahl ist nicht gleich der Zahl. Zum Beispiel ist `"2" == 2` unwahr also `False`. Um diese beiden Werte sinnvoll zu vergleichen, muss der Buchstabe `"2"` zur Zahl `2` konvertiert werden: `int("2") == 2` ([mehr](Datentypen.md#umwandlung-von-datentypen)).

[Zurück: Kapitel 4 - Eingaben in Turtle](TurtleInput.md) |  [Home](README.md) |  [Weiter: Kapitel 6 - Wiederholungen mit While](Wiederholungenwhile.md) | 
