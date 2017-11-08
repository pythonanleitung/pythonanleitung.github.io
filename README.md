# Pythonanleitung
Eine sehr einfache Aleitung Python zu lernen.

# Was ist Python
Python ist eine Programmiersprache. Mit Python können alle Programme geschrieben werden (Spiele, Musikspieler, Texteditor usw.).

# Ein Erstes Beispiel
Python kann in einem Modus verwendet werden, in dem die Programmiersprache immer sofort eine Rückmeldung gibt. Dieser spezielle Modus wird wie folgt gestartet.

Als erstes wird ein Terminal geöffnet. Hierzu wird das entsprechende Programm aus dem Starter ausgewählt.
Zum Beispiel wird die `"Windows"`-Taste gedrückt, dann `terminal` eingegeben und die Auswahl mit `Enter` bestätigt.
Es öffnet sich ein Fenster, in welchem oben in der ersten Zeile etwas steht was mit einem `$ ` aufhört.
Zunächst wird in der ersten Zeile mit `python3` python gestartet.
Der eingegebene Befehl muss mit der `Enter`-Taste bestätigt werden.

Wurde Python gestartet zeigt als erstes seine Version und wer es gemacht hat an.
Danach erscheint auf dem Bildschirm in einer neuen Zeile `>>>`.
Das ist das Zeichen dafür, dass Python gestartet ist und man es nun verwenden kann.
Jede Eingabe, die man in Python macht muss man mit `Enter` bestätigen.
Sollte einmal die Zeile nicht mit `>>>` beginnen so ist etwas mit Python nicht in Ordnung und man startet am besten nochmal vom Anfang des Beispiels.

Hat ein Befehl ein Ergebnis, so wird dieses direkt ausgegeben.
Keine Panik nach dem Beispiel werden die Zeilen einzeln erklärt.

Werden einige Befehle in Python eingegeben könnte das so aussehen:
```python3
$ python3
Python 3.6.2 (default, Sep 22 2017, 08:28:09) 
[GCC 7.2.1 20170915 (Red Hat 7.2.1-2)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 1
1
>>> 1+1
2
```

In Zeile 4 des Beispiels wurde einfach eine Zahl eingegeben.
Python antwortet darauf einfach indem es die selbe Zahl wieder gibt.

In Zeile 6 wird eine einfache Rechenaufgabe in Python gestellt.
Worauf Python diese berechnet und das Ergebnis zurück gibt.

Es können so alle Grundrechenarten verwendet wobei die folgenden Rechenzeichen verwendet werden:
  * Plus: `1 + 2`
  * Minus: `2 - 1`
  * Mal: `3 * 4`
  * Geteilt und Brüche: `6 / 3`

Beispiel:
```python3
$ python3
Python 3.6.2 (default, Sep 22 2017, 08:28:09)
[GCC 7.2.1 20170915 (Red Hat 7.2.1-2)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 1 + 2
3
>>> 2 - 1
1
>>> 3 * 4
12
>>> 6 / 3
2.0
```

Auf jede Eingabe reagiert Python mit der berechneten Antwort.
Die Leerzeichen zwischen den Rechenzeichen und den Zahlen sind nicht unbedingt notwendig, dienen aber der besseren Übersicht.

Soweit kann Python wie ein Taschenrechner verwendet werden.
Es können auch mehrere Rechenoperationen in einer einzigen Zeile berechnet werden.
Wird eine andere als die Punkt vor Strich rechenregel benötigt, so müssen Klammern gesetzt werden.

Im folgenden Beispiel werden zwei Aufgaben berechnet die durch unterschiedliche Klammern unterschiedliche Ergebnisse liefern.

```python3
>>> 6 / 3 + 3
5.0
>>> (6 / 3) + 3
5.0
>>> 6 / (3 + 3)
1.0
```

Die erste Eingabe ist ganz ohne Klammern.
Python macht dann automatisch die klammern so, wie sie in der zweiten Eingabe sind.
Das Ergebnis ist beide Male `5.0`.
In der dritten Eingabe sind die Klammern so, dass sie `3 + 3` umschließen.
Nun rechnet Python zuerst die Klammer aus, um dann 6 durch (3 + 3) = 6 zu teilen.
Das Ergebnis ist nun `1.0`.

