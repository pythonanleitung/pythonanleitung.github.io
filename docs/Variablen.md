# Variablen

[Zurück: Kapitel 2 - Speichern in eine Datei](Speichern.md) |  [Home](README.md) |  [Weiter: Kapitel 4 - Fehlermeldungen](Fehler.md) | 

In diesem Kapitel geht es darum, wie sich das Computerprogramm etwas merkt, und wie man dieses gemerkte verwenden kann.


Bis jetzt Werte immer sofort verwendet. Wurde eine `5` geschrieben, wurde sie zum Beispiel in einer Rechnung verwendet. Wenn aber der Wert an zwei Stellen im Programm verwendet werden soll, also zum Beispiel um  die Mitternachtsformel einmal mit plus und einmal mit minus zu rechnen, so muss der Wert zwischengespeichert werden. Hierzu werden Variablen verwendet. Um eine Variable zu erstellen, schreibt man einen beliebigen Namen der Variablen (ohne Leerzeichen), nach einem `=`  folgt der Wert den die Variable haben soll.

Einige Beispiele:
```python
x = 5
y = 'hallo'
z = 5 + 5
```

In der ersten Zeile wird die Zahl `5` in die Variable `x` eingespeichert. Die zweite Zeile speichert `'hallo'` in `y`. Die Dritte das Ergebnis der Berechnung `5 + 5` in `z`.

Die Zuweisung einer Variable hat keinerlei Ausgabe - es wird also nirgends sichtbar, dass diese Variable jetzt gesetzt ist.

Diese Variablen können nun verwendet werden hat man zum Beispiel mit `x = 5` der Variablen `x` den Wert `5` gegeben, so kann man nun statt der dritten Zeile auch `z = x + x` schreiben und wird wieder in `z` denselben Wert (`10`) gespeichert haben. Möchte man den Wert einer Variablen ausgeben, so kann man dies mit `print` tun. Um den Wert von `z` zu erfahren also `print(z)`.

Die Variablen sind so etwas wie das Kurzzeitgedächtnis des Computers... Er kann sich alles darin merken, aber nach Ende des Programms sind alle Variablen weg. Soll beim Start die Variable wieder vorhanden sein, dann muss sie wieder neu gesetzt werden.

In `thonny` können alle bestehenden Variablen angesehen werden. Hierzu Öffnet man den "`Variables View`", indem man auf `View->Variables` klickt. Auf der rechten Seite des Fensters erscheint dann ein Teil, welcher immer Variablenname und den darin gespeicherten Wert angibt.

![VariablesView](VariablesView.png)

> ### Übungen
>
>  1. Erstellen Sie eine Python-Datei `Variablen.py` welche die Variablen `x, y, z` die Werte `34, 24, 'hallo'` zuweist.
>  1. Führen Sie das Programm aus. Es erscheint keine Ausgabe (warum? Siehe [hier](02Speichern.md/#automatische-ausgabe))
>  1. Geben Sie alle Variablen mit `print` aus. Achtung Geben Sie die Variablen aus und nicht nur die selbe Zahl.
>  1. Testen Sie, indem Sie das Programm nochmals starten, ihre neue Ausgabe.
>  2. Berechnen Sie in die Variable `summe` die Summe von `x` und `y`. Verwenden Sie auch hier die Variablen statt ihren Zahlenwert.
>  3. Geben Sie die Summe mit `print` aus.
>  4. Starten Sie das Programm erneut lösen Sie alle [Fehlermeldungen](Fehler.md). Im nächsten Absatz werden einige Meldungen erklärt.
>  5. Betrachten Sie die erstellten Variablen im "`Variables View`"

[Zurück: Kapitel 2 - Speichern in eine Datei](Speichern.md) |  [Home](README.md) |  [Weiter: Kapitel 4 - Fehlermeldungen](Fehler.md) | 
