## TP 5 - Matrices avec Numpy

**[Revenir au Sommaire](../README.md)**

Les parties en _italique_ sont des approfondissements qui pourraient être utiles.

- Création de matrices

    Pour créer uen matrice, il faut utiliser la fonction `array` de la bibliothèque `numpy`.

    ```python
    import numpy as np
    matrice=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # Renvoie [[1 2 3] [4 5 6] [7 8 9]]
    print(matrice)
    ```

    ```python
    from numpy import *
    matrice=array([[1, 2, 3], [4, 5, 6]])
    print(matrice) # Renvoie [[1 2 3] [4 5 6]]
    ```

    Sur python, il est possible de revenir à la ligne entre les différents objets d'une liste, afin de rendre la liste ou matrice plus lisible.

    ```python
    import numpy as np
    matrice=np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ])
    print(matrice) # Renvoie [[1 2 3] [4 5 6] [7 8 9]]
    ```

    Certaines matrices utiles sont générées grâce à des fonctions:
    
    ```python
    import numpy as np
    matrice0=np.zeros((3, 3))
    print(matrice0) # Renvoie [[0 0 0] [0 0 0] [0 0 0]]
    matrice1=np.ones((2, 3))
    print(matrice1) # Renvoie [[1 1 1] [1 1 1]]
    identite=np.eye(4)
    print(identite) # Renvoie [[1. 0. 0. 0.] [0. 1. 0. 0.] [0. 0. 1. 0.] [0. 0. 0. 1.]]
    ```

- Fonctions et opérations sur les matrices

    Pour accéder à un élément d'une matrice, on utilise les crochets `[ligne, colonne]`, presque comme pour les listes. Il est également possible d'utilises les `:`

    ```python
    import numpy as np
    matrice=np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
    print(matrice[1, 2]) # Renvoie 6
    print(matrice[1:3]) # Renvoie [[4 5 6] [7 8 9]]
    print(matrice[1:3, 1:3]) # Renvoie [[5 6] [8 9]]
    ```

    Pour connaitre le nombre d'éléments d'une matrice, on utilise la fonction `size` de `numpy`.

    ```python
    import numpy as np
    matrice=np.array([[1, 2, 3], [4, 5, 6]])
    print(np.size(matrice)) # Renvoie 6
    ```

    Pour connaitre le nombre de lignes et de colonnes d'une matrice, on utilise la fonction `shape` de `numpy`.

    ```python
    import numpy as np
    matrice=np.array([[1, 2, 3], [4, 5, 6]])
    print(np.shape(matrice)) # Renvoie (2, 3)
    ```

    Pour multiplier une matrice par une deuxième matrice, on utilise la fonction `dot` de `numpy`, ou l'opérateur `@` à partir de Python 3.5.

    ```python
    import numpy as np
    matrice1=np.array([[1, 2, 3], [4, 5, 6]])
    matrice2=np.array([[1, 2], [3, 4], [5, 6]])
    print(np.dot(matrice1, matrice2)) # Renvoie [[22 28] [49 64]]
    print(matrice1 @ matrice2) # Renvoie [[22 28] [49 64]]
    ```

    Pour faire le produit terme à terme de deux matrices, on utilise l'opérateur `*`.

    ```python
    import numpy as np
    matrice1=np.array([[1, 2, 3], [4, 5, 6]])
    matrice2=np.array([[7, 8, 9], [10, 11, 12]])
    print(matrice1*matrice2) # Renvoie [[7 16 27] [40 55 72]]
    ```

    Pour obtenir la transposée d'ue matrice, on utilise la fonction `T` de `numpy`.

    ```python
    import numpy as np
    matrice=np.array([[1, 2, 3], [4, 5, 6]])
    print(matrice.T) # Renvoie [[1 4] [2 5] [3 6]]
    ```

    Pour obtenir le déterminant d'une matrice, on utilise la fonction `det` de `numpy.linalg`.

    ```python
    import numpy as np
    import numpy.linalg as al
    matrice22=np.array([[1, 2], [3, 4]])
    print(al.det(matrice22)) # Renvoie -2.0000000000000004
                             # (Python à des problèmes au niveau de l'arrondi lors des opérations)
    ```

    ```python
    import numpy as np
    from numpy.linalg import *
    matrice33=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(det(matrice33)) # Renvoie 0.0
    ```

    Pour obtenir l'inverse d'une matrice, on utilise la focntion `inv` de `numpy.linalg`.

    ```python
    import numpy as np
    matrice22=np.array([[1, 2], [3, 4]])
    print(np.linalg.inv(matrice22)) # Renvoie [[-2. 1.], [ 1.5 -0.5]]
    ```

