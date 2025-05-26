## TP 1 - Introduction à l'algorithmique, présentation de python et exemples

**[Revenir au Sommaire](../README.md)**

Les parties en _italique_ sont des approfondissements qui pourraient être utiles.

- **Quelques symboles**
    
    |+|-|*|**|/|//|_%_|
    |:-:|:-:|:-:|:-:|:-:|:-:|:-:|
    |Addition `1+2==3`|Soustraction `1-2==-1`|Multiplication `2*3==6`|Puissance `2**3==8`|Division `6/2==3`|Quotient division euclidienne `7//2==3`|_Reste division eculidienne `7%2==1`_|

    Les chiffres à virgule s'écrivent avec un point en python. Ex: `1.005`
    
- **Variables et affichage**

    Un algorithme python s'exécute dans l'ordre(1ère ligne->dernière ligne), il faut donc initialiser les variables avant de les utiliser.
    ```python
    a="t"
    b,c=2,3 # b==2 et c==3
    print(a,c,b) # print permet d'afficher des valeurs dans le terminal
    ```
    Python est sensible à la casse, donc `Variable != variable`.

- **Premières fonctions**

    |abs()|int()|max()|min()|round()|
    |:-:|:-:|:-:|:-:|:-:|
    |Valeur absolue `abs(-3)==3`|Supprime la partie fractionnaire `int(-3.7)==-3`|Maximum `max(2,3,6)==6`|Minimum `min(2,3,6)==2`|Arrondi à 10^(-n) près `round(3.577,1)==3.6`|

- **Importer une bibliothèque**

    Une bibliothèque est un ensemble de fonctions et variables prédéfinies.
    Il faut toujours importer la bibliothèque avant d'utiliser une fonction ou variable de cette bibliothèque. Le plus souvent, il est préférable d'importer les bibliothèques au début du fichier, afin quelles soient disponibles dans tout le fichier.
    
    Pour importer une bibliothèque, par exemple la bibliothèque math:
    ```python
    import math
    print(math.pi) # Affiche la valeur de pi
    ```
    Pour importer une fonction ou variable d'une bibliothèque:
    ```python
    from math import pi
    print(pi) # Affiche la valeur de pi
    ```
    Pour importer toutes les fonctions et variables d'une bibliothèque:
    ```python
    from math import *
    print(pi)
    ```
    Il est possible de renommer une bibliothèque _(on appelle ce nouveau nom un alias)_, on l'utilisera surtout pour les bibliothèques `numpy` et `matplotlib.pyplot`:
    ```python
    import math as m
    print(m.pi)

    import numpy as np
    import matplotlib.pyplot as plt
    ```

- **Première bibliothèque: math**
    
    Il faut importer lal bibliothèque math avant d'utiliser les focntions ou variables de cette bibliothèque.

    |math.pi|math.floor(x)|math.sqrt(x)|
    |:-:|:-:|:-:|
    |π|⌊x⌋ `math.floor(-3.7)==-4`|√x `math.sqrt(9)==3`|

    `math.pi` n'est pas une fonction mais une variable, il ne faut donc pas écrire `math.pi()` mais `math.pi`.

- **Bibliothèque fractions**
    
    Ne pas écrire `from Fraction import *`, mais `from fractions import *`.

    _**Pour mieux comprendre:** Le nom de la librairie est `fractions` et une classe (un "outil") de cette bibliothèque est `Fraction`. Un import est de la forme `from fichier import outil` ou fichier est le nom de la bibliothèque et outil est le nom de la classe, fonction ou variable qu'on souhaite utiliser._

    ```python
    from fractions import *
    numerateur=3
    denominateur=12
    a=Fraction(numerateur, denominateur)
    print(a.numerator) # Renvoie le dénominateur de la fraction simplifiée
    print(a.denominator) # Renvoie le numérateur de la fraction simplifiée
    print(a) # Renvoie la fraction simplifiée
    b=Fraction(2, 3)
    print(a*b, a/b, a+b, a-b, a//b, a**b) # Renvoie: 1/6 3/8 11/12 -5/12 0 0.3968502629920499  Mêmes opérations que pour les nombres (int, float).
    ```
- **Symboles de tests**
    |==|<|>|!=|<=|>=|
    |:-:|:-:|:-:|:-:|:-:|:-:|
    |Egal|Strict. inf.|Strict. sup.|N'est pas égal|Inf. ou égal|Sup. ou égal|

    Si le test est vrai (Ex: `6==2*3`), alors il renvoie `True`, sinon `False`.


**[Cours TP 2 →](../TP2/README.md)**