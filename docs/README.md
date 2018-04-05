# Pythonanleitung
Eine sehr einfache Aleitung Python zu lernen.

# Was ist Python
Python ist eine Programmiersprache. Mit Python können alle Programme geschrieben werden (Spiele, Musikspieler, Texteditor usw.).


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
Wird nun die Eingabe durch zweimaliges drücken von `Enter` bestätigt, erscheint, wie erwartet, der Text `wird angezeigt`.

## Kurze Bemerkung zur **Einrückung**

Python verwendet verschieden starke Einrückungen, um die Zusammengehörigkeit von Befehlen zu markieren. Ist also zum Beispiel eine Zeile nach dem `if` Befehl mehr eingerückt als das `if` selbst, so gehört diese Zeile zu diesem `if`. Einrückungen sind immer notwendig nach einem Doppelpunkt und andersherum sind Doppelpunkte immer notwendig vor Einrückungen. Auch innerhalb eines eingerückten Bereiches kann wieder ein `if` vorkommen. Der Eingerückte teil des inneren `if`s muss dann noch weiter eingerückt werden.

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

Alternativ kann man natürlich auch eine wahre Bedingung einstellen, welche dem Text in `print` widerspricht:
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
> 1. Schreibe ein if, welches als Bedingung `True` hat und im Wahrheitsfall `"richtig so!"` ausgibt.
> 2. Schreibe ein if, welches als Bedingung `False` hat und im Sonstfall `"Sonstfall False"` ausgibt.

# Eingaben mit Input

Bis jetzt waren die Programme so, dass sie immer dasselbe Ergebnis hatten.
Das heißt, wurde ein Programm gestartet, so zeigt es immer dieselben Ausgaben,
es sei denn, das Programm wurde verändert.
Um langsam Richtung sinnvolles Programm zu gehen, kann der Befehl `input`
verwendet werden. Dieser nimmt als Argument eine Frage, also einen Text,
welcher auf dem Bildschirm erscheinen soll, danach wartet er auf eine Eingabe.
Das was hier eingegeben wird, gibt er zurück.

Zum Beispiel:
```python3
>>> input("Grußwort ")
Grußwort Hallo
'Hallo'
```

Zunächst wird der Befehl `input("Grußwort ")` eingegeben. Dann Antwortet der Computer mit `Grußwort ` und wartet nun auf eine Eingabe. Es kann nun zum Beispiel `Hallo` eingegeben werden. Was immer man hier eingibt, der Computer antwortet nun genau mit diesem eingegebenen.

Statt es direkt wieder auszugeben, kann man das eingegebene auch verwenden zum Beispiel:

```python3
>>> "hallo" == input("Grußwort ")
Grußwort hallo
True
```

Es wurde hier `"hallo"` verglichen mit der Eingabe (`hallo`) und es kommt `True` also wahr heraus. Wird in der Zeile, in der der Computer nach einem Grußwort fragt nicht `hallo` eingegeben, sondern etwas anderes kommt das Ergebnis `False`, also falsch heraus. Ein Beispiel hierzu:

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

Die beiden Beispiele verdeutlichen, einmal die Eingabe `hallo`, welche `True` ergibt, und einmal die Eingabe `nö`, welche `False` ergibt. Je nach Ergebnis wird `hallo` oder `nicht hallo` ausgegeben.

# Speichern in eine Datei

Da das ständige erneut Tippen auf Dauer nicht besonders effizient ist, kann man den Programmcode von Python in eine Datei abspeichern und dann diese Datei ausführen.

Hierzu wird zunächst die Textbearbeitung geöffnet (Windowstaste drücken, `textbearbeitung` eingeben, und mit `Enter` bestätigen - Vorsicht nicht Libreoffice öffnen). Dann wird der Python Code eingegeben und die Datei unter `hallo.py` im "Persönlichen Ordner" abgespeichert. Der Inhalt von `hallo.py` kann dann zum Beispiel so aussehen:

