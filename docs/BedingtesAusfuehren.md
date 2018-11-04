# Bedingtes ausführen

[Zurück: Kapitel 6 - Eingaben](Eingaben.md) |  [Home](README.md) |  [Weiter: Kapitel 8 - Schildkröten](Turtle.md) | 

Alle Programmiersprachen bieten die Möglichkeit, einen Befehl nur dann auszuführen, wenn eine bestimmte Bedingung eintritt.

Ein einfaches Beispiel ist somit:

```python
if 1 == 1:
   print("wird angezeigt")
```

Ausgabe:
```
wird angezeigt
```

Ein einfaches Beispiel ist somit:

```python
if 1 == 2:
   print("wird nicht angezeigt")
```

Ausgabe:
``` 

```

Das `if` in diesem Beispiel ist das Kommando, welches den bedingten Aufruf einleitet. Das `1 == 1` bzw. `1 == 2` ist die Bedingung.
Im ersten Fall also die wahre Bedingung, im zweiten die unwahre Bedingung.
Nun folgt ein **Doppelpunkt**. Die nächste Zeile wird eingerückt.

> ### Übungen
> 1. Schreiben Sie ein `if`, welches eine wahre Bedingung hat und mit print `"Wahr"` ausgibt
> 2. Schreiben Sie ein zweites `if`, welches eine unwahre Bedingung hat und mit print `"Unwahr"` ausgibt
> 
> Was gibt das erste, was gibt das zweite aus? Schreiben Sie die antwort als Kommentar in den code.

## Kurze Bemerkung zur **Einrückung**

Python verwendet verschieden starke Einrückungen, um die Zusammengehörigkeit von Befehlen zu markieren. Ist also zum Beispiel eine Zeile nach dem `if` Befehl mehr eingerückt als das `if` selbst, so gehört diese Zeile zu diesem `if`. Einrückungen sind immer notwendig nach einem Doppelpunkt und andersherum sind Doppelpunkte immer notwendig vor Einrückungen. Auch innerhalb eines eingerückten Bereiches kann wieder ein `if` vorkommen. Der Eingerückte teil des inneren `if`s muss dann noch weiter eingerückt werden.

> ### Merke
> Immer einrücken nach einem Doppelpunkt und immer wenn `Thonny` nicht automatisch einrückt, wo es eigentlich einrücken sollte, fehlt davor ein Doppelpunkt.

Beispiel:

```python
if 1 == 1:
  print("einsundeins")
  if 5 == 6:
     print("fünfundsechs")
     if 3 == 3:
         print("dreiunddrei")
```

Ausgabe:
```
einsundeins
```

In einer grafischen Programmiersprache `scratch` wird der obere Code so dargestellt, dass deutlicher ist, was wie zusammen gehört. Dieses Bild ist nur, falls Sie sich das dann besser vorstellen können. Falls nicht ignorieren Sie es.

![Geschachteltes If in Scratch](img/ifInScratch.png)

Das `if`, welches zu falls übersetzt wird, ist eine Klammer. Alles was innerhalb dieses `if`s ist, wird nur ausgeführt, wenn die Bedingung des `if`s zutrifft. Dieses "innerhalb" wird in Python durch "stärker eingerückt", also mehr Leerzeichen am Anfang der Zeile deutlich gemacht. Natürlich kann auch innerhalb eines `if`s ein zweites `if` stehen.

## Wenn → Dann → Ansonsten

Oft wird es benötigt, dass ein bestimmter Befehl ausgeführt wird, wenn eine Bedingung zutrifft, ansonsten ein anderer Befehl. Der Befehl hierzu ist `else`. Auch auf `else` folgt ein Doppelpunkt und weitere eingerückte Befehle.

> Notiz: Sowohl nach `if` als auch nach `else` muss mindestens ein eingerückter Befehl kommen. Also man kann  im folgenden Beispiel **keines** der beiden `print`s weglassen (man kann sie aber durch beliebige andere Befehle ersetzen).

```python
if 1 == 2:
   print("wird nicht gezeigt")
else:
   print("wird gezeigt")
```

Ausgabe:
```
wird angezeigt
```
Logischerweise ist `else` nur nach einem fertigen `if` sinnvoll.

Alternativ kann man natürlich auch eine wahre Bedingung einstellen, welche dem Text in `print` widerspricht. Man sieht hier, dass dem Computer die Bedeutung der Worte völlig gleichgültig ist er folgt nur der Logik der Befehle:

```python
if 1 == 1:
   print("wird nicht gezeigt")
else:
   print("wird gezeigt")
```

Ausgabe:
```
wird nicht angezeigt
```

