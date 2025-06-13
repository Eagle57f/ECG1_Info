# Exercice 1: Simulation d'une variable aléatoire, sans remise


#   On tire aléatoirement trois cartes d'un jeu de n+1 cartes (sans remise), n>4, les cartes sont
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


# ===================================================================================================================================================

# Exercice 2: Chaîne de Markov


#   On considère un système avec 3 états numérotés 0, 1, et 2. Le système évolue de manière
#   probabiliste selon les transitions suivantes:
#   - Au temps t=0, le système est dans l'état 0 avec une probabilité de 1.
#   - Si l'état actuel est 0, il peut passer à 0 avec une probabilité de 0.3, à 1 avec une
#     probabilité de 0.4, et à 2 avec une probabilité de 0.3.
#   - Si l'état actuel est 1, il peut passer à 0 avec une probabilité de 0.2, à 1 avec une
#     probabilité de 0.5, et à 2 avec une probabilité de 0.3.
#   - Si l'état actuel est 2, il peut passer à 0 avec une probabilité de 0.6, à 1 avec une
#     probabilité de 0.3, et à 2 avec une probabilité de 0.1.
#   La variable aléatoire X représente l'état du système à chaque instant t.
#
# 1) Créez une fonction transition_etat(etat) qui prend l'état actuel en entrée et renvoie le
#    nouvel état après une transition aléatoire en fonction des probabilités données, affichez
#    le nouvel état avec comme état actuel l'état 1.
#
# 2) Créez une fonction simulation_markov(k) qui simule k transitions successives et renvoie la
#    suite d'états traversés grâce à une liste, affichez cette liste pour k=20.
#
# 3) Créez une fonction pourcentages_etats(etats) qui prend en entrée la liste des états et
#    renvoie le pourcentage de fois où le système est dans l'état 0, 1 ou 2 après k transitions.
#    Affichez ces pourcentages pour k=20.








# Correction de l'exercice 1:

# 1)

import random

def X(n):
    L=[i for i in range(0, n+1)]
    s=0
    for i in range(3):
        x=random.randint(0, len(L)-1)
        a=L.pop(x)
        s+=a
    return s  
print(X(7))


# 2)

def Xk(n, k):
    total = 0
    sup=0
    for i in range(k):
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




# Correction de l'exercice 2:

# 1)

import random

def transition_etat(etat):
    if etat == 0:
        prob_0 = 0.3
        prob_1 = 0.4
        prob_2 = 0.3 # Les valeurs prob_2 ne sont jamais utilisées pour le random, car on passe à l'état 2 si on ne passe ni à l'état 0 ni à l'état 1 (prob_2=1-prob_0-prob_1). On peut supprimer ces lignes.
    elif etat == 1:
        prob_0 = 0.2
        prob_1 = 0.5
        prob_2 = 0.3 # Pareil ici
    else:
        prob_0 = 0.6
        prob_1 = 0.3
        prob_2 = 0.1 # Pareil ici
    
    tirage = random.random()
    if tirage < prob_0:
        return 0
    elif tirage < prob_0 + prob_1:
        return 1
    else:
        return 2
    
print(transition_etat(1)) 


# 2)

def simulation_markov(k):
    etat_courant = 0 # Cas initial
    etats = [etat_courant]
    for i in range(k):
        etat_courant = transition_etat(etat_courant) # On remplace l'état courant par le nouvel état après la transition
        etats.append(etat_courant)
    return etats

print(simulation_markov(20))


# 3)

def pourcentages_etats(etats):
    comptage_0 = etats.count(0)
    comptage_1 = etats.count(1)
    comptage_2 = etats.count(2)

    pourcentage_0 = (comptage_0 / len(etats)) * 100
    pourcentage_1 = (comptage_1 / len(etats)) * 100
    pourcentage_2 = (comptage_2 / len(etats)) * 100

    return pourcentage_0, pourcentage_1, pourcentage_2

print(pourcentages_etats(simulation_markov(20)))