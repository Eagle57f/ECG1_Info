---
hide:
  - toc
---


# DS Final Info — ECG1-2


<a href="../Ressources-Exercices-Corrections/Corrections/DS Final 2024.py" download>**Télécharger la correction**</a>


## I. Exercices sur les suites

### I.1 Suites récurrentes

Pour chaque suite définie ci-dessous, écrire une fonction Python prenant en paramètre un entier naturel \( n \) et renvoyant la valeur de \( u_n \). On privilégiera une écriture récursive.

1.  
\[
\begin{cases}
u_0 = 2 \\
u_{n+1} = 3u_n^2 - 1
\end{cases}
\]

2.  
\[
\begin{cases}
u_1 = 0 \\
u_{n+1} = e^{-u_n}
\end{cases}
\]

3.  
\[
\begin{cases}
u_0 = 1,\quad u_1 = 1 \\
u_{n+2} = u_{n+1} + u_n
\end{cases}
\]

4.  
\[
\begin{cases}
u_0 = 1 \\
u_{n+1} = \sum_{k=0}^{n} \frac{u_k}{k^2 + 1}
\end{cases}
\]

Démontrer que :

\[
u_{n+1} = u_n \cdot \frac{n^2 + 2}{n^2 + 1}
\]

---

## I.2 Suites imbriquées

Soient \( (a_n) \) et \( (b_n) \) définies par :

\[
a_0 = 0,\quad b_0 = 1
\]

\[
a_{n+1} = 2a_n + b_n,\quad b_{n+1} = 2a_n + 3b_n
\]

1. Calculer \( a_1, b_1, a_2, b_2 \)

2. Écrire une fonction Python `suites(n)` qui renvoie \( a_n \) et \( b_n \)

3. Soit \( s_n = a_n + b_n \). Déterminer une relation de récurrence entre \( s_n \) et \( s_{n+1} \)

4. Soit \( t_n = 2a_n - b_n \). Déterminer une relation de récurrence entre \( t_n \) et \( t_{n+1} \)

---

## II. Simulation et fréquences

### II.1 Simulation 1

On lance 3 fois une pièce donnant PILE avec une probabilité \( \frac{1}{3} \). On note \( X \) le nombre de PILE obtenus.

1. Compléter le programme suivant :

```python
from random import *
x = random()
if x < ...:
    piece = "PILE"
else:
    piece = "FACE"
print(piece)
```

2. Écrire une fonction `simulX()` qui renvoie la valeur de \( X \)

3. Donner la loi de probabilité de \( X \) et calculer son espérance

---

### II.2 Simulation 2

On lance une pièce (PILE avec probabilité \( \frac{1}{3} \)) jusqu’à obtenir le premier PILE, ou jusqu’au 4ᵉ lancer.

On note \( X \) le nombre de lancers effectués (maximum 4).

1. Écrire une fonction `simul2X()` qui simule cette variable aléatoire

2. Écrire une fonction `simultiplex(n)` qui renvoie la moyenne de \( n \) simulations de \( X \)

---

## III. Matrices

1. Quelle instruction permet d'importer un module pour manipuler des matrices ?

2. Écrire une instruction qui crée la matrice :

\[
A = \begin{pmatrix}
1 & 2 & 3 \\
2 & -7 & 6
\end{pmatrix}
\]

3. Quelle instruction permet d’effectuer le produit matriciel \( A \cdot B \) ?

4. Quelle instruction permet d’afficher la matrice identité \( I_n \) ?

5. Que renvoie l’instruction `print(np.size(A))` ?

6. Que renvoie `print(A[1,2])` ?

---

## IV. Opérations sur les listes

Chaque QCM comporte 20 questions avec 4 réponses possibles (1 à 4). Une seule réponse est correcte.

La correction est donnée par une liste `corr`, et chaque copie par une liste `cop`.

1. Quelle est la bonne réponse à la question 18 ?

2. Quelle instruction Python permet de l’afficher ?

3. Quel booléen est associé à une réponse fausse ?

4. Écrire la liste `corrTM` correspondant à la correction de la copie de Tom Matt

5. Écrire une fonction `note(cop, corr)` qui renvoie le nombre de bonnes réponses

6. Écrire une fonction `reussite(cop, corr)` qui affiche "Réussite" si la note est ≥ 10, sinon "Échec"

7. Écrire une fonction `note2bonus(cop, corr)` qui ajoute un bonus de 2 points si le candidat a plus de 4 bonnes réponses consécutives (note max : 20)

---

## V. Courbes représentatives

Tracer la courbe de la fonction :

\[
f(x) = e^{x^2}
\]

sur l’intervalle \([-1;2]\), avec 200 points régulièrement espacés.

Bonus : ajouter une légende.



# Correction DS 2024


```python linenums="1"
--8<-- "docs/1ere/Ressources-Exercices-Corrections/Corrections/DS Final 2024.py"
```