### Dateiname: `hallo.py`
```python3
if "hallo" == input("Grußwort "):
    print("hallo")
else:
    print("nicht hallo")
```

Noch einmal überprüfen, ob man gespeichert hat, dann kann man das Programm im
Terminal ausführen.
Der Befehl lautet: `python3 hallo.py`.

Es fragt nach einem Grußwort und gibt dann die entsprechende Antwort, wie schon vorher.

> Wenn Python noch von vorherigen Experimenten läuft, kann man keine Programme
> ausführen, sondern nur Python code eingeben.
>
> Zeigt der Computer in der untersten Zeile noch `>>>` an, ist Python noch
> gestartet und muss beendet werden. Am Ende der vom Computer
> geschriebenen Zeile sollte ein `$` stehen.
> Falls alles nicht klappt einfach das Terminal schließen und neu starten.


```
user@computer ~$ python3 hallo.py 
Grußwort hallo
hallo
user@computer ~$ python3 hallo.py 
Grußwort nö
nicht hallo
```

# Thonny

Da der Wechsel zwischen Terminal und Editor lästig sein kann, gibt es auch ein Programm Thonny welches diese Funktionen in sich vereint. Thonny ist speziell für Schüler und Studenten geschrieben. Es kann gestartet werden mit Windowstaste → Eingabe `thonny` → `Enter`.

Nach dem Start sieht Thonny so aus:

![Screenshot Thonny](/img/ThonnyLeer.png)

Direkt unter dem Menü befinden sich die wichtigsten Funktionen als Buttons.

![Screenshot Thonny](/img/ThonnyButtons.png)

 1. Eine neue Datei anlegen
 2. Eine Datei öffnen
 3. Die Datei speichern
 4. "Play-Button" das Programm ausführen
 5. Das Programm Schritt für Schritt ausführen.
 6. Beim Schrittweisen ausführen einen großen Schritt machen.
 7. Beim Schrittweisen ausführen einen kleinen Schritt machen.
 8. So ähnlich wie 6.
 9. "Stopp-Button" das Programm beenden, wenn es Probleme gibt und das Ausführen
    nicht mehr funktioniert so hilft es oft das alte Programm zu beenden und dann neu starten.
 
Wurde ein Programm geöffnet und gestartet, so sieht Thonny so aus:

![Screenshot Thonny](/img/BildschirmfotoThonny.png)

Der große Teil des Fensters wird ausgefüllt von dem Inhalt der geöffneten Datei. Alles was hier steht, ist das was wir in dem Textbearbeitungsfenster gemacht haben.

Darunter ist ein kleinerer Teil, welcher das derzeitige Programm im interaktiven Modus ausführt. Das heißt hier erscheinen Ausgaben, wenn man auf "play" drückt und man muss die Eingaben tätigen, wenn im Programm ein `input` steht. Dieses Fenster ist also so wie das Terminal, beziehungsweise das `python3`.

Alle weiteren Programme und Beispiele werden in Thonny ausgeführt. Beginnen die Beispiele mit `>>>` so sind sie für das untere interaktive  "Ausprobier"-Fenster gedacht. Beginnen sie direkt mit Python-Befehlen, so sind sie für das obere Fenster gedacht.

Immer wenn etwas im oberen Fenster verändert wurde, so muss wieder der "Play-Button" gedrückt werden.

# Variablen

Bis jetzt haben wir den Wert der Eingabe immer sofort verwendet. Wenn aber der Wert an zwei Stellen im Programm verwendet werden soll, also zum Beispiel um einmal zu überprüfen, ob die Eingabe `hallo` ist und einmal um zu prüfen, ob die Eingabe `tschüss` ist, so muss der Wert zwischengespeichert werden. Hierzu werden Variablen verwendet. Um eine Variable zu erstellen, schreibt man einen beliebigen Namen der Variablen (ohne Leerzeichen) und dann, nach einem `=` den Wert den die Variable haben soll.

