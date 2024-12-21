## TP 3 - Listes

**[Revenir au Sommaire](../README.md)**

Les parties en _italique_ sont des approfondissements qui pourraient être utiles.

- Introduction aux listes

    Une liste est une structure de données qui contient une collection d'objets Python. Ces objets peuvent être des `int`, `float`, `str`, `bool`, d'autres listes, des fonctions, ... Une liste est ordonnée, l'ordre des objets reste le même.

    Une liste s'écrit avec des corchets, et un virgule entre chaque objet de la liste.

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

    Pour concaténer, donc "coller" ensemble deux listes, on utilise le l'opérateur `+`. Pour "coller" la même liste plusieurs fois une derrière l'autre, on utilise l'opérateur `*`.

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
    liste=["1","b", True]
    liste[1]=23.3
    print(liste) # Renvoie ['1', 23.3, True]
    ```

    ```python
    p=[0,2,4,6,8,10]
    for k in range(0,6):
        p[k]=p[k]+1
    print(p) # Renvoie [1, 3, 5, 7, 9, 11]
    ```
