# Steuerung der Schlange per Tastatur

[Zurück: Kapitel 20 - Animation](Animation.md) |  [Home](README.md) |  [Weiter: Kapitel 22 - Cheat-Sheet](Cheat-Sheet.md) | 

Nachdem nun die Schlange läuft, ist es jedoch immernoch nicht möglich diese per Tastatur zu steuern.

Das Programm muss noch auf verschiedene Tasten "hören". Die entsprechende Funktion heißt darum oft `keylistener` oder auf deutsch `reagiereauftasten`. Die Funktion reagiere auf Tasten bekommt einen parameter. Eine erste (Test-)Version dieser Funktion ist hier:

```python
def reagiereauftasten(taste):
    print("Es wurde folgende Taste gedrückt: ", taste)
```

Diese Funktion wird nun noch dem Spiel übergeben, sodass sie bei jedem Tastendruck ausgeführt wird. Schreiben Sie `s.addKeylistener(reagiereauftasten)` unten bei den `s.addStep` Zeilen.

Wenn Sie jetzt das Spiel gestartet haben und ein paar Tasten drücken werden die gedrückten Tasten auf der Konsole ausgegeben. Achten Sie darauf, dass die Tasten nur beim Spiel ankommen, wenn dieses im Vordergrund ist.

In der `reagiereauftasten`-Funktion kann nun mit `if` usw. auf die Variable `taste` reagiert werden. Um zum Beispiel das Spiel mit der Escape(Esc) Taste zu beenden kann die Funktion folgender maßen geändert werden.

```python
def reagiereauftasten(taste):
    print("Es wurde folgende Taste gedrückt: ", taste)
    
    if taste == "Esc":
        s.exit()
```

[Zurück: Kapitel 20 - Animation](Animation.md) |  [Home](README.md) |  [Weiter: Kapitel 22 - Cheat-Sheet](Cheat-Sheet.md) | 