> ### Aufgabe
> 1. Berechne das Ergebnis von `5` mal `3` und das ganze plus `2`.
> 2. Berechne das Ergebnis von `3` plus `2` und das ganze mal `5`.

# Bedingtes ausführen
Alle Programmiersprachen bieten die Möglichkeit, einen Befehl nur dann auszuführen, wenn eine bestimmte Bedingung eintrifft.
In Python trifft eine Bedingung ein, wenn sie Wahr (`True`) ist - oder zu `True` ausgewertet wird.
Sie tritt nicht ein, wenn sie zu `False` ausgewertet wird.

Ein einfaches Beispiel ist somit:

```python3
>>> if True:
...     print("wird angezeigt")
...
wird angezeigt
>>>
```

Das `ìf` in diesem Beispiel ist das Kommando, welches den bedingten Aufruf einleitet. Das `True` ist die Bedingung.
In diesem Fall also die Immer wahre Bedingung - man könnte stattdessen auch `1==1` schreiben.
Nun folgt ein **Doppelpunkt**. Die nächste Zeile wird eingerückt. Der `print`-Befehl gibt einfach das ihm zwischen Klammern übergebene aus. Ausgaben, also etwas was das Programm geschrieben hat, haben keine Punkte oder Pfeile am Anfang der Zeile.
Wird nun die Eingabe durch zweimaliges drücken von `Enter` bestätigt, erscheint wie erwartet der Text `wird angezeigt`.

## Kurze Bemerkung zur **Einrückung**

Python verwendet verschieden starke Einrückungen, um die Zusammengehörigkeit von Befehlen zu markieren. Ist also zum Beispiel eine Zeile nach dem `if` Befehl mehr eingerückt als das `if` selbst, so gehört diese Zeile zu diesem `if`. Einrückungen sind immer notwendig nach einem Doppelpunkt und andersherum sind Doppelpunkte immer notwendig vor Einrückungen. Auch innerhalb eines eingerückten Bereiches kann wieder ein `if`vorkommen. Der Eingerückte teil des inneren `if`s muss dann noch weiter eingerückt werden.

## Wenn → Dann → Ansonsten

Oft wird es benötigt, dass ein bestimmter Befehl ausgeführt wird, wenn eine Bedingung zutrifft, ansonsten ein anderer. Der Befehl hierzu ist `else`. Auch `else` braucht andere zugehörige Befehle, das heißt ihm folgt ein Doppelpunkt und die nächste Zeile muss eingerückt werden.

Ein Beispiel:

```python3
>>> if False:
...     print("wird nicht gezeigt")
... else:
...     print("wird gezeigt")
...
wird angezeigt
>>>
```
Logischerweise ist `else` nur nach einem fertigen `if` sinnvoll. Man sieht durch die `>>>`, das if beginnt den Befehl und alles weitere ist Teil dieses Befehls, was durch `...` gezeigt wird.

Alternativ kann man natürlich auch eine Wahre Bedingung einstellen, welche dem Text in `print` wiederspricht:
```python3
>>> if True:
...     print("wird nicht gezeigt")
... else:
...     print("wird gezeigt")
...
wird nicht angezeigt
>>>
```

> ### Aufgabe
> 1. Schreibe ein if welches als Bedingung `True` hat, und im Wahrheitsfall `"richtig so!"` ausgibt.
> 2. Schreibe ein if welches als Bedingung `False` hat, und im Sonstfall `"Sonstfall False"` ausgibt.

# Eingaben mit `input`

Bis jetzt waren die Programme so, dass sie immer das selbe Ergebniss hatten. Um langsam richtung sinnvolles Programm zu gehen, kann der Befehl `input` verwendet werden. Dieser nimmt als Argument eine Frage, also einen Text, welcher auf dem Bildschirm erscheinen soll, danach wartet er auf eine Eingabe. Das was hier eingegeben wird gibt er zurück.

Zum Beispiel:
```python3
>>> input("Grußwort ")
Grußwort Hallo
'Hallo'
```

Zunächst wird der Befehl `input("Grußwort ")` eingegeben. Dann Antwortet der Computer mit `Grußwort ` und wartet nun auf eine Eingabe. Es kann nun zum Beispiel `Hallo` eingegeben werden. Was immer man hier eingibt, der Computer antwortet nun genau mit diesem eingegebenen.

Statt es direkt wieder auszugeben kann man das eingegebene auch verwenden zum Beispiel:

```python3
>>> "hallo" == input("Grußwort ")
Grußwort hallo
True
```

Es wurde hier `"hallo"` verglichen mit der Eingabe (`hallo`) und es kommt `True` also wahr heraus. Wird in der Zeile in der der Computer nach einem Grußwort fragt nicht `hallo` eingegeben, sondern etwas anderes kommt das Ergebnis `False` also falsch heraus. Ein Beispiel hierzu:

```python3
>>> "hallo" == input("Grußwort ")
Grußwort nö
False
```

Das so erzeugte `True` oder `False` kann in einem `if` verwendet werden:

```python3
>>> if "hallo" == input("Grußwort "):
...     print("hallo")
... else:
...     print("nicht hallo")
... 
Grußwort hallo
hallo
>>> if "hallo" == input("Grußwort "):
...     print("hallo")
... else:
...     print("nicht hallo")
... 
Grußwort nö
nicht hallo
```

Die beiden Beispiele verdeutlichen, einmal die Eingabe `hallo` welche `True` ergibt, und einmal die Eingabe `nö` welche `False` ergibt. Je nach Ergebnis wird `hallo` oder `nicht hallo` ausgegeben.

# Speichern in eine Datei

Da das ständige erneut Tippen auf Dauer nicht besonders effizient ist, kann man den Programmcode von Python in eine Datei abspeichern und dann diese Datei ausführen.

Hierzu wird zunächst die Textbearbeitung geöffnet (Vorsicht nicht Libreoffice). Dann wird der Python Code eingegeben und die Datei unter `hallo.py` im Persönlichen Ordner abgespeichert. Der Inhalt von `hallo.py` kann dann zum Beispiel so aussehen:

### Dateiname: `hallo.py`
```python3
if "hallo" == input("Grußwort "):
    print("hallo")
else:
    print("nicht hallo")
```

Nocheinmal überprüfen ob man gespeichert hat, dann kann man das Programm im Terminal ausführen (Vorsicht nicht in Python - am Ende der vom Computer geschriebenen Zeile sollte ein `$` stehen. Falls dies nicht so ist einfach das Terminal schließen und neu starten).

Dann kann mit dem Befehl `python3 hallo.py` das selbst geschriebene Programm gestartet werden. Es Fragt nach einem Grußwort und gibt dann die entsprechende Antwort, wie schon vorher.

```
user@computer ~$ python3 hallo.py 
Grußwort hallo
hallo
user@computer ~$ python3 hallo.py 
Grußwort nö
nicht hallo
```

# Variablen

Bis jetzt haben wir den Wert der Eingabe immer sofort verwendet. Wenn aber der Wert an zwei Stellen im Programm verwendet werden soll, also zum Beispiel um einmal zu überprüfen, ob die Eingabe `hallo` ist und einmal um zu prüfen ob die Eingabe `tschüss` ist, so muss der Wert zwischengespeichert werden. Hierzu werden Variablen verwendet. Um eine Variable zu erstellen schreibt man einen Beliebigen Namen der Variablen (ohne Leerzeichen) und dann, nach einem `=` den Wert den die Variable haben soll.

Einige Beispiele:
```python3
x = 5
y = 'hallo'
z = 5 + 5
dreingabe = input("was soll gespeichert werden? ")
```

In der ersten Zeile wird die Zahl `5` in die Variable `x` eingespeichert. Die zweite Zeile speichert `'hallo'` in `y`. Die Dritte das Ergebnis der Berechnung `5 + 5` in `z`. Und die vierte den eingegebenen Text in die Variable `dreingabe`.

Diese Variablen können nun verwendet werden hat man zum Beispiel mit `x = 5` der Variablen `x` den Wert `5` gegeben, so kann man nun statt der dritten Zeile auch `z = x + x` schreiben und wird wieder in `z` den selben Wert (`10`) gespeichert haben. Möchte man den Wert einer Variablen ausgeben, so kann man dies mit `print` tun. Um den Wert von `z` zu erfahren also `print(z)`.

> ### Aufgabe
>  1. Erstelle eine Python-Datei `Beispielaufgabe.py` welche die Variablen `x, y, z` die Werte `34, 24, 'hallo'` zuweist.
>  2. Berechne nun in die Variable `summe` die summe von `x` und `y`.
>  3. Gebe alle vier variablen mit `print` aus.
>  4. Führe die Datei mit `python3` aus und löse alle Fehlermeldungen.

