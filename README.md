# Pythonanleitung
Eine sehr einfache Aleitung Python zu lernen.

# Was ist Python
Python ist eine Programmiersprache. Mit Python können alle Programme geschrieben werden (Spiele, Musikspieler, Texteditor usw.).

# Ein Erstes Beispiel
Python kann in einem Modus verwendet werden, in dem die Programmiersprache immer sofort eine Rückmeldung gibt.
Um diesen Modus zu Starten kann man in einem Terminal einfach `python3` eingeben.

In dem sich öffnenden Prompt können alle Python befehle eingegeben werden.
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

In Zeile 4 des Beispiels wurde einfach eine Zahl eingegeben.
Python antwortet darauf einfach indem es die selbe Zahl wieder gibt.

In Zeile 6 wird eine einfache Rechenaufgabe in Python gestellt.
Worauf Python diese berechnet und das Ergebnis zurück gibt.

Es können so alle Grundrechenarten verwendet wobei die folgenden Rechenzeichen verwendet werden:
  * Plus mit `1 + 2`
  * Minus mit `2 - 1`
  * Mal mit `3 * 4`
  * Geteilt und Brüche mit mit `6 / 3`

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

## Wenn Dann Sonst

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


