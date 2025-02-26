import numpy as np
import numpy.linalg as al
matrice22=np.array([[1, 2], [3, 4]])
print(al.det(matrice22)) # Renvoie -2.0000000000000004
                         # (Python à des problèmes au niveau de l'arrondi lors des opérations)