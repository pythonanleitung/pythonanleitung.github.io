# Speichern in eine Datei

[Zurück zum ersten Abschnitt](01ErsteSchritte.md) | [Zurück zur ersten Seite](/)

Da das ständige erneut Tippen auf Dauer nicht besonders effizient ist, kann man den Programmcode von Python in eine Datei abspeichern und dann diese Datei ausführen.

Hierzu wird zunächst die Textbearbeitung geöffnet (Windowstaste drücken, `textbearbeitung` eingeben, und mit `Enter` bestätigen - Vorsicht nicht Libreoffice öffnen). Dann wird der Python Code eingegeben und die Datei unter `hallo.py` im "Persönlichen Ordner" abgespeichert. Der Inhalt von `hallo.py` kann dann zum Beispiel so aussehen:

Dateiname: `hallo.py`
```python
print("hallo")
```

Noch einmal überprüfen, ob man gespeichert hat, dann kann man das Programm im
Terminal ausführen.

> ### Notiz
> Wenn Python noch von vorherigen Experimenten läuft, kann man keine Programme
> ausführen, sondern nur Python-Code eingeben.
>
> Zeigt der Computer in der untersten Zeile noch `>>>` an, ist Python noch
> gestartet und muss beendet werden. Am Ende der vom Computer
> geschriebenen Zeile sollte ein `$` stehen.
> Falls alles nicht klappt einfach das Terminal schließen und neu starten.

Der Befehl lautet: `python3 hallo.py`.

Dieses kurze Programm tut nichts anderes, als `hallo` auszugeben.

```bash
user@computer ~$ python3 hallo.py 
hallo
```

> ### Übung
> Erstellen Sie das oben genannte Programm und führe es aus. Überprüfen Sie, dass es keinen Fehler macht.

# Automatische Ausgabe

Wird ein Programm aus einer Datei heraus gestartet, so ist die automatische Ausgabe deaktiviert. Das heißt eine Datei, mit folgendem Inhalt, wird keine Ausgabe haben:

```python
5 + 7
```

Der Computer rechnet zwar fleißig was 5+7 ist, aber verwendet dann das Ergebnis nicht weiter. Um das Ergebnis angezeigt zu bekommen, muss man explizit sagen, dass man dies sehen möchte:

```python
print(5 + 7)
```

Da das Hin- und Her-wechseln zwischen den Programmen aber immer noch relativ kompliziert ist, gibt es ein Programm, welches die Funktion des Terminals und die Funktion des Texteditors in einem vereint.

# Thonny

Thonny ist speziell für Schüler und Studenten geschrieben. Es kann gestartet werden mit Windowstaste → Eingabe `thonny` → `Enter`.

Nach dem Start sieht Thonny so aus:

![Screenshot Thonny](/img/ThonnyLeer.png)

Direkt unter dem Menü befinden sich die wichtigsten Funktionen als Buttons.

![Screenshot Thonny](/img/ThonnyButtons.png)

 1. Eine neue Datei anlegen
 2. Eine Datei öffnen
 3. Die Datei speichern
 4. "Play-Button" das Programm ausführen
 5. Das Programm Schritt für Schritt ausführen
 6. Beim Schrittweisen ausführen einen großen Schritt machen
 7. Beim Schrittweisen ausführen einen kleinen Schritt machen
 8. So ähnlich wie 6.
 9. "Stopp-Button" das Programm beenden, wenn es Probleme gibt und das Ausführen
    nicht mehr funktioniert so hilft es oft das alte Programm zu beenden und dann neu starten
 
Wurde ein Programm geöffnet und gestartet, so sieht Thonny so aus:

![Screenshot Thonny](/img/BildschirmfotoThonny.png)

Der große Teil des Fensters wird ausgefüllt von dem Inhalt der geöffneten Datei. Alles was hier steht, ist das was zuvor in dem Textbearbeitungsfenster gemacht wurde.

Darunter ist ein kleinerer Teil, welcher das derzeitige Programm im interaktiven Modus ausführt. Dies ist also so etwas wie ein Python, im Terminal gestartet. Das heißt hier erscheinen eventuelle Ausgaben, wenn man auf "play" drückt.

> ### Notiz
> Alle weiteren Programme und Beispiele werden in Thonny ausgeführt. Beginnen die Beispiele mit `>>>` so sind sie für das untere interaktive  "Ausprobier"-Fenster gedacht. Beginnen sie direkt mit Python-Befehlen, so sind sie für das obere Fenster gedacht.

Immer wenn etwas im oberen Fenster verändert wurde, so muss wieder der "Play-Button" gedrückt werden, dass das neu veränderte Programm gestartet wird. Vorsicht Eingaben, die in dem unteren Teil gemacht wurden, sind danach "verloren".

> ### Übung
> 1. Schreiben Sie in den oberen Teil von Thonny einen Python Befehl, der `"Hallo"` ausgibt.
> 1. Speichern Sie diese Datei mit dem Namen `HalloWelt.py` ab.
> 1. Führen Sie nun die datei mit dem "play"-Knopf aus.

[Weiter zum nächsten Abschnitt](03Variablen.md) |