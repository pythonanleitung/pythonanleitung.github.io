#! /usr/bin/env python3
import os

chapters_list = [
    ["Grafiken mit Turtle", "", 'turtlekapitel.md',
        [("Erste Schritte", "", "ErsteSchritte.md"),
        ("Speichern in eine Datei", "", "Speichern.md"),
        ("Schildkröten", "", "Turtle.md"),
        ("Eingaben in Turtle", "Turtle hat eine Möglichkeite für Eingaben", "TurtleInput.md"),
        ("Wiederholungen mit While", "", "Wiederholungenwhile.md"),
        ("Mandala mit while", "", "Turtlewiederholungenwhile.md"),
        ("Variablen", "Das Kurzzeitgedächtnis", "Variablen.md"),
        ("Fallunterscheidung", "wenn → dann (→ sonst)", "BedingtesAusfuehren.md"),
        ("For Schleifen", "", "Forschleifen.md"),
        ("Listen", "", "Listen.md"),
        ("For mit Listen ", "", "Formitlisten.md"),
        ("Zufall", "", "Zufall.md"),
        ("Funktionen", "so etwas wie Schablonen", "Funktionen.md"),
        ("Kreise", "", "Kreise.md"),
        ("Kommentare", "", "Kommentare.md"),
        ("Turtle Beispielaufgaben", "", "Turtlebeispielaufgaben.md"),
        ("Turtle Zusammenfassung", "", "Turtlebefehle.md"),
        ]
    ],
    ["Galgenmännchen mit turtle", "", "hangman.md",
        [("Eine Funktion für jeden Galgenschritt", "", "hangschritte.md"),
        ("Immer wieder abfragen", "", "hangabfrage.md"),
        ("Geheimwortliste", "", "hanggeheimliste.md"),
        ("Einbinden der Wortliste", "", "hangeinbinden.md"),
        ("Abspeichern der Tipps", "", "hangtipsspeich.md"),
        ("Anzeigen der Geratenen Buchstaben", "", "hanggeratenes.md"),
        ("Feinschliff", "", "hangfeinschl.md"),
        ]
    ],
    ["Ein Snakespiel", "", "snakespiel.md",
        [
        ("Computerspiele", "", "Computerspiel.md"),
        ("Animation", "", "Animation.md"),
        ("Steuerung", "", "Steuerung.md")]
    ],
    ["Anhang", "", "anhang.md",
        [("Cheat-Sheet", "", "Cheat-Sheet.md"),
        ("Bedingungen", "was alles im `if` stehen kann", "Bedingungen.md"),
        ("Fehlermeldungen", "", "Fehler.md"),]
    ]
]

projpath = os.path.dirname(os.path.dirname(__file__))
srcpath = "src"
destpath = "docs"


def src(filename):
    return os.path.join(projpath, srcpath, filename)
def dest(filename):
    return os.path.join(projpath, destpath, filename)

def render_strings(index, subindex, prev, cur, next, chapter):
    strings = dict()
    if prev:
        strings['back'] = "[Zurück: {index}.{subindex} - {name}]({filename}) | ".format(index=index+1, subindex = subindex, name=prev[0], filename=prev[2])
    else:
        strings['back'] = ""

    strings['inhalt'] = "[Inhalt]({filename}) | ".format(filename="README.md")
    strings['chapter'] = "[Kapitel]({filename}) | ".format(filename=chapter[2])
    if next:
        strings['next'] = "[Weiter: {index}.{subindex} - {name}]({filename}) | ".format(index=index+1, subindex=subindex +2, name=next[0], filename=next[2])
    else:
        strings['next'] = ""
    return strings

for chapter_index in range(len(chapters_list)):
    chapter = chapters_list[chapter_index]
    chap_lines = []

    for numl, line in enumerate(chapter[3]):
        chap_lines += ["\n   * {0}.{1} – [{2}{3}]({4})".format(chapter_index+1, numl+1, line[0], ": " + line[1] if line[1] else "" , line[2])]
    chap_cont = ''.join(chap_lines)

    strings = render_strings(chapter_index, -1, None, chapter, chapter[3][0], chapter)
    strings['inhaltsverzeichnis'] = chap_cont
    filename = chapter[2]
    with open(src(filename), 'r') as s:
        with open(dest(filename), 'w') as d:
            text = s.read()
            text = text.format(**strings)
            d.write(text)

    for headline_index in range(len(chapter[3])):

        if headline_index > 0:
            prev = chapter[3][headline_index-1]
        else:
            prev = None
        if headline_index < len(chapter[3])-1:
            next = chapter[3][headline_index+1]
        else:
            next = None

        strings = render_strings(chapter_index, headline_index, prev, chapter[3][headline_index], next, chapter )
        filename = chapter[3][headline_index][2]
        with open(src(filename), 'r') as s:
            with open(dest(filename), 'w') as d:
                text = s.read()
                text = text.format(**strings)
                d.write(text)

index_lines = []
for numc, chapter in enumerate(chapters_list):
    chap_lines = ["\n\n### {0}. [{1}{2}]({3})\n".format( numc+1, chapter[0], ": " + chapter[1] if chapter[1] else "" , chapter[2])]
    for numl, line in enumerate(chapter[3]):
        chap_lines += ["\n   * {0}.{1} – [{2}{3}]({4})".format(numc+1, numl+1, line[0], ": " + line[1] if line[1] else "" , line[2])]
    index_lines.append(chap_lines)

strings = dict()
#strings['back'] = "[Zurück zu Kapitel {index}: {name}]({filename}) | ".format(index=chapter_index, name=prev[0], filename=prev[1])
strings['inhalt'] = "[Home]({filename}) | ".format(filename="README.md")
strings['next'] = "[Weiter: Kapitel {index} - {name}]({filename}) | ".format(index=1, name = chapters_list[0][0], filename=chapters_list[0][2])
inhaltsstrings = [" 1. [{0}{1}]({2})".format( x[0], " - " + x[1] if x[1] else "" , x[2]) for x in chapters_list]
strings['inhaltsverzeichnis'] = ''.join([''.join(i) for i in index_lines])

with open(src("README.md"), 'r') as s:
    with open(dest("README.md"), 'w') as d:
            text = s.read()
            text = text.format(**strings)
            d.write(text)
