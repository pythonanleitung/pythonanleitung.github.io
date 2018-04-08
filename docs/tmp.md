Es wurde hier `"hallo"` verglichen mit der Eingabe (`hallo`) und es kommt `True` also wahr heraus. Wird in der Zeile, in der der Computer nach einem Grußwort fragt nicht `hallo` eingegeben, sondern etwas anderes kommt das Ergebnis `False`, also falsch heraus. Ein Beispiel hierzu:

```python
>>> "Hallo" == input("Sag fein Hallo: ")
Sag fein Hallo: never
False
```

Das so erzeugte `True` oder `False` kann in einem `if` verwendet werden:

```python
>>> if "Hallo" == input("Sag fein Hallo: "):
...     print("Hallo")
... else:
...     print("Nicht Hallo!")
... 
Sag fein Hallo: Hallo
Hallo
>>> if "Hallo" == input("Sag fein Hallo: "):
...     print("Hallo")
... else:
...     print("Nicht Hallo!")
... 
Sag fein Hallo: never
Nicht Hallo!
```

Die beiden Beispiele verdeutlichen, einmal die Eingabe `hallo`, welche `True` ergibt, und einmal die Eingabe `nö`, welche `False` ergibt. Je nach Ergebnis wird `hallo` oder `nicht hallo` ausgegeben.