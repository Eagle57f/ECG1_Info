# Cours d'informatique en ECG1-2

## TP 1 - Introduction à l'algorithmique, présentation de python et exemples

- Quelques symboles d'opération
    ```python
    +, -, *, **, /, //
    ```
- Variables et affichage
    ```python
    a="t"
    b,c=2,3
    print(a,c,b)
    ```
- Premières fonctions
    ```python
    abs, int, max, min, round
    ```
- Première bibliothèque
    ```python
    import math
    math.pi, math.floor, math.sqrt
    ```
- Bibliothèque Fractions 
    ```python
    from Fractions import *
    a=Fractions(numérateur, dénominateur)
    a.numerator
    a.denominator
    Mêmes opérations que pour int et float
    ```
- Tests
    ```python
    bool: True,False
    ==, <, >, !=, <=, >=
    ```

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