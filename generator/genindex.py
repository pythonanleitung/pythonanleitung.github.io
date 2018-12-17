#! /usr/bin/env python3
import os

chapters_list = [
    ("Erste Schritte", "", "ErsteSchritte.md"),
    ("Speichern in eine Datei", "", "Speichern.md"),
    ("Variablen", "das Kurzzeitgedächtnis", "Variablen.md"),
    ("Fehlermeldungen", "können helfen", "Fehler.md"),
    ("Datentypen", "Buchstaben und Zahlen", "Datentypen.md"),
    ("Eingaben", "interaktive Programme", "Eingaben.md"),
    ("Schildkröten", "", "Turtle.md"),
    ("Eingaben in Turtle", "Turtle hat eigene Möglichkeiten für Eingaben", "TurtleInput.md"),
    ("Fallunterscheidung", "wenn → dann (→ sonst)", "BedingtesAusfuehren.md"),
    ("Wiederholungen mit While", "", "Wiederholungenwhile.md"),
    ("Mandala mit while", "", "Turtlewiederholungenwhile.md"),
    ("For Schleifen", "", "Forschleifen.md"),
    ("Listen", "", "Listen.md"),
    ("For mit Listen ", "", "Formitlisten.md"),
    ("Zufall", "", "Zufall.md"),
    ("Funktionen", "so etwas wie Schablonen", "Funktionen.md"),
    ("Kreise", "", "Kreise.md"),
    ("Kommentare", "", "Kommentare.md"),
    ("Turtle Beispielaufgaben", "", "Turtlebeispielaufgaben.md"),
    ("Turtle Zusammenfassung", "", "Turtlebefehle.md"),
    ("Computerspiele", "", "Computerspiel.md"),
    ("Animation", "", "Animation.md"),
    ("Steuerung", "", "Steuerung.md"),
    ("Cheat-Sheet", "", "Cheat-Sheet.md")
]

other = [
("Bedingungen", "was alles im `if` stehen kann", "Bedingungen.md"),
]

projpath = os.path.dirname(os.path.dirname(__file__))
srcpath = "src"
destpath = "docs"


def src(filename):
    return os.path.join(projpath, srcpath, filename)
def dest(filename):
    return os.path.join(projpath, destpath, filename)

for chapter_index in range(len(chapters_list)):
    chapter = chapters_list[chapter_index]
    if chapter_index > 0:
        prev = chapters_list[chapter_index-1]
    else:
        prev = ("","","")
    if chapter_index < len(chapters_list)-1:
        next = chapters_list[chapter_index+1]
    else:
        next = ("","","")

    name, description, filename = chapter
    nextname, nextdescription, nextfilename = next
    prevname, prevdescription, prevfilename = prev

    strings = dict()
    strings['back'] = "[Zurück: Kapitel {index} - {name}]({filename}) | ".format(index=chapter_index, name=prevname, filename=prevfilename)
    strings['inhalt'] = "[Home]({filename}) | ".format(filename="README.md")
    strings['next'] = "[Weiter: Kapitel {index} - {name}]({filename}) | ".format(index=chapter_index+2, name=nextname, filename=nextfilename)

    if chapter_index == 0:
        strings['back'] = ""
    if chapter_index >=   len(chapters_list)-1:
        strings['next'] = ""

    with open(src(filename), 'r') as s:
        with open(dest(filename), 'w') as d:
            text = s.read()
            text = text.format(**strings)
            d.write(text)

strings = dict()
#strings['back'] = "[Zurück zu Kapitel {index}: {name}]({filename}) | ".format(index=chapter_index, name=prev[0], filename=prev[1])
strings['inhalt'] = "[Home]({filename}) | ".format(filename="README.md")
strings['next'] = "[Weiter: Kapitel {index} - {name}]({filename}) | ".format(index=1, name = chapters_list[0][0], filename=chapters_list[0][2])
inhaltsstrings = [" 1. [{0}{1}]({2})".format( x[0], " - " + x[1] if x[1] else "" , x[2]) for x in chapters_list]
strings['inhaltsverzeichnis'] = '\n'.join(inhaltsstrings)

with open(src("README.md"), 'r') as s:
    with open(dest("README.md"), 'w') as d:
            text = s.read()
            text = text.format(**strings)
            d.write(text)
