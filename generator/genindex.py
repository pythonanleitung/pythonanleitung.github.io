#! /bin/env python3
import os

chapters_list = [
    ("Erste Schritte", "", "ErsteSchritte.md"),
    ("Speichern in eine Datei", "", "Speichern.md"),
    ("Variablen", "Das Kurzzeitgedächtnis", "Variablen.md"),
    ("Fehlermeldungen", "können helfen", "Fehler.md"),
    ("Datentypen", "Buchstaben und Zahlen", "Datentypen.md"),
    ("Eingaben", "Interaktive Programme", "Eingaben.md"),
    ("Fallunterscheidung", "Wenn -> Dann", "BedingtesAusfuehren.md"),
    ("Schildkröten", "", "Turtle.md"),
    ("Zufall", "", "Zufall.md"),
    ("Wiederholungen", "", "Wiederholungen.md"),
    ("Mehrmaliges tun", "", "Turtle-Wiederholungen.md"),
    ("Sterne", "", "Sterne.md"),
    ("Kreise", "", "Kreise.md"),
    ("Turtle Zusammenfassung", "", "Turtlebefehle.md"),
    ("Turtle Beispielaufgaben", "", "Turtlebeispielaufgaben.md"),
    ("Listen", "", "Listen.md"),
    ("For Schleifen", "", "Forschleifen.md"),
    ("Kommentare", "", "Kommentare.md"),
    ("Epochenheft", "", "AufgabenEpochenheft.md"),
    ("Computerspiele", "", "Computerspiel.md"),
    ("Animation", "", "Animation.md"),
    ("Cheat-Sheet", "", "Cheat-Sheet.md")
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
    strings['back'] = "[Zurück zu Kapitel {index}: {name}]({filename}) | ".format(index=chapter_index, name=prevname, filename=prevfilename)
    strings['inhalt'] = "[Inhaltsverzeichnis]({filename}) | ".format(filename="README.md")
    strings['next'] = "[Weiter zu Kapitel {index}: {name}]({filename}) | ".format(index=chapter_index+2, name=nextname, filename=nextfilename)

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
strings['inhalt'] = "[Inhaltsverzeichnis]({filename}) | ".format(filename="README.md")
strings['next'] = "[Weiter zu Kapitel {index}: {name}]({filename}) | ".format(index=1, name = chapters_list[0][0], filename=chapters_list[0][1])
inhaltsstrings = [" 1. [{0}{1}]({2})".format( x[0], " - " + x[1] if x[1] else "" , x[2]) for x in chapters_list]
strings['inhaltsverzeichnis'] = '\n'.join(inhaltsstrings)

with open(src("README.md"), 'r') as s:
    with open(dest("README.md"), 'w') as d:
            text = s.read()
            text = text.format(**strings)
            d.write(text)
        
