# Der input-Befehl des turtle-Moduls

[Zurück: Kapitel 3 - Schildkröten](Turtle.md) |  [Home](README.md) |  [Weiter: Kapitel 5 - Fallunterscheidung](BedingtesAusfuehren.md) | 

Möchte man eine Form in variabler Größe zeichnen, könnte man einfach den `input` Befehl aus dem Kapitel [Eingaben](Eingaben.md) verwenden. Dieser ist jedoch in der "Shell" - man müsste also zunächst unten im Fenster von Thonny die Fragen beantworten, danach wird dann die Form gezeichnet. Eine etwas schönere Variante ist es, wenn das Turtlefenster selbst nach den Eingaben fragt.

Turtle stellt zwei Befehle zur Verfügung:

```python
zahl = turtle.numinput(title="was dann im titel des Fensters steht", prompt="Welche Frage vor dem Eingabefeld steht")
text = turtle.textinput(title="was dann im titel des Fensters steht", prompt="Welche Frage vor dem Eingabefeld steht")
```

Zu beachten ist, dass tatsächlich `turtle.` vor `*input` stehen muss. Was in `title=` übergeben wird landet im Fenstertitel, was in `promt=` übergeben wird ist quasi die Frage.

> ### Übung
>
> Gespeichert in der neuen Datei `kleingroß.py`
>
> 1. Schreiben Sie ein Turtle-Programm, welches zuerst nach einer Zahl fragt, und dann ein Quadrat in entsprechender Größe, also Seitenlänge zeichnet.
> 2. Erweitern Sie das Programm, dass es nach dem Zeichnen des Quadrats noch eine Größe für ein gleichseitiges Dreieck fragt, und dieses dann zeichnet.

[Zurück: Kapitel 3 - Schildkröten](Turtle.md) |  [Home](README.md) |  [Weiter: Kapitel 5 - Fallunterscheidung](BedingtesAusfuehren.md) | 
