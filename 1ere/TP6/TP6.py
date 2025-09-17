# Ex 1
"""import matplotlib.pyplot as plt
abscisses = [0.5, 3.5 , 1, 2, 3, 0.5]
ordonnees = [2, 2, 0, 3, 0, 2]
plt.plot(abscisses, ordonnees)
plt.show()"""

"""import matplotlib.pyplot as plt
abscisses = [0.5, 1 , 3, 3.5, 2, 0.5]
ordonnees = [2, 0, 0, 2, 3, 2]
plt.plot(abscisses, ordonnees)
plt.show()"""

# Ex 2
"""from math import exp
import matplotlib.pyplot as plt
x=[i/10 for i in range(-50,21)]
y=[exp(i/10) for i in range(-50,21)]
plt.plot(x,y)
plt.show()"""

# Ex 3
"""import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-5,5,101)
y=[i**2-3*i+1 for i in x]
plt.plot(x,y)
plt.show()"""

# Ex 4
"""import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 3 * np.pi, 0.01)[1:]
print(x)
plt.plot(x, np.cos(x),label='$y=sin(x)/x$')
plt.legend()
plt.grid()
plt.show()
# Je n'ai pas obtenu d'erreur en exécutant le programme, mais pour éviter le problème de la fonction qui n'est pas définie en 0,
# il suffit de retirer la première valeur de la liste x (qui est 0), en ajoutant [1:] après np.arange(...)."""

# Ex 5
"""import numpy as np
import matplotlib.pyplot as plt
# x = np.linspace(-1,1,100)
# y = np.where(x == 0, np.nan, 1 / x) # ne marche que si 0 est inclu dans x, ce qui n'est pas le cas ici, on va donc diviser le linespace en deux.
# plt.plot(x, 1/x,label='$y=sin(x)/x$')

x1 = np.linspace(-1,-0.01,50)
x2 = np.linspace(0.01,1,50)
plt.plot(x1, 1/x1,label='$y=sin(x)/x$  (x < 0)')
plt.plot(x2, 1/x2,label='$y=sin(x)/x$  (x > 0)')
plt.legend()
plt.grid()
plt.show()"""

# 5 : Autres exemples
"""import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-2*np.pi, 2* np.pi, 0.01)
for i in range(1,4):
    texte="$y=cos("+str(i*2)+"x)$"
    plt.plot(x, np.cos(i*2*x),label =texte)
plt.legend()
plt.show()"""

# Ex 6
# 1)
"""import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-4*np.pi, 4* np.pi, 0.01)
texte="$y=cos(x)$"
plt.plot(x, np.cos(x),label =texte)
texte="$y=cos(x)$"
plt.plot(x, np.sin(x),label =texte)
plt.legend()
plt.show()"""

# 2)
"""import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 1.5, 0.01)
texte="$y=x$"
plt.plot(x, x,label =texte)
texte="$y=sqrt(x)$"
plt.plot(x, np.sqrt(x),label =texte)
texte="$y=x**2$"
plt.plot(x, x**2,label =texte)
texte="$y=x**3$"
plt.plot(x, x**3,label =texte)
plt.legend()
plt.show()
"""

# Ou alors :
"""import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 1.5, 0.01)
for f, t in [(x, "x"),(np.sqrt(x), "np.sqrt(x)"), (x**2, "x**2"), (x**3, "x**3")]:
    texte=f"$y={t}$"
    plt.plot(x, f,label =texte)
plt.legend()
plt.show()"""

# 3)
"""import matplotlib.pyplot as plt
import numpy as np
x1 = np.arange(-7, 3, 0.01)
x2 = np.arange(3, 7, 0.01)
plt.plot(x1, 3*(np.sqrt(1-(x1**2)/49)),label='$y=3*(np.sqrt(1-(x**2)/49))$  (x<3)')
plt.plot(x2, 3*(np.sqrt(1-(x2**2)/49)),label='$y=3*(np.sqrt(1-(x**2)/49))$  (x>3)')
plt.legend()
plt.grid()
plt.show()"""

# 4)
"""import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-1, 1, 0.01)
plt.plot(x, 9-8*abs(x),label='$y=9-8*abs(x)$')
plt.legend()
plt.grid()
plt.show()"""

# 5)
"""import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 3, 0.01)
plt.plot(x, 0.5*((np.sqrt(x)+np.sqrt(2))**2+(np.sqrt(x)-np.sqrt(2))**2),label='$y=0.5*((np.sqrt(x)+np.sqrt(2))**2+(np.sqrt(x)-np.sqrt(2))**2)$')
plt.legend()
plt.grid()
plt.show()
# Le fait que cette focntion est linéaire est prévisible car en développant les carrés et en les additionnant,
# on obtient 2x+4, puis en multipliant par 0.5, on obtient x+2."""

# 6)
"""import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 10, 0.01)
plt.plot(x, x*(np.floor(x) + 1),label='$y=sum(x,$ $0$ $to$ $abs(x))$  (0<=x>=10)')
plt.legend()
plt.grid()
plt.show()"""