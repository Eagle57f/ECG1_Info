# Exercice 1: Simulation d'une variable aléatoire, sans remise


#   On tire aléatoirement trois cartes d'un jeu de n cartes (sans remise), n>4, les cartes sont
#   numérotées de 0 à n.
#   X est la variable aléatoire qui représente la somme des valeurs des cartes tirées.
#
# 1) Simulez par une fonction X(n) X pour 20 cartes, et renvoyez la valeur de X.
#
# 2) a. Simulez par une fonction Xk(n, k) k tirages, et renvoyez la moyenne de X sur ces k tirages.
#    b. Renvoyez également par la fonction Xk(n, k) le pourcentage de fois où X est supérieur à 2*n.
#
# 3) a. Affichez un graphique de la moyenne de X en fonction de n, pour n variant de 5 à 200,
#       et k=1000.
#    b. Affichez sur ce même graphique le pourcentage de fois où X est supérieur à 2*n en fonction
#       de n, pour n variant de 5 à 200, et k=1000.
#    c. Affichez la droite d'équation y=1.5x en pointillés rouges sur le graphique précédent,
#       la droite doit être derrière les autres courbes sur le graphique (il faut donc mettre
#       la ligne de code pour créer la droite avant celles pour créer les courbes).
#    d. Ajoutez un titre, des labels aux axes, une grille et une légende.





# Correction de l'exercice 1:







# 1)

import random

def X(n):
    L=[i for i in range(0, n+1)]
    s=0
    for _ in range(3):
        x=random.randint(0, len(L)-1)
        a=L.pop(x)
        s+=a
    return s  
print(X(7))


# 2)

def Xk(n, k):
    total = 0
    sup=0
    for _ in range(k):
        x=X(n)
        total += x
        if x > 2*n:
            sup+=1
    return total/k, sup/k*100

print(Xk(20, 1000))

# 3)

import matplotlib.pyplot as plt
import numpy as np

n_values = np.linspace(5, 200, 196) # 196 car il y a 196 valeurs entre 5 et 200 (les deux extrêmes inclus)
plt.plot(n_values, 1.5*n_values, '--', color='red', label="y = 1.5x") # Ligne rouge en pointillés pour x=y
y_values = [Xk(int(n), 1000)[0] for n in n_values] # On utilise [0] pour obtenir le premier élément des deux retournés par Xk (Donc la moyenne de X)
plt.plot(n_values, y_values, label="Moyenne de X pour n cartes")
y2_values = [Xk(int(n), 1000)[1] for n in n_values] # On utilise [1] pour obtenir le second élément des deux retournés par Xk (Donc le pourcentage de fois où X est supérieur à 2*n)
plt.plot(n_values, y2_values, label="Pourcentage de X > 2*n")
plt.xlabel("Nombre de cartes")
plt.ylabel("Moyenne de X et\npourcentage de X > 2*n")
plt.title("Moyenne de X en fonction de n et pourcentage de fois où X > 2*n,\npour k=1000")
plt.grid()
plt.legend()
plt.show()

