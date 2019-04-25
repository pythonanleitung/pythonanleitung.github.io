# Speichern in eine Datei

[Zurück: 1.1 - Erste Schritte](ErsteSchritte.md) |  [Inhalt](README.md) |  [Kapitel](turtlekapitel.md) |  [Weiter: 1.3 - Schildkröten](Turtle.md) | 

> Ziel dieses Kapitels ist es die Arbeit die wir machen abzuspeichern, sodass man es später wieder verwenden kann, und vielleicht auch jemand das Programm einfach verwenden kann ohne zu programmieren.

Da das ständige erneut Tippen auf Dauer nicht besonders effizient ist, kann man den Programmcode von Python in eine Datei abspeichern und dann diese Datei ausführen.

Um dies zu tun muss der obere Teil von `thonny` verwendet werden.

  > ### Übung Speichern in eine Datei
  > 1. Öffnen Sie eine neue Datei durch einen Klick auf den neuen Datei-Button.
  > 1. Geben Sie den Befehl `print("hallo")` in die neu geöffnete Datei, also den oberen Teil des Fensters, ein.
  > 1. Speichern Sie diese Datei mit dem Namen `Hallo.py` ab, indem Sie auf das Diskettensymbol klicken, oder indem Sie `Datei->Speichern` klicken.
  > 1. Führen Sie nun die Datei mit dem grünen "Play-Button" aus. Alternativ können Sie auch die mit F5 beschriftete Taste der Tastatur drücken.
  > 1. Finden Sie, wo der Text `"hallo"` ausgegeben wurde.

Dieses kurze Programm tut nichts anderes, als `hallo` auszugeben.

## Die Buttons erklärt

![Screenshot Thonny](./img/ThonnyButtons.png)

Von links nach rechts haben die Buttons folgende Funtkionen, wobei die ersten vier und der letzte die wichtigsten sind:

 1. Eine neue Datei anlegen
 2. Eine Datei öffnen
 3. Die Datei speichern
 4. "Play-Button" das Programm ausführen
 5. unwichtig: Das Programm Schritt für Schritt ausführen
 6. unwichtig: Beim Schrittweisen ausführen einen großen Schritt machen
 7. unwichtig: Beim Schrittweisen ausführen einen kleinen Schritt machen
 8. unwichtig: So ähnlich wie 6.
 9. "Stopp-Button" das Programm beenden, wenn es Probleme gibt und das Ausführen
    nicht mehr funktioniert so hilft es oft das alte Programm zu beenden und dann neu starten

# Automatische Ausgabe

Wird ein Programm aus einer Datei heraus gestartet, so ist die automatische Ausgabe deaktiviert, da sonst viel zu viele Ausgaben angezeigt würden. Das heißt eine Datei, mit folgendem Inhalt, wird keine Ausgabe haben, obwohl der Computer die beiden Zahlen zusammen addiert:

```python
5 + 7
```

Der Computer rechnet zwar fleißig was 5+7 ist, aber verwendet dann das Ergebnis nicht weiter. Um das Ergebnis angezeigt zu bekommen, muss man explizit sagen, dass man dies sehen möchte:

```python
print(5 + 7)
```


> ### Notiz
> Alle weiteren Programme und Beispiele werden in Thonny ausgeführt. Beginnen die Beispiele mit `>>>` so sind sie für das untere interaktive  **"Ausprobier"-Fenster** gedacht. Beginnen sie direkt mit Python-Befehlen, so sind sie für das obere Fenster gedacht.

Immer wenn etwas im oberen Fenster verändert wurde, so muss wieder der "Play-Button" gedrückt werden, dass das neu veränderte Programm gestartet wird. Vorsicht Eingaben, die in dem unteren Teil gemacht wurden, sind danach "verloren".


> ### Übung Rechnung mit Ausgabe
> 1. Schreiben Sie in den oberen Teil von Thonny einen Python Befehl, der `555` mit `364` multipliziert, und das Ergebnis ausgibt.
> 1. Speichern Sie diese Datei mit dem Namen `rechnung.py` ab.
> 1. Führen Sie nun die Datei mit dem "Play-Button" aus.

[Zurück: 1.1 - Erste Schritte](ErsteSchritte.md) |  [Inhalt](README.md) |  [Kapitel](turtlekapitel.md) |  [Weiter: 1.3 - Schildkröten](Turtle.md) | 
