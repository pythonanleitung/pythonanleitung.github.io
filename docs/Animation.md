# Animation

[Zurück: 3.1 - Computerspiele](Computerspiel.md) |  [Inhalt](README.md) |  [Kapitel](snakespiel.md) |  [Weiter: 3.3 - Steuerung](Steuerung.md) | 

Ein Spiel wäre nun relativ langweilig, wenn sich nichts "bewegen" würde. Bei diesem Spiel Soll sich eine Schlange bewegen. Bewegung heißt, dass der Pixel **vor** dem Kopf der Schlange blau wird, und der letzte wieder weiß.

> ### Info
> Computerspiele laufen in frames ab. Also der Computer zeichnet jede Sekunde das komplette Bild was auf dem Bildschirm angezeigt wird mehrere male komplett neu. Das heißt eine Bewegung eines Dings ist eigentlich ein verschobenes neu zeichnen. Oder anders gesagt ein über den Bildschirm "ruckeln". Das Spiel muss nun so gestaltet werden, dass dieses ruckeln als Bewegung wahrgenommen wird. In diesem Snake wird jeder "Ruck" eine halbe Sekunde dauern und die Schlange wird genau einen "Riesenpixel" weiter laufen.

Betrachtet man nun den Ersten Pixel, also den Schlangenkopf und bleiben wir bei diesem Pixel so ist dieser Pixel nach einem Ruck nun der zweite Pixel der Schlange. Man kann feststellen, dass ein Pixel des Kopfes, der gerade Blau wird noch so lange blau ist bis er einmal die gesamte Schlange durchlaufen hat. Der Pixel ist also genau für so viele Rucke blau, wie die Schlange lang ist. Um das umzusetzen schreiben wir in das `s.level` also immer die Zahl, wie viele Rucke ein Pixel noch blau sein soll. Für den Kopfpixel ist dies immer die aktuelle Länge der Schlange. Für den nächsten Pixel ist dies genau eines weniger und für den nächsten noch eines weniger. Wir können also feststellen, dass wir mit jedem Ruck eine eins von jedem levelfeld abziehen müssen.

Um dies zu tun schreiben wir zunächst eine Funktion die jedes Feld minus eins rechnet.

> ### Aufgabe: Alle minus eins
>  * Schreiben Sie eine Funktion namens `ame()`, welche von jedem Pixel im Spielfeld eines abzieht.
>
>    Ein paar Tipps:
>     * Funktionen waren das mit `def`
>     * Verwenden Sie `for i in range(400):` um die Befehle für alle Pixel zu wiederholen.
>     * Sie können von dem i'ten Pixel eins abziehen mit folgender Zeile: `s.level[i] = s.level[i] - 1`
> 
>    Schreiben Sie nun diese `ame`-Funktion.
> 
>  * Generieren Sie ein Testlevel mit folgender Struktur:
> 
>    ![Test Level](img/snaketestlevel.png)
> 
>  * Überprüfen Sie, ob `ame()` funktioniert, indem Sie es bei geöffnetem Spielfenster in den unteren Teil von Thonny eingeben. Nachdem Sie es eingegeben haben, sollte Ihre Schlange jetzt eines kürzer sein.
>
>  * Außerdem stellen Sie fest, dass jetzt der gesamte Hintergrund auch farbig geworden ist und überall `-1` steht. Das ist natürlich der Fall, weil wir auch von allen Nullen (`0` - also weiß) eins abgezogen haben.
>
>  * Es muss nun also mit `if` noch das abziehen beschränkt werden, sodass nur dann abgezogen wird, wenn der dort stehende Wert größer ist als `0`.

# Frames

Wie Oben dargestellt muss diese `ame()`-Funktion jetzt regelmäßig ausgeführt werden. Die meisten Spieleengines bieten hierfür eine Möglichkeit die Funktion als solche zu registrieren. Das heißt wir müssen dem `game`-Modul nur sagen, was es regelmäßig ausfüren soll. Der dafür zuständige Befehl ist: `s.addStep(ame)`

> ### Übung
>
> Fügen Sie den Befehl `s.addStep(ame)` vor s.start zu Ihrem Snake hinzu. Das Ergebnis sollte jetzt so aussehen.
> 
> [Video snake Test](img/snaketest.webm)
> 
> Natürlich verschwindet jetzt die schlange, statt zu laufen. Das ist so, weil noch kein neuer Kopf gesetzt wird.

# Setzen des neuen Kopfes

Soll der Kopf der Schlange gesetzt werden muss zunächst bekannt sein wohin dieser gesetzt werden muss. Dies ist abhängig von der Richtung und der vorherigen Position. Zum Beispiel muss das Feld oberhalb des alten Kopfes angemalt werden, wenn die Schlange nach oben läuft.

Um dies zu ermöglichen muss das Programm sich die Position des Kopfes sowie die Richtung merken:

```python
s.pos = 210
s.dir = 1
```

Nun kann man mithilfe dieser Variablen eine Funktion schreiben, die die neue Kopfposition berechnet, und diesen auch zeichnet:

```python
def neuerKopf():
    s.pos = s.pos + s.dir
    s.level[s.pos] = 5
```

> ### Übung
> 
>  1. Schreiben Sie die Funktion neuerKopf
>  2. Fügen Sie die Funktion auch zu den regelmäßig ausgeführten Funktionen hinzu
>  3. Testen Sie, ob Ihre Schlange läuft
>  4. Probieren Sie alle möglichen Richtungen zu gehen (nach oben, nach unten, nach rechts, nach links), indem Sie bei `s.dir` andere Zahlen einspeichern.

[Zurück: 3.1 - Computerspiele](Computerspiel.md) |  [Inhalt](README.md) |  [Kapitel](snakespiel.md) |  [Weiter: 3.3 - Steuerung](Steuerung.md) | 
