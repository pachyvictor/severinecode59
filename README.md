# severinecode59
Code du jeu hackathon

```python
Map_de_base = '------------------/|................|/|................|/|................|/|................|/|................|/|................|/|................|/|................|/|................|/------------------/'

def str_to_tableau(chaine):
    tableau = [[]]
    j = 0
    for k in chaine:
        if k == '/':
            tableau.append([])
            j += 1
        else:
            tableau[j].append(k)
    return tableau

tableau = str_to_tableau(Map_de_base)
```

```python

```
