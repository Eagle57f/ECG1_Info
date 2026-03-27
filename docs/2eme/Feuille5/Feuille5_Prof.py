
#FEUILLE 5

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


ax=Axes3D(plt.figure())

def f(x,y):
    return x*y
#subdivision de [-1,1]x[-1,1]
x=np.linspace(-1,1,40)
y=x
#maillage du domaine [-1,1]x[-1,1]
X,Y=np.meshgrid(x,y)
Z=f(X,Y)
ax.plot_surface(X,Y,Z,cmap='autumn')
plt.show()

def g(x,y):
    return x**2+y**2
def h(x,y):
    return x**2-y**2
def k(x,y):
    np.sin(x)*np.sin(y)
x=np.linspace(-5,5,40)
y=x
X,Y=np.meshgrid(x,y)
Z=h(X,Y)
ax.plot_surface(X,Y,Z,cmap='cool')
plt.title('fonction h')
plt.show()
contour=plt.contour(X,Y,Z,10)
plt.show()
    