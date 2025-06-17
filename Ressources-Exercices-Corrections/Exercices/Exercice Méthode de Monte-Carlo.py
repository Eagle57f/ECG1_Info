# Exercice : Méthode de Monte-Carlo pour calculer l'aire sous la courbe de exp(x) entre a et b


# Explication de la méthode de Monte-Carlo :
# 1. On choisit un intervalle [a, b] et on génère n_points points aléatoires dans un rectangle
#    de largeur b-a et de hauteur max(exp(t)) pour t allant de a à b.
# 2. On compte combien de ces points sont sous la courbe de exp(x).
# 3. L'aire sous la courbe est approximée par le ratio du nombre de points sous la courbe sur
#    le nombre total de points, multiplié par l'aire du rectangle.

# Consigne :
# La fonction monte_carlo_exp prend en entrée les bornes a et b de l'intervalle ainsi que le
# nombre de points n_points à générer. Elle renvoie l'aire sous la courbe entre a et b, et
# affiche un graphique avec la courbe de exp entre a et b, ainsi qu'un nuage de points, avec
# les points sous la courbe en vert et ceux au-dessus en rouge.
# Complétez la fonction monte_carlo_exp.



# Correction possible:


import random as rd
import math
import matplotlib.pyplot as plt

def monte_carlo_exp(a, b, n_points):
    y_max = max([math.exp(a + (b - a) * i / 1000) for i in range(1001)])
    count_under_curve = 0

    xs_in, ys_in = [], []
    xs_out, ys_out = [], []

    for i in range(n_points):
        x = rd.uniform(a, b)
        y = rd.uniform(0, y_max)
        if y <= math.exp(x):
            count_under_curve += 1
            xs_in.append(x)
            ys_in.append(y)
        else:
            xs_out.append(x)
            ys_out.append(y)

    area_rectangle = (b - a) * y_max
    area_under_curve = (count_under_curve / n_points) * area_rectangle

    x_curve = [a + (b - a) * i / 1000 for i in range(1001)]
    y_curve = [math.exp(x) for x in x_curve]
    plt.plot(x_curve, y_curve, color='black', label='exp(x)')
    plt.scatter(xs_in, ys_in, color='green', s=1, label='Sous la courbe')
    plt.scatter(xs_out, ys_out, color='red', s=1, label='Au-dessus')
    plt.xlim(a, b)
    plt.ylim(0, y_max)
    plt.legend()
    plt.title(f"Monte Carlo pour aire sous exp(x) entre {a} et {b}: {round(area_under_curve, 3)}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

    return area_under_curve


a = 0
b = 7
n_points = 1000
aire = monte_carlo_exp(a, b, n_points)
print(f"Aire approximative sous exp(x) entre {a} et {b} : {aire}")

# Correction question BONUS


import random as rd
import math
import matplotlib.pyplot as plt

def monte_carlo_exp(a, b, n_points, f):
    y_max = max([f(a + (b - a) * i / 1000) for i in range(1001)])
    count_under_curve = 0

    xs_in, ys_in = [], []
    xs_out, ys_out = [], []

    for i in range(n_points):
        x = rd.uniform(a, b)
        y = rd.uniform(0, y_max)
        if y <= f(x):
            count_under_curve += 1
            xs_in.append(x)
            ys_in.append(y)
        else:
            xs_out.append(x)
            ys_out.append(y)

    area_rectangle = (b - a) * y_max
    area_under_curve = (count_under_curve / n_points) * area_rectangle

    x_curve = [a + (b - a) * i / 1000 for i in range(1001)]
    y_curve = [f(x) for x in x_curve]
    plt.plot(x_curve, y_curve, color='black', label='f(x)')
    plt.scatter(xs_in, ys_in, color='green', s=1, label='Sous la courbe')
    plt.scatter(xs_out, ys_out, color='red', s=1, label='Au-dessus')
    plt.xlim(a, b)
    plt.ylim(0, y_max)
    plt.legend()
    plt.title(f"Monte Carlo entre {a} et {b}: {round(area_under_curve, 3)}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

    return area_under_curve


a = 1
b = 7
n_points = 1000
aire = monte_carlo_exp(a, b, n_points, math.log) # Autre fonction, comme exemple
print(f"Aire approximative entre {a} et {b} : {aire}")