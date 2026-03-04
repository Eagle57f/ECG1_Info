# Exercice 1

# a)

import numpy as np
from matplotlib import pyplot as plt

ax = plt.axes(projection='3d')
n=35
def f(x,y):
    return x*y

# b)

x=np.linspace(-1,1,n)
y=np.linspace(-1,1,n)
X, Y = np.meshgrid(x,y)
# ax.plot_surface(X, Y, f(X, Y), cmap='viridis')
# plt.show()


# Exercice 2

def exo2(t, x, y):
    return x**2+y**2 if t=="a" else x**2-y**2 if t=="b" else np.sin(x)*np.cos(y)

x=np.linspace(-5, 5,n)
y=np.linspace(-5, 5,n)
X, Y = np.meshgrid(x,y)
ax.plot_surface(X, Y, exo2("c", X, Y), cmap='viridis')
plt.show()

