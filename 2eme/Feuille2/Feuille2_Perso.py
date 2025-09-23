# En cours

# Exercice 1:



# Exercice 2:
"""n=10 # int(input("n ? "))
def L(k,X, x):
    p=1
    for j in range(len(X)):
        p*=(x-X[j])/(X[k]-X[j]) if j!=k else 1
    return p
print(L(3,[1,2,3,4,5,6,7,8,9,10,11],1.5))

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,100)
l=[-2, -1, 0, 1, 2]
for k in range(len(l)):
    y=[L(k, l, xi) for xi in x]
    plt.plot(x,y)
plt.grid()
plt.show()"""


# Exercice 3:

"""import numpy as np

def f(x): return x+np.log(x)

def df(x): return 1+1/x


def newton(f, df, a, eps):
    an=a
    anp=an-f(an)/df(an)
    i=1
    while abs(anp-an)>eps:
        an=anp
        anp=an-f(an)/df(an)
        i+=1
    return an, i

print(newton(f, df, 1, 10e-10))"""


# Exercice 4: 
"""p=[1, 0, -2, 1]  # x^3 - 2x + 1
def eval_poly(p, x0):
    r=p[0]
    for i in range(1, len(p)):
        r=r*x0+p[i]
    return r
print(eval_poly(p, 2))"""


# Exercice 5:



# Exercice 6:
"""import numpy as np

def f(x): return np.exp(x)*x**3
n=0
S=0
while 1/((np.e-1)*np.exp(n))>10e-4:
    n+=1
    S+=1/f(n)
print(n, S)"""


# Exercice 7: