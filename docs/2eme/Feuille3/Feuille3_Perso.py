# Exercice 1

# 1)
import random as rd
def X():
    return 1 if rd.random() < 0.2 else 0

# 2)
def S(n):
    L=(X() for _ in range(n))
    return sum(L)/n

print(S(10000))

# Exercice 2:

