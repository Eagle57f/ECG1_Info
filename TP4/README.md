## TP 4 - Fonctions

**[Revenir au Sommaire](../README.md)**

Les parties en _italique_ sont des approfondissements qui pourraient être utiles.


L'instruction `def` permet de définir une fonction. Cela permet d'éviter de réécrire le même code à plusieurs endroits dans un programme et de réutiliser aisément des morceaux de code. On peut ainsi appeler la fonction à tout moment dans le programme.

- Définir une fonction

Pour créer une fonction, on utilise le mot-clé `def` suivi du nom de la fonction, de ses paramètres entre parenthèses, et d’un deux-points. Le corps de la fonction est indenté. Par exemple :

```python
def fonction(x):
    y = x**2
    return y
    return "patate"  # Cette ligne ne sera jamais exécutée
```

*Attention : dès qu'un `return` est rencontré, la fonction se termine. Ici, le second `return` ne sera jamais atteint.*


- Différentes formes usuelles de fonctions
    - Procédures

    Une fonction qui n'utilise pas de `return` est appelée une procédure. Elle sert principalement à exécuter des instructions (par exemple, afficher des résultats) sans renvoyer de valeur.

    ```python
    def affiche_message():
        print("Bonjour")
    ```

    - Fonctions avec conditions

    On peut intégrer des conditions dans une fonction pour modifier son comportement en fonction des valeurs d'entrée :

    ```python
    def signe(x):
        if x > 0:
            return "positif"
        elif x < 0:
            return "négatif"
        else:
            return "nul"
    ```

    - Fonctions avec plusieurs arguments

    Les fonctions peuvent prendre plusieurs paramètres, ce qui permet de travailler sur plusieurs valeurs à la fois :

    ```python
    def somme(a, b, c):
        return a + b + c
    ```

    - Fonctions appelant d’autres fonctions

    Une fonction peut faire appel à une autre pour réaliser une tâche plus complexe :

    ```python
    def carre(x):
        return x**2

    def somme_des_carres(a, b):
        return carre(a) + carre(b)
    ```

    - Fonctions récursives

    Une fonction récursive s'appelle elle-même pour résoudre un problème en le décomposant en sous-problèmes plus simples. Il est essentiel de prévoir une condition d'arrêt pour éviter une récursion infinie.


    Quelques exemples :
    ```python
    def factorielle(n):
        if n == 0:
            return 1
        else:
            return n * factorielle(n - 1)
    ```

    ```python
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    ```

    ```python
    def puissance(x, n):
        """
        Calcul de la puissance n-ième d’un réel x.
        """
        if n == 0:
            if x == 0:
                print("impossible")
            else:
                return 1
        elif n % 2 == 0:
            y = puissance(x, n // 2) ** 2
        else:
            y = x * puissance(x, n - 1)
        return y

    x = eval(input("Entrer le réel x : "))
    n = eval(input("Entrer la puissance entière positive n : "))
    print(puissance(x, n))

    ```

    ```python
    def u(n):
        """
        Calcule le n-ième terme de la suite définie par :
        U_0 = 1
        U_n = (U_{n-1} + 1) / (U_{n-1} + 2)
        """
        if n == 0:
            return 1
        # Appel récursif :
        u_prec = U(n - 1)
        return (u_prec + 1) / (u_prec + 2)
    ```

    ```python
    def count_digits(n):
        """
        Renvoie le nombre de chiffres qui composent l'entier n.
        On utilise la division euclidienne par 10 pour retirer le dernier chiffre.
        """
        n = abs(n) # On travaille avec la valeur absolue pour gérer les nombres négatifs
        
        if n < 10:
            return 1 # Cas de base : s'il n'y a qu'un seul chiffre, on renvoie 1.
        
        else:
            return 1 + count_digits(n // 10)# Appel récursif : on enlève le dernier chiffre et on ajoute 1 au résultat.

    # Exemples de test :
    print(count_digits(5))      # Affiche 1
    print(count_digits(1234))   # Affiche 4
    print(count_digits(0))      # Affiche 1
    print(count_digits(-98765)) # Affiche 5
    ```


<div style="display: flex; justify-content: space-between;">
  <a href="../TP3/README.md" style="font-weight:bold">← Chapitre 3</a>
  <a href="../TP5/README.md" style="font-weight:bold">Chapitre 4 →</a>
</div>