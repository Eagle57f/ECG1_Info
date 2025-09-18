# TP 1 - Introduction à l'algorithmique, présentation de python et exemples

Les parties en _italique_ sont des approfondissements qui pourraient être utiles.

## Quelques symboles

| Symbole | Signification |
|:-:|:-|
| +  | Addition `#!python 1+2==3` |
| -  | Soustraction `#!python 1-2==-1` |
| *  | Multiplication `#!python 2*3==6` |
| ** | Puissance `#!python 2**3==8` |
| /  | Division `#!python 6/2==3` |
| // | Quotient division euclidienne `#!python 7//2==3` |
| %  | Reste division euclidienne `#!python 7%2==1` |

Les chiffres à virgule s'écrivent avec un point en python. Ex: `#!python 1.005`

## Variables et affichage

Un algorithme python s'exécute dans l'ordre(1ère ligne->dernière ligne), il faut donc initialiser les variables avant de les utiliser.


```python
a="t"
b=2
c=3
print(a,c,b)
```
<div class="result" markdown>
``` python title="Renvoie"
t 3 2
```
</div>

Python est sensible à la casse, donc `#!python Variable != variable`.

## Le point-virgule

En python, le point-virgule `#!python ;` n'est pas obligatoire à la fin d'une ligne. Il est possible de l'utiliser pour séparer plusieurs instructions sur une même ligne, mais ce n'est **vraiment** pas recommandé ([PEP-0008](https://peps.python.org/pep-0008/#other-recommendations): "_Compound statements (multiple statements on the same line) are generally discouraged_").

```python
a=1; b=2; print(a+b)
```
<div class="result" markdown>
``` python title="Renvoie"
3
```
</div>

Dans certains cas, l'utilisation du point-virgule peut même donner des erreurs, comme pour les instructions `#!python if`, `#!python for`, `#!python while` et `#!python def`.

```py
print('Hi') ; for i in range (4): print ('Hello')
```
<div class="result" markdown>
``` python title="Renvoie"
SyntaxError: invalid syntax
```
</div>

Il est donc préférable de ne pas l'utiliser.

## Premières fonctions

|abs(x)|int(x)|max(a,b,c,...)|min(a,b,c,...)|round(x, n)|
|:-:|:-:|:-:|:-:|:-:|
|Valeur absolue `#!python abs(-3)==3`|Supprime la partie fractionnaire `#!python int(-3.7)==-3`|Maximum `#!python max(2.5,-3,6)==6`|Minimum `#!python min(2.5,-3,6)==-3`|Arrondi à 10^(-n) près `#!python round(3.577,1)==3.6`|

## Importer une bibliothèque

Une bibliothèque est un ensemble de fonctions et variables prédéfinies.
Il faut toujours importer la bibliothèque avant d'utiliser une fonction ou variable de cette bibliothèque. Le plus souvent, il est préférable d'importer les bibliothèques au début du fichier, afin quelles soient disponibles dans tout le fichier.

Pour importer une bibliothèque, par exemple la bibliothèque math:

```python
import math
print(math.pi, math.e)
```
<div class="result" markdown>
``` python title="Renvoie"
3.141592653589793 7.38905609893065
```
</div>

Pour importer une fonction ou variable d'une bibliothèque:

```python
from math import pi
print(pi)
```
<div class="result" markdown>
``` python title="Renvoie"
3.141592653589793
```
</div>

Attention, en important de cette façon, on n'importe que `#!python pi`, pas toute la bibliothèque `#!python math`. Donc on ne peut pas écrire `#!python math.pi` par exemple:

```python
from math import pi
print(pi)
print(math.pi)
```
<div class="result" markdown>
``` python title="Renvoie"
3.141592653589793
    print(math.pi)
        ^^^^
NameError: name 'math' is not defined # (1)!
```

1. Erreur car on a importé seulement `#!python pi`, pas toute la bibliothèque `#!python math`.

</div>



Pour importer toutes les fonctions et variables d'une bibliothèque:

```python
from math import *
print(pi, exp(2))
```
<div class="result" markdown>
``` python title="Renvoie"
3.141592653589793 7.38905609893065
```
</div>

Il est possible de renommer une bibliothèque _(on appelle ce nouveau nom un alias)_, on l'utilisera surtout pour les bibliothèques `#!python numpy` et `#!python matplotlib.pyplot`:
```python
import math as m
print(m.pi)

import numpy as np
import matplotlib.pyplot as plt
```

## Première bibliothèque: math

Il faut importer la bibliothèque math avant d'utiliser les fonctions ou variables de cette bibliothèque.

|math.pi|math.floor(x)|math.sqrt(x)|
|:-:|:-:|:-:|
|π|⌊x⌋ `#!python math.floor(-3.7)==-4`|√x `#!python math.sqrt(9)==3`|

`#!python math.pi` n'est pas une fonction mais une variable, il ne faut donc pas écrire `#!python math.pi()` mais `#!python math.pi`.

## Bibliothèque fractions

Permet de manipuler des fractions. Toutes les opérations possibles avec les entiers et les flottants sont aussi possibles avec les fractions.
Les fractions sont toujours automatiquement simplifiées.

Ne pas écrire `#!python from Fraction import *`, mais `#!python from fractions import *`.


??? info "Pour mieux comprendre"
    Le nom de la librairie est `#!python fractions` et une classe (un "outil") de cette bibliothèque est `#!python Fraction`. Un import est de la forme `#!python from fichier import outil` ou fichier est le nom de la bibliothèque et outil est le nom de la classe, fonction ou variable qu'on souhaite utiliser.

```python
from fractions import *
numerateur=3
denominateur=12
a=Fraction(numerateur, denominateur)
print(a.numerator)
print(a.denominator)
print(a)
b=Fraction(2, 3)
print(a*b, a/b, a+b, a-b, a//b, a**b)
```
<div class="result" markdown>
``` python title="Renvoie"
1
4  
1/4
1/6 3/8 11/12 -5/12 0 0.3968502629920499
```
</div>

## Symboles de tests

| Symbole | Signification |
|:-:|:-:|
| ==  | Égal |
| <   | Strictement inférieur |
| >   | Strictement supérieur |
| !=  | N'est pas égal |
| <=  | Inférieur ou égal |
| >=  | Supérieur ou égal |

Si le test est vrai (Ex: `6==2*3`), alors il renvoie `#!python True`, sinon `#!python False`.


