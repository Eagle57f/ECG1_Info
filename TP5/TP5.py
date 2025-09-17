# Cours 12) Résolution d'un système d'équations :
"""import numpy as np
a = np.array([[2,3,3,1], [-4,-6,3,2], [-1,1,1,1], [-2,-1,1,1]])
b = np.array([15,3,5,1])
x = np.linalg.solve(a, b)
print(x) # Renvoie la valeur des 4 variables"""

# Exercices :
# Ex 1
"""import numpy as np
m = input("Enter une matrice")
print(np.array(eval(m)))"""

# Ex 2
"""import numpy as np
def symetrique(m:np.array):
    if np.shape(m) == np.shape(m.T):
        return True if (m==m.T).all() or (m==-m.T).all() else False
    return False
print(symetrique(np.array([[1,2,3],[4,5,6],[7,8,9]])))
print(symetrique(np.array([[1,2,3],[2,4,5],[3,5,6]])))
print(symetrique(np.array([[0,2,-1],[-2,0,4],[1,-4,0]])))"""

# Ex 3
"""import numpy as np
def mat1(n,p):
    return np.random.random((n,p))
print(mat1(3,5))

def mat6(n,p):
    return 6*np.random.random((n,p))+1 # On mutiplie par 6 car card([|1,6|])==6 et on ajoute 1 car on commence à 1.
print(mat6(3,5))

def matpair(n,p):
    return 2*np.random.randint(0,10000,(n,p))
print(matpair(3,5))"""

# Ex 4
"""import numpy as np
def diag(n):
    m = np.zeros((n, n), dtype=int)
    for i in range(n): # On commence par la diagonale centrale, puis on remplie les diagonales de chaque coté, puis encore de chaqque coté...
        np.fill_diagonal(m[i:], n - i) # Au dessus
        np.fill_diagonal(m[:, i:], n - i) # En dessous
    return m
print(diag(5))"""

# Ex 5
"""def diag2(n):
    m = np.zeros((n, n), dtype=int)
    np.fill_diagonal(m, n)
    np.fill_diagonal(np.fliplr(m), n)
    return m
print(diag2(5))"""

# Ex 6
# A faire après avoir fait le cours sur les matrices