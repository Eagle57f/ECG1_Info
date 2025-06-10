## TP 3 - Listes

**[Revenir au Sommaire](../README.md)**

Les parties en _italique_ sont des approfondissements qui pourraient être utiles.

- Introduction aux listes

    Une liste est une structure de données qui contient une collection d'objets Python. Ces objets peuvent être des `int`, `float`, `str`, `bool`, d'autres listes, des fonctions, ... Une liste est une structure ordonnée, ce qui signifie que l'ordre des éléments est préservé.

    Une liste s'écrit avec des crochets, et une virgule entre chaque objet de la liste.

    ```python
    liste_a = [1, -3, "Bonjour", "", True, 1.06, ["Deuxième", "liste"]]
    liste_b = [] # Une liste peut être vide
    ```

    Les éléments d'une liste sont numérotés, le premier élément est l'élément d'indice 0, le deuxième d'indice 1, ...
    De plus, le dernier élément est l'élément d'indice -1, l'avant dernier d'indice -2, ... Ce qui permet de pouvoir accéder au dernier élément de la liste sans connaître la longueur de celle-ci.

    ```python
    liste_a = [1, -3, "Bonjour", "", True, 1.06, ["Deuxième", "liste"]]
    
    print(liste_a[0]) # Renvoie 1
    print(liste_a[2]) # Renvoie "Bonjour"
    print(liste_a[6]) # Renvoie ["Deuxième", "liste"]
    print(liste_a[-1]) # Renvoie ["Deuxième", "liste"]
    print(liste_a[-2]) # Renvoie 1.06
    ```

    Pour concaténer, donc "coller" ensemble deux listes, on utilise l'opérateur `+`. Pour "coller" la même liste plusieurs fois une derrière l'autre, on utilise l'opérateur `*`.

    ```python
    liste_a = [1, 2, 3, 4]
    liste_b = ["5", "6", "7"]
    print(liste_a+liste_b) # Renvoie [1, 2, 3, 4, "5", "6", "7"]
    print(liste_b+liste_a) # Renvoie ["5", "6", "7", 1, 2, 3, 4]
    print(liste_a*3) # Renvoie [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
    ```

    On peut parcourir une liste en utilisant une boucle `for`:

    ```python
    v=""
    for i in ["a", "b", "c", "d"]:
        v = v+i
    print(v) # Renvoie "abcd"
    ```

    De même qu'une liste, on peut parcourir une chaîne de caractères:
 
    ```python
    liste=[]
    for i in "Une phrase":
        liste = liste+[i]
    print(liste) # Renvoie ['U', 'n', 'e', ' ', 'p', 'h', 'r', 'a', 's', 'e']
    ```

    Pour ajouter un élément à une liste, on utilise la fonction `.append()`:

    ```python
    liste=["1","b", True]
    liste.append("bonjour")
    print(liste) # Renvoie ['1', 'b', True, 'bonjour']
    ```

    Pour changer la valeur d'un élément on utilise l'opérateur `=`:

    ```python
    liste=["1", 23.3, True]
    liste[1]=23.3
    print(liste) # Renvoie ['1', 23.3, True]
    ```

    ```python
    p=[0,2,4,6,8,10]
    for k in range(0,6):
        p[k]=p[k]+1
    print(p) # Renvoie [1, 3, 5, 7, 9, 11]
    ```

    Pour connaitre le nombre d'éléments d'une liste, on utilise la fonction `len()`:

    ```python
    liste=["1","b", True]
    print(len(liste)) # Renvoie 3
    ```

    Pour supprimer un élément d'une liste dont **on connait l'emplacement** dans la liste, on utilise le mot clé `del`:

    ```python
    liste=["1","b", True]
    del liste[1]
    print(liste) # Renvoie ['1', True]
    ```

    On peut créer des listes de listes (utile pour les matrices par exemple):

    ```python
    liste=[[1,2,3],[4,5,6],[7,8,9]]
    print(liste[1][2]) # Renvoie 6
    print(liste[2][-1]) # Renvoie 9

    l1=[1,2,3]
    l2=[4,5,6]
    liste=[l1,l2]
    print(liste[1]) # Renvoie [4,5,6]
    ```

    Pour extraire une partie de liste, on utilise la syntaxe `[debut:fin:pas]` _(on appelle cette manipulation `slicing`)_:
    La valeur finale n'est pas atteinte.
    ```python
    liste=[1,2,3,4,5,6,7,8,9]
    print(liste[1:5]) # Renvoie [2, 3, 4, 5]
    print(liste[1:5:2]) # Renvoie [2, 4]
    print(liste[::2]) # Renvoie [1, 3, 5, 7, 9]
    print(liste[::-1]) # Renvoie [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(liste[5:2:-1]) # Renvoie [6, 5, 4]
    ```