> ### Aufgabe
> 1. Schreiben Sie folgende Aufgaben in die Datei `ifelse.py`
> 1. Schreibe ein if, welches als Bedingung `64 == 64` hat und im **Wahrheitsfall** `"Richtig so!"` ausgibt.
> 2. Schreibe ein zweites if, welches als Bedingung `1 == 5000` hat und im **Sonstfall** `"Sonstfall!"` ausgibt.
> 
> Wird dieses Programm ausgeführt produziert es folgende Ausgabe:
> 
```
>>> %Run ifelse.py
Richtig so!
Sonstfall
```

# Bedingungungen schreiben

Neben den normalen Rechenoperationen kann Python auch Vergleichsoperationen. Diese geben immer entweder wahr (`True`) oder falsch (`False`) zurück:

| Operator (Zeichen) | ist `True`(wahr) wenn... |
| `A == B` | A ist gleich wie B |
| `A < B` | A ist kleiner als B |
| `A > B` | A ist größer als B |
| `A != B` | A ist ungleich B |
| `A <= B` | A ist kleiner oder gleich B |
| `A >= B` | A ist größer oder gleich B |

Außerdem kann man noch zwei Wahrheitswerte mit den folgenden Befehlen kombinieren:

| Operator (Zeichen) | ist `True`(wahr) wenn... |
| `A and B` | ist wahr, wenn A und B wahr sind |
| `A or B` | ist wahr, wenn A oder B oder beide wahr sind |
| `not A` | ist wahr, wenn A unwahr (`False`) ist |

> ### Übung
> sind die folgenden Ausdrücke wahr oder falsch? - Schreiben Sie die Ergebnisse in die Datei `ifelse.py` mit. Nach einem `#` wird der Rest der Zeile vom Computer ignoriert.
> 
> Für die erste Zeile ist die Lösung also: `5 < 6 # Wahr (True)`
> 
> 1. `5 < 6`
> 1. `5 != 6`
> 1. `5 <= 6`
> 1. `True and True`
> 1. `False or True`
> 1. `3 < 4 and 4 < 5`
> 1. `not (3 != 4)`
>
> Prüfen Sie die Ergebnisse, die Sie im Kopf herausgefunden haben mit Python im ausprobierfenster nach.

# Kombinieren mit dem bisher gelernten

Natürlich kann dieses `if` mit allem zuvor gelernten und mit allem kommenden kombiniert werden. Die folgenden Beispiele kombinieren den `input`-Befehl mit den `if`-Abfragen.

# Beispiel: ein Grußprogramm

Ein Programm, das auf `hallo` und `tschüss` unterschiedlich reagiert:

```python
gru = input("Welcher gruß? ")
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
Welcher gruß? hallo
Guten Tag
>>> %Run gru.py
Welcher gruß? tschüss
Auf Wiedersehen
>>> %Run gru.py
Welcher gruß? tschau
Ich habe Sie leider nicht verstanden
```

## Beispiel: ein "Passwortprogramm"

Die nun  gestellte Aufgabe ist es ein Passwort zu erraten, welches im Programm festgelegt wird. Zunächst speichern wir das zu erratende Passwort in einer Variablen.
```python
geheim = "Döner"
```
Es werden drei Versuche gegeben das Passwort zu erraten unter Verwendung des Eingabe-Befehls aus dem vorherigen Abschnitt:
```python
geheim = "Döner"

if geheim == input("Versuch1: "):
    print("geschaft")
elif geheim == input("Versuch2: "):
    print("geschaft")
elif geheim == input("Versuch2: "):
    print("geschaft")
else:
    print("nicht geschafft")
```

Beispiel:
```
Versuch1: hi
Versuch2: Döner
geschaft
```

Dieses Programm ist natürlich nicht so, wie der Computer ein Passwort abfragen würde, da das Passwort für jeden lesbar im Programm steht. Normalerweise wird das Passwort nur verschlüsselt abgespeichert.

> ### Übungen
> Schreiben Sie ein Programm, welches 3 Versuche gewährt eine Zahl zu erraten.
> 
> Vorsicht beim Vergleichen: der Buchstabe einer Zahl ist nicht gleich der Zahl. Zum Beispiel ist `"2" == 2` unwahr also `False`. Um diese beiden Werte sinnvoll zu vergleichen, muss der Buchstabe `"2"` zur Zahl `2` konvertiert werden ([mehr](03ZZDatentypen.md#umwandlung-von-datentypen)). 

[Zurück: Kapitel 6 - Eingaben](Eingaben.md) |  [Home](README.md) |  [Weiter: Kapitel 8 - Schildkröten](Turtle.md) | 