Einige Beispiele:
```python3
x = 5
y = 'hallo'
z = 5 + 5
dreingabe = input("was soll gespeichert werden? ")
```

In der ersten Zeile wird die Zahl `5` in die Variable `x` eingespeichert. Die zweite Zeile speichert `'hallo'` in `y`. Die Dritte das Ergebnis der Berechnung `5 + 5` in `z`. Und die vierte den eingegebenen Text in die Variable `dreingabe`.

Diese Variablen können nun verwendet werden hat man zum Beispiel mit `x = 5` der Variablen `x` den Wert `5` gegeben, so kann man nun statt der dritten Zeile auch `z = x + x` schreiben und wird wieder in `z` denselben Wert (`10`) gespeichert haben. Möchte man den Wert einer Variablen ausgeben, so kann man dies mit `print` tun. Um den Wert von `z` zu erfahren also `print(z)`.

> ### Aufgabe
>  1. Erstelle eine Python-Datei `Beispielaufgabe.py` welche die Variablen `x, y, z` die Werte `34, 24, 'hallo'` zuweist.
>  2. Berechne nun in die Variable `summe` die summe von `x` und `y`.
>  3. Gebe alle vier variablen mit `print` aus.
>  4. Führe die Datei mit `python3` aus und löse alle Fehlermeldungen.

## Verwendung von Variablen

Um nun also das Programm zu schreiben, welches zwischen `hallo` und `tschüss` unterscheidet, kann man nun das vorherige `if` Beispiel anpassen:

```python3
gru = input("Welcher gruß? ")
if gru == "hallo":
     print("Guten Tag")
elif gru == "tschüss":
     print("Auf Wiedersehen")
else:
     print("Ich habe Sie leider nicht verstanden")
```
In diesem Beispiel wird eine weitere Option der `if`-Ausdrücke verwendet: `elif`. Dieses steht für `else if` und bedeutet: Falls nicht die erste Bedingung dann vielleicht diese Bedingung also am ehesten zu übersetzen mit "oder wenn". Zwischen einem `if` und einem `else` können beliebig viele `elif` stehen.

Wird dies in eine Datei `gru.py` gespeichert und diese dann (zweimal) ausgeführt, so entsteht folgende Ausgabe:

    dietrich@lehrer ~$ python3 gru.py
    Welcher gruß? hallo
    Guten Tag
    dietrich@lehrer ~$ python3 gru.py
    Welcher gruß? nö
    Ich habe Sie leider nicht verstanden

# Fehler

Vermutlich ist schon aufgefallen, wie kleinlich python auf die Korrektheit
achtet. sobald auch nur ein einzelner Buchstabe falsch ist, bekommt man einen
Fehler zu sehen. Die Fehler geben meistens einen Hinweis darüber was falsch
sein könnte. Im Folgenden sind ein Paar Beispiele von Fehlern:

### NameError

Mögliche Gründe:

  * Eine Variable wurde nicht definiert
  * Es wurden Anführungszeichen um Text vergessen
  * Ein Befehl wurde falsch geschrieben (Achtung auch Groß- und Kleinschreibung
    ist wichtig)

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

