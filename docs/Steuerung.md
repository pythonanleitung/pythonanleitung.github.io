# Steuerung der Schlange per Tastatur

[Zurück: Kapitel 17 - Animation](Animation.md) |  [Home](README.md) |  [Weiter: Kapitel 19 - Cheat-Sheet](Cheat-Sheet.md) | 

Nachdem nun die Schlange läuft, ist es jedoch immernoch nicht möglich diese per Tastatur zu steuern.

Das Programm muss noch auf verschiedene Tasten "hören". Die entsprechende Funktion heißt darum oft `keylistener` oder auf deutsch `reagiereauftasten`. Die Funktion reagiere auf Tasten bekommt einen parameter. Eine erste (Test-)Version dieser Funktion ist hier:

```python
def reagiereauftasten(taste):
    print("Es wurde folgende Taste gedrückt: ", taste)
```

Diese Funktion wird nun noch dem Spiel übergeben, sodass sie bei jedem Tastendruck ausgeführt wird. Schreiben Sie `s.addKeylistener(reagiereauftasten)` unten bei den `s.addStep` Zeilen.

Wenn Sie jetzt das Spiel gestartet haben und ein paar Tasten drücken werden die gedrückten Tasten auf der Konsole ausgegeben. Tasten auf die reagiert wird sind: die Pfeiltasten, WASD, Escape. Bedenken Sie, dass die Tasten nur beim Spiel ankommen, wenn dieses im Vordergrund ist.

In der `reagiereauftasten`-Funktion kann nun mit `if` usw. auf die Variable `taste` reagiert werden. Um zum Beispiel das Spiel mit der Escape(esc) Taste zu beenden kann die Funktion folgender maßen geändert werden.

```python
def reagiereauftasten(taste):
    print("Es wurde folgende Taste gedrückt: ", taste)
    
    if taste == "Esc":
        s.exit()
```

> ### Übung
> 
>  1. Erweitern Sie die `reagiereauftasten`-Funktion, sodass Sie, wenn `"Left"` gedrückt wurde die `s.dir` Variable anpasst. (Wenn Sie wollen können Sie mehr L33t H4x0r sein, indem Sie die WASD Tasten zur Steuerung verwenden).
>  2. Fügen Sie jetzt alle anderen Richtungen hinzu.
>  3. Testen Sie ihr Spiel ausgiebig. Welche Probleme haben Sie noch?

[Zurück: Kapitel 17 - Animation](Animation.md) |  [Home](README.md) |  [Weiter: Kapitel 19 - Cheat-Sheet](Cheat-Sheet.md) | 