## Verwendung von Variablen

Um nun also das Programm zu schreiben, welches zwischen `hallo` und `tschüss` unterscheidet kann man nun das vorherige `if` Beispiel anpassen:

```python3
gru = input("Welcher gruß? ")
if gru == "hallo":
     print("Guten Tag")
elif gru == "tschüss":
     print("Auf Wiedersehen")
else:
     print("Ich habe Sie leider nicht verstanden")
```
In diesem Beispiel wird eine weitere Option der `if`-Ausdrücke verwendet: `elif`. Dieses steht für `else if` und bedeutet Falls nicht die erste Bedingung dann vielleicht diese Bedingung also am ehesten zu übersetzen mit "oder wenn". Zwischen einem `if` und einem `else` können beliebig viele `elif` stehen.

Wird dies in eine Datei `gru.py` gespeichert und diese dann (zwei mal) ausgeführt, so entsteht folgende Ausgabe:

    dietrich@lehrer ~$ python3 gru.py
    Welcher gruß? hallo
    Guten Tag
    dietrich@lehrer ~$ python3 gru.py
    Welcher gruß? nö
    Ich habe Sie leider nicht verstanden

# Fehler

Vermutlich ist schon aufgefallen, wie kleinlich python auf die korrektheit achtet. sobald auch nur ein einzelner Buchstabe falsch ist bekommt man einen Fehler zu sehen. Die Fehler geben meistens einen Hinweis darüber was falsch sein könnte.

### NameError

Mögliche Gründe:

  * Eine Variable wurde nicht definiert
  * Es wurden Anführungszeichen um Text vergessen
  * Ein Befehl wurde falsch geschrieben (Achtung auch Groß- und Kleinschreibung ist wichtig)
Beispiel:
```
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
  * Erwartete, aber nicht vorhandene Einrückung (intendation)
  * Vorhandene, aber nicht erwartete Einrückung (intendation)
  * ...

Im folgenden Beispiel wurden Doppelpunkte vergessen:
```
>>> if True
  print("True")
  
  File "<pyshell>", line 1
    if True
          ^
SyntaxError: invalid syntax
```



# Datentypen

Bis jetzt wurden zwei Datentypen verwendet. Zahlen (`1, 2, 3, 445, 1.2`) und Text (`"hallo", "tschüss", "a", 'a', "2"`). Zahlen werden einfach als zahlen geschrieben. Um kommazahlen zu schreiben, muss man einen Punkt statt ein Komma schreiben: `1.2`. Text ist zwischen einfachen `'` (großes `#`) oder doppelten `"` (große `2`) Anführungszeichen. Es ist python egal wie lange ein Text ist. Er muss jedoch in einer Zeile geschrieben sein. Soll ein Text über mehrere Zeilen gehen, so muss man dreifache Anführungszeichen verwenden: `"""`. Der darauf folgende Text ist alles Teil des Textes bis erneut drei Anführungszeichen folgen.

Ein Beispiel hierfür:
```python3
a = """Das ist ein Meer,
ein Textmeer,
ein Meer aus Text,
durch mehr Text.
"""
print(a)
```
ergibt ausgeführt:
```bash
$ python3 t.py
Das ist ein Meer,
ein Textmeer,
ein Meer aus Text,
durch mehr Text.
```
Wichtig ist auch noch zu bemerken, dass die zahl `2` verschieden ist von dem Buchstaben `"2"`. Soll etwas zu einem Text verwandelt werden, so kann der befehl `str` verwendet werden (`str` ist die kurzform von string, was die Englische Bezeichnung für einen solchen Text ist). Soll etwas in eine ganze Zahl verwandelt werden, so verwendet man den Befehl `int` (für integer). Soll etwas in eine Kommazahl verwandelt werden verwendet man den Befehl `float` (für floating point number).

Beispiele für diese Verwandlungen:
```python3
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
In der letzten Umformung ist zu beachten, dass nicht gerundet wird, sondern einfach die Kommazahl abgeschnitten.

> ### Beachte
> Text hat Anführungszeichen und kann beliebiges enthalten. Zahlen haben keine Anführungszeichen. Dezimalzahlen müssen mit Punkten statt Kommas aufgeschrieben werden.