Bis jetzt wurden zwei Datentypen verwendet. Zahlen (`1, 2, 3, 445, 1.2`) und Text (`"hallo", "tschüss", "a", 'a', "2"`). Zahlen werden einfach als zahlen geschrieben. Um kommazahlen zu schreiben, muss man einen Punkt statt ein Komma schreiben: `1.2`. Text ist zwischen einfachen `'` (großes `#`) oder doppelten `"` (große `2`) Anführungszeichen. Es ist python egal, wie lange ein Text ist. Er muss jedoch in einer Zeile geschrieben sein. Soll ein Text über mehrere Zeilen gehen, so muss man dreifache Anführungszeichen verwenden: `"""`. Der darauf folgende Text ist alles Teil des Textes bis erneut drei Anführungszeichen folgen.

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
Wichtig ist auch noch zu bemerken, dass die zahl `2` verschieden ist von dem Buchstaben `"2"`. Soll etwas zu einem Text verwandelt werden, so kann der Befehl `str` verwendet werden (`str` ist die Kurzform von String, was die englische Bezeichnung für einen solchen Text ist). Etwas in eine ganze Zahl verwandeln funktioniert mit `int` (für Integer). Soll etwas in eine Gleitkommazahl verwandelt werden verwendet man den Befehl `float` (für floating point number).

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
In der letzten Umformung ist zu beachten, dass nicht gerundet wird, sondern einfach die Kommastellen abgeschnitten werden.

> ### Beachte
>   * Text hat Anführungszeichen und kann beliebiges enthalten.
>   * Zahlen haben keine Anführungszeichen.
>   * Dezimalzahlen müssen mit Punkten statt Kommas aufgeschrieben werden.

# Ein Passwortprogramm

Die nun  gestellte Aufgabe ist es ein Passwort zu erraten, welches im Programm festgelegt wird. Zunächst speichern wir das zu erratende Passwort in einer Variablen.
```
geheim = "Döner"
```
Es werden drei Versuche gegeben das Passwort zu erraten:
```
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

# Zufall

Oft ist es notwendig eine zufällige Zahl zu generieren. Python benötigt ein Modul,
um dies zu tun. Module werden mit dem `import` Befehl geladen. Das Modul,
welches viele Zufalls relevanten Funktionen beherbergt heißt `random`.
Dieses kann geladen werden mit `import random`.

Nachdem das Modul geladen ist, kann mit `random.randint(0,100)` eine zufällige
ganze Zahl zwischen `0` und `100` ausgewählt werden.

Beispiel:

```python3
>>> import random
>>> random.randint(0,100)
48
>>> random.randint(0,100)
78
>>> random.randint(0,100)
17
```

Diese Zufallszahl kann natürlich auch in eine Variable gespeichert werden mit `zahl = random.randint(0,100)`.

> ### Aufgabe
> 1. Schreibe ein Programm, welches eine Zufallszahl zwischen `1` und `10` generiert, und diese ausgibt.
> 2. Erweitere dieses Programm so, dass es dreimal nach einem Tipp fragt, für diese Zahl () die Ausgabe der zahl sollte natürlich entfernt werden.
> 3. Speichere den Tipp in eine Variable und gebe jedes Mal aus, ob der Tipp zu groß oder zu klein war.
> Beispiel:
> ```python3
> Tipp: 5
> zu klein
> Tipp: 8
> zu groß
> Tipp: 7
> richtig
> ```

# Wiederholungen

Oftmals in einem Computerprogramm soll der Computer Dinge wiederholen. Dies kann eine bestimmte Anzahl sein oder es kann etwas wiederholt werden so lange bis eine Bedingung nicht mehr zutrifft.

## While
Für den zweiten Fall ist der Befehl `while` vorgesehen. While wiederholt einen Programmteil so oft, bis die Bedingung nicht mehr zutrifft. Ein abstraktes Beispiel:

```python3
while <Bedingung>:
    print("ich werde wiederholt")
```

Ein konkretes Beispiel, welches immer wieder nach einer Eingabe fragt, bis `"ende"` eingegeben wurde:

```python3
eingabe = input("Eingabe: ")
while not (eingabe == "ende"):
    eingabe = input("Eingabe: ")
```

Wird dieses Programm ausgeführt so muss man irgendwann ende eingeben, sonst beendet sich das Programm nicht.

> ### Aufgabe
> Verändere das Zahlen-Rate-Programm so, dass man beliebig viele Versuche hat beim Raten. Verwende hierzu `while`.
> Erweitere das Programm so, dass es Zufallszahlen zwischen `0` und `100` verwendet.
