# Cheat-Sheet



### [Zahlen und Wörter](4-datentypen.md)

```python
1, 2, 25, 10000000, 0.1, "hallo", "hallo welt!", """merhzeiliger text
geht so"""
```

### [Listen](../3-turtle/090-listen.md)

```python
[], [1,2,3,4], range(5), range(5,15,2)
```

### [Rechnen](../2-programmieren/2-ersteschritte.md)

```python
/ # Division
* # Multiplikation
+ # Addition
- # Subtraktion

5 + 7
4 * 4
```

### [Variablen](../3-turtle/060-variablen.md)
Variablen können verwendet werden um Zwischenergebnisse zu Speichern, oder einen Wert mehrmals zu verwenden.

```python
a = 50
b = 70
herbert = a + b
```

### [Fallunterscheidung](../040-ratespiel/04.3-bedingtesausfuehren.md)
Mit if können Teile des Programms nur unter bestimmten Bedingungen ausgeführt werden.

```python
if herbert < 121:
    herbert = herbert + 1
```

### [Ein und Ausgabe](../2-programmieren/2-ersteschritte.md)
```python
print("hallo")
input()
```

### Wiederholung [while](../040-ratespiel/04.4-wiederholungenwhile.md), [for](../3-turtle/040-forschleifen.md), [for](../3-turtle/045-forschleifen2.md)
```python
while 1 < 2:
    print("go")

for i in range(50):
    print("stop")

for i in "hello":
    print(i)

for i in [25, 25, 1.9, 'hi', 'du']:
    print(i)
```

### [Funktionen](../3-turtle/120-funktionen.md)
```python
def doFun(name):
   print("hello there", name)

doFun(name="Gollom")
doFun(name="Dobby")
```
