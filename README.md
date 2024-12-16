# Cours d'informatique en ECG1-2

Les parties en <span style="color: red;">rouge</span> sont des approfondissements qui pourraient être utiles.

<details>
  <summary style="font-weight: bold">Quelques ressources pour appronfondir <span style="font-style: italic">(cliquez pour afficher)</span></summary>
  
- **Vidéos (ou playlists):**
    - Graven (FR): https://www.youtube.com/watch?v=psaDHhZ0cPs&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR
    - Docstring (FR): https://www.youtube.com/watch?v=LamjAFnybo0&list=PLXDBYzqsqO3Wut-gQktoqJ30eaOel0hgb
    -FormationVidéo (FR): https://www.youtube.com/watch?v=HWxBtxPBCAc&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC
    - NetworkChuck (EN): https://www.youtube.com/watch?v=mRMmlo_Uqcs
    - freeCodeCamp.org (EN): https://www.youtube.com/watch?v=LHBE6Q9XlzI

- **Sites web:**
    - Python Doctor (FR): https://python.doctor/
    - w3schools (EN, pour tous les languages): https://www.w3schools.com/

- **Pour vous entrainer:**
    - Edabit (EN): https://edabit.com/challenges
    - HackerRank (EN): https://www.hackerrank.com/dashboard
</details>




## TP 1 - Introduction à l'algorithmique, présentation de python et exemples

- **Quelques symboles**
    
    |+|-|*|**|/|//|<span style="color: red;">%</span>|
    |:-:|:-:|:-:|:-:|:-:|:-:|:-:|
    |Addition `1+2==3`|Soustraction `1-2==-1`|Multiplication `2*3==6`|Puissance `2**3==8`|Division `6/2==3`|Quotient division euclidienne `7//2==3`|<span style="color: red;">Reste division eculidienne</span> `7%2==1`|

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

- **Première bibliothèque: math**

    Il faut toujours importer la bibliothèque avant d'utiliser une fonction ou variable de cette bibliothèque. Le plus souvent, il est préférable d'importer les bibliothèques au début du fichier, afin quelles soient disponibles dans tout le fichier.
    
    Pour importer la bibliothèque math:
    ```python
    import math
    print(math.pi)
    # OU
    from math import *
    print(pi)
    ```

    |math.pi|math.floor(x)|math.sqrt(x)|
    |:-:|:-:|:-:|
    |π|⌊x⌋ `math.floor(-3.7)==-4`|√x `math.sqrt(9)==3`|

    `math.pi` n'est pas une fonction mais une variable, il ne faut donc pas écrire `math.pi()` mais `math.pi`.

- **Bibliothèque fractions**
    
    Ne pas écrire `from Fraction import *`, mais `from fractions import *`.

    <span style="color: red;">**Pour mieux comprendre:** Le nom de la librairie est `fractions` et une classe (un "outil") de cette bibliothèque est `Fraction`. Un import est de la forme `from fichier import outil` ou fichier est le nom de la bibliothèque et outil est le nom de la classe, fonction ou variable qu'on souhaite utiliser.</span>

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
- **Tests**
    |==|<|>|!=|<=|>=|
    |:-:|:-:|:-:|:-:|:-:|:-:|
    |Egal|Strict. inf.|Strict. sup.|N'est pas égal|Inf. ou égal|Sup. ou égal|

    Si le test est vrai (Ex: `6==2*3`), alors il renvoie `True`, sinon `False`.

## TP 2 - Boucles for et while, tests
- Fonctions : 
    ```python
    input, eval
    type(input())==str
    ```
- Boucles for et intendations
    ```python
    for i in range(a, b): # Donc prenant les valeurs entre a et b-1, type(a)==type(b)==int
        ...
    ```
- Sommes, produits, limites avec boucles for
    ```python
    s=0
    for i in range(a, b):
        s+=...
    print(s)

    p=0
    for i in range(a, b):
        p*=...
    print(p)
    # Limites avec b très grand
    ```
- Boucles while
    ```python
    while a>b:
        ...
    ```
- Suites avec boucles while
    ```python
    u=0
    while u<20:
        u+=2
    print(u)
    ```
- Fonctions de la bibliothèque math: 
    ```python
    import math
    math.exp, math.log, math.log2, math.log10
    ```
- Tests
    ```python
    a=eval(input("Donnez un chiffre appartenant à Z: "))
    if a==0:
        ...
    elif a>0:
        ...
    else:
        ...
    ```
- Fonction de la bibliothèque random:
    ```python
    import random
    random.random() # Renvoie un float entre O et 1 inclus
    ```
- Algorithme de dichotomie
    ```python
    def d(a,b,f,p): # a et b deux réels entre lesquels il faut trouver alpha tel que f(alpha)=0, f la fonction et p la précision (par exemple 0.001)
        while abs(b-a)>p:
            if (f(a)*f((a+b)/2)<0):
                b=(a+b)/2
            else:
                a=(a+b)/2
        return [a,(a+b)/2,b] # x est compris entre a et b, et (a+b)/2 est le milieu de cet intervalle
    def f(x): return ... # Fonction, par exemple x**3+3*x-5
    print(d(10,1,f,0.0001))
    ```