# Exercices

## Sommaire
- [Exercices Probabilités](#exercices-probabilit%C3%A9s)
    - [Exercice 1: Simulation d'une variable aléatoire, sans remise](#exercice-1-simulation-dune-variable-al%C3%A9atoire-sans-remise)
    - [Exercice 2: Chaîne de Markov](#exercice-2-cha%C3%AEne-de-markov)
- [Exercice Méthode de Monte-Carlo](#m%C3%A9thode-de-monte-carlo)

## Exercices Probabilités

### Exercice 1: Simulation d'une variable aléatoire, sans remise

#### [Correction](https://github.com/Eagle57f/ECG1_Info/blob/main/Ressources-Exercices-Corrections/Exercices/Exercice%20Probabilit%C3%A9s%201.py)

On tire aléatoirement trois cartes d'un jeu de n cartes (sans remise), n>4, les cartes sont numérotées de 0 à n-1. X est la variable aléatoire qui représente la somme des valeurs des cartes tirées.

1) Simulez par une fonction X(n) X pour 20 cartes, et renvoyez la valeur de X.

2) a. Simulez par une fonction Xk(n, k) k tirages, et renvoyez la moyenne de X sur ces k tirages.

   b. Renvoyez également par la fonction Xk(n, k) le pourcentage de fois où X est supérieur à 2*n.

3) a. Affichez un graphique de la moyenne de X en fonction de n, pour n variant de 5 à 200, et k=1000.

   b. Affichez sur ce même graphique le pourcentage de fois où X est supérieur à 2*n en fonction de n, pour n variant de 5 à 200, et k=1000.

   c. Affichez la droite d'équation y=1.5x en pointillés rouges sur le graphique précédent, la droite doit être derrière les autres courbes sur le graphique (il faut donc mettre la ligne de code pour créer la droite avant celles pour créer les courbes).

   d. Ajoutez un titre, des labels aux axes, une grille et une légende.


### Exercice 2: Chaîne de Markov

#### [Correction](https://github.com/Eagle57f/ECG1_Info/blob/main/Ressources-Exercices-Corrections/Exercices/Exercice%20Probabilit%C3%A9s%202.py)

  On considère un système avec 3 états numérotés 0, 1, et 2. Le système évolue de manière probabiliste selon les transitions suivantes:
  - Au temps t=0, le système est dans l'état 0 avec une probabilité de 1.
  - Si l'état actuel est 0, il peut passer à 0 avec une probabilité de 0.3, à 1 avec une probabilité de 0.4, et à 2 avec une probabilité de 0.3.
  - Si l'état actuel est 1, il peut passer à 0 avec une probabilité de 0.2, à 1 avec une probabilité de 0.5, et à 2 avec une probabilité de 0.3.
  - Si l'état actuel est 2, il peut passer à 0 avec une probabilité de 0.6, à 1 avec une probabilité de 0.3, et à 2 avec une probabilité de 0.1.

  La variable aléatoire X représente l'état du système à chaque instant t.

1) Créez une fonction transition_etat(etat) qui prend l'état actuel en entrée et renvoie le nouvel état après une transition aléatoire en fonction des probabilités données, affichez le nouvel état avec comme état actuel l'état 1.

2) Créez une fonction simulation_markov(k) qui simule k transitions successives et renvoie la suite d'états traversés grâce à une liste, affichez cette liste pour k=20.

3) Créez une fonction pourcentages_etats(etats) qui prend en entrée la liste des états et renvoie le pourcentage de fois où le système est dans l'état 0, 1 ou 2 après k transitions. Affichez ces pourcentages pour k=20.


## Méthode de Monte-Carlo

#### [Correction](https://github.com/Eagle57f/ECG1_Info/blob/main/Ressources-Exercices-Corrections/Exercices/Exercice%20M%C3%A9thode%20de%20Monte-Carlo.py)

Méthode de Monte-Carlo pour calculer l'aire sous la courbe de `exp(x)` entre a et b.


Explication de la méthode de Monte-Carlo pour la fonction `exp`:
1. On choisit un intervalle [a, b] et on génère n_points points aléatoires dans un rectangle de largeur b-a et de hauteur `max(exp(t))` pour t allant de a à b.
2. On compte combien de ces points sont sous la courbe de `exp(x)`.
3. L'aire sous la courbe est approximée par le ratio du nombre de points sous la courbe sur le nombre total de points, multiplié par l'aire du rectangle.

Consigne :

La fonction `monte_carlo_exp` prend en entrée les bornes a et b de l'intervalle ainsi que le nombre de points n_points à générer. Elle renvoie l'aire sous la courbe de la fonction exp entre a et b, et affiche un graphique avec la courbe de exp entre a et b, ainsi qu'un nuage de points, avec les points sous la courbe en vert et ceux au-dessus en rouge.

Complétez la fonction `monte_carlo_exp`.

BONUS: Transformez la fonction `monte_carlo_exp` pour qu'elle fonctionne pour n'importe quelle fonction mathématique.

```python
import random as rd
import math
import matplotlib.pyplot as plt

def monte_carlo_exp(a, b, n_points):
    y_max = max([_____(a + (b - a) * i / 1000) for i in range(1001)])
    count_under_curve = 0

    xs_in, ys_in = [], []
    xs_out, ys_out = [], []

    for i in range(_____):
        x = rd.uniform(a, b)
        y = rd.uniform(0, y_max)
        if y <= math.exp(x):
            count_under_curve = count_under_curve + _____
            xs_in._____(x)
            ys_in._____(y)
        else:
            xs_out._____(x)
            ys_out._____(y)

    area_rectangle = _____
    area_under_curve = (count_under_curve / n_points) * area_rectangle

    x_curve = [a + (b - a) * i / 1000 for i in range(1001)]
    y_curve = [_____ for x in x_curve]
    plt.plot(x_curve, y_curve, color='black', label='exp(x)')
    plt._____(_____, _____, color='green', s=1, label='Sous la courbe')
    plt._____(_____, _____, color='red', s=1, label='Au-dessus')
    plt.xlim(a, b)
    plt.ylim(0, y_max)
    plt.legend()
    plt._____(f"Monte Carlo pour aire sous exp(x) entre {a} et {b}: {round(area_under_curve, 3)}")
    plt._____("x")
    plt._____("y")
    plt._____()

    return _____


a = 0
b = 7
n_points = 1000
aire = monte_carlo_exp(a, b, n_points)
print(f"Aire approximative sous exp(x) entre {a} et {b} : {aire}")
```