- Fonctions utiles pour les listes
    
    - `.count(élément)`: Permet de compter le nombre d'occurences d'un élément dans une liste.

    ```python
    liste=["a", "b", "a", "b", "c", "b", "a", "a"]
    print(liste.count("a")) # Renvoie 4
    ```

    - `.index(élément)`: Permet de connaitre l'indice de la première occurence d'un élément dans une liste.

    ```python
    liste=["a", "b", "a", "b", "c", "b", "a", "a"]
    print(liste.index("b")) # Renvoie 1
    ```

    - `.pop(index)`: Supprime un élément d'une liste à un index (emplacement dans la liste) spécifique et renvoye cet élément. Si aucun index n'est spécifié, elle supprime et retourne le dernier élément de la liste.

    ```python
    liste=["a", "b", "a", "b", "c", "b", "a", "a"]
    print(liste.pop(3)) # Renvoie "b"
    print(liste) # Renvoie ['a', 'b', 'a', 'c', 'b', 'a', 'a']
    var = liste.pop()
    print(var) # Renvoie "a"
    print(liste) # Renvoie ['a', 'b', 'a', 'c', 'b', 'a']
    ```

    - `.insert(index, élément)` : Permet d'insérer un élément à un index spécifique.

    ```python
    liste=["a", "b", "a", "b", "c", "b"]
    liste.insert(2, "d")
    print(liste) # Renvoie ['a', 'b', 'd', 'a', 'b', 'c', 'b']
    ```

    - `.reverse()` : Permet d'inverser l'ordre des éléments d'une liste.

    ```python
    liste=["a", "b", "a", "b", "c", "b"]
    liste.reverse()
    print(liste) # Renvoie ['b', 'c', 'b', 'a', 'b', 'a']
    ```

    - `.remove(élément)` : Permet de supprimer la première occurence d'un élément dans une liste.

    ```python
    liste=["a", "b", "a", "b", "c", "b"]
    liste.remove("b")
    print(liste) # Renvoie ['a', 'a', 'b', 'c', 'b']
    ```

    - `.sort()` : Permet de trier une liste.

    ```python
    liste=[3, 1, 4, 1, -5, 9, 2, 6, 5, 3, 5]
    liste.sort()
    print(liste) # Renvoie [-5, 1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
    liste2=["a", "c", "b", "d"]
    liste2.sort()
    print(liste2) # Renvoie ['a', 'b', 'c', 'd']
    ```

    - `max(liste)` : Permet de connaitre la valeur maximale d'une liste, `min(liste)` : Permet de connaitre la valeur minimale d'une liste.

    ```python
    liste=[3, 1, 4, 1, -5, 9, 2, 6, 5, 3, 5]
    print(max(liste)) # Renvoie 9
    print(min(liste)) # Renvoie -5
    ```

    - `sum(liste)` : Permet de calculer la somme de tout les éléments de la liste.

    ```python
    liste=[3, 1, 4, 1, -5, 9, 2, 6, 5, 3, 5]
    print(sum(liste)) # Renvoie 34
    ```

- Divers

    - On peut générer des listes grâce à des boucles `for`:

    ```python
    liste=[i for i in range(10)]
    print(liste) # Renvoie [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    liste=[i for i in range(10) if i%2==0]
    print(liste) # Renvoie [0, 2, 4, 6, 8]
    abscisse=[0, 1, 2, 3, 4, 5, 6, 7 ]
    ordonnée=[ 3*x+5 for x in abscisse] # Images des éléments de abscisse par la fonction x ↦ 3*x+5
    print(ordonnée) # Renvoie [5, 8, 11, 14, 17, 20, 23, 26]
    ```

    - Copie des listes et effet de bord

    En Python, lorsqu'on affecte une liste à une autre variable avec =, cela ne crée pas une nouvelle liste mais une référence vers la même liste. Toute modification de l'une affectera donc l'autre.


    ```python
    liste_a = [1, 2, 3]
    liste_b = liste_a  # liste_b référence la même liste que liste_a
    liste_b.append(4)

    print(liste_a)  # Renvoie [1, 2, 3, 4]
    print(liste_b)  # Renvoie [1, 2, 3, 4]
    ```

    Pour éviter cet effet de bord, on peut utiliser la méthode `.copy()`, `list()`, ou le slicing `[:]` afin de créer une vraie copie indépendante de la liste :

    ```python
    liste_a = [1, 2, 3]

    # Copie indépendante de liste_a
    liste_b = liste_a.copy()  
    liste_c = list(liste_a)
    liste_d = liste_a[:]  # Slicing

    liste_b.append(4)
    print(liste_a)  # Renvoie [1, 2, 3] (liste_a n'a pas été modifiée)
    print(liste_b)  # Renvoie [1, 2, 3, 4]
    print(liste_c)  # Renvoie [1, 2, 3]
    print(liste_d)  # Renvoie [1, 2, 3]
    ```

**[← Cours TP 2](../TP2/README.md)**
**[Cours TP 4 →](../TP4/README.md)**