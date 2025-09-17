# Ex 1
"""L = [ -1, 2 , 8 , 7 , -3 , -3 , 7 , 9 , 2 , -1 , -1 , 6, 0 , 7 , 10]
print(L.count(0)) # Renvoie le nombre d’occurrences de la valeur.
print(L.index(2)) # Renvoie le premier indice de la valeur.
print(L.pop(7)) # Supprime de la liste et renvoye l'élément à l'index choisi (dernier par défaut).
print(L)
L.insert(3,"4") # insert(i,o) : Insére un objet o avant l'index i.
print(L)
L.reverse()
print(L) # Inverse la liste
L.remove(8) # Supprime la première occurence de la valeur dans la liste
print(L)
L = [ -1, 2 , 8 , 7 , -3 , -3 , 7 , 9 , 2 , -1 , -1 , 6, 0 , 7 , 10]
L.sort() # Trie la liste par ordre croissant et renvoye None. Le tri est sur place (c'est-à-dire que la liste elle-même est modifiée) et stable (c'est-à-dire que l'ordre de deux éléments égaux est conservé).  Si une fonction clé est donnée, applique-la une fois à chaque élément de la liste et les trie, par ordre croissant ou décroissant, en fonction de leurs valeurs de fonction. L'indicateur inverse peut être configuré pour trier par ordre décroissant.
print(L)"""

# Ex 2
"""L =["Bonjour","comment","vas","tu","aujourd'hui","?"]
print(L[1:5:2]) # Slicing : object Slice(debut inclu (0 par defaut), fin exclue (len(l) par défaut), pas (1 par défaut))"""

# Ex 3
"""L=[ -1 , 5 , 8 , -9 , 12 , 7 , 3 , 5 , 12 ]
print(sum(L)) # Renvoie la somme de tout les termes de la liste
print(min(L)) # Renvoie la valeur minimale parmis tout les termes de la liste
print(max(L)) # Renvoie la valeur maximale parmis tout les termes de la liste"""

# Ex 4
"""printemps=[ "mars", "avril", "mai"]
ete=["juin","juillet", "aout"]
automne=["septembre", "octobre", "novembre"]
hiver=["decembre", "janvier", "fevrier"]

saison=[printemps, ete, automne, hiver]

print(saison[3]) # Renvoie la liste hiver
print(saison[2][1]) # Renvoie octobre
print(saison[0 :3]) # Renvoie les listes printemps, été et automne
print(saison[ 1 ][0 : 2 ]) # Renvoie juin et juillet"""

# Ex 5
"""L=[2,3,1,7,9,5]
for k in range(len(L)):
    if k not in L:
        print("Le nombre",k," n'est pas dans la liste L")
# Ce programme renvoie le premier entier inf ou égal a la longueur de la liste L qui n'est pas dans L. Ne renvoie rien si tout les entiers inf ou egal a la longueur de L sont dans L."""

# Ex 6
"""abscisse=[0,1,2,3,4,5,6,7]
ordonnee=[3*x+5 for x in abscisse]
print(ordonnee) # Renvoie une liste contenant les valeurs de f(k) avec k parcourant les valeurs de la suite abscisse.

X=[i for i in range(21)]
Y=[x**2-2*x+1 for x in X]"""

# Ex 7
"""L1=[2]
L2=[i for i in range(21)]
L3=[i for i in range(0,101,3)]
L4=[i**2 for i in range(1,31)]
L5=[i+1 for i in range(5,128,2)]
import numpy.random as rd
L6=[rd.randint(1,11) for i in range(10)]
print(len(L1), len(L2), len(L3), len(L4), len(L5), len(L6))"""

# Ex 8
L=[1,2,5,7,7,8,7,9,4,5,2,4,6,8,7,3,1]
for i in L:
    while L.count(i)>1:
        L.remove(i)
print(L)

print([i for i in L if i>6])

print([i for i in L if i%2==0])

max=L[0]
for i in L:
    if i>max:
        max=i
print(max)

min=L[0]
for i in L:
    if i<max:
        min=i
print(min)

n=0
for _ in L:
    n+=1
print(n)