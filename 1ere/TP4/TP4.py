# Ex 1
"""from math import log, sqrt
def f(l, a, mode):
    def fa(x): return x**2+2*x-1
    def fb(x): return log(x**2+1)
    def fc(x): return log(x+sqrt(1+x**2))
    i=l[0]
    output=[]
    while i<=l[1]:
        output.append(fa(i) if mode=="a" else fb(i) if mode=="b" else fc(i))
        i+=a
    return output
print(f([-2,3], 0.5, "a")) # Marche aussi sans renvoyer de liste, grande à la fonction join (voir Ex 3)
print(f([-3,3], 0.25, "b"))
print(f([-4,4], 0.5, "c"))"""

# Ex 2
"""def f(x): return x*3
def g(x): return x**3"""

# Ex 3
"""def f(): return " ".join([str(i*7) for i in range(1,11)])
print(f())"""

# Ex 4
"""def tjk(j,k):
    def tn(n): return " ".join([str(n*i) for i in range(1,11)])
    return "\n".join(([str(tn(i)) for i in range(j,k+1)]))
print(tjk(1,10))"""

# Ex 5
"""def test(x,y):
    somme = 0
    for i in range(y) :
        somme = somme + x
    return somme
print(test(10,5)) # Renvoie x*y"""

# Ex 6
"""def max3(a, b, c):
    return a if a > b and a > c else b if b > a and b > c else c
print(max3(1,5,-2))"""

"""def max3(a, b, c):
    l=[a, b, c]
    l.sort(reverse=True)
    return l[0]
print(max3(1,5,-2))"""

#Ex 7
"""from math import log
def a(n):
    p=1
    for i in range(2,n+1):
        p*=log(1-1/(i**2))
    return p
print(a(10))

def ba(n):
    s=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            s+=min(i,j)
    return s
print(ba(10))

def bb(n):
    s=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            s+=max(i,j)
    return s
print(bb(10))

def bc(n):
    s=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            s+=abs(i-j)
    return s
print(bc(10))"""

# Ex 8
"""def f(l, n):
    return n in l
print(f([1,2,56,4,6,2,5,6,5,6,8,99,5,5,2,22,7], 7))"""

# Ex 9
"""def nfibo(n):
    l=[1,1]
    for i in range(n):
        l.append(l[i]+l[i+1])
    return l[n]
print(nfibo(10))

def fibo(n):
    l=[1,1]
    for i in range(n):
        l.append(l[i]+l[i+1])
    return l
print(fibo(10))"""

# Ex 10
# a)
"""from math import factorial
print(factorial(8)/(factorial(8-5)*factorial(5)))

def coef_bino(n,p):
    return factorial(n)/(factorial(p)*factorial(n-p))
print(coef_bino(8,5))

from math import prod
def coef_bino(n,p):
    def facto(k):
        return prod([i for i in range(1,k+1)])
    return facto(n)/(facto(p)*facto(n-p))
print(coef_bino(8,5))

def coef_bino(n,p):
    def facto(k):
        p=1
        for i in range(1,k+1):
            p*=i
        return p
    return facto(n)/(facto(p)*facto(n-p))
print(coef_bino(8,5))
"""
# b)
"""def bino(n, k, i=1, r=1):
    if i<=k:
        return bino(n,k,i+1,r*((n-k+i)/i))
    return r
print(bino(8,5))"""

# c)
# 1) On cherche la valeur a la n ieme ligne et k ieme rangée du triangle de pascal, on va donc recréer ce triangle
"""n=8
k=5
triangle=[[1]]
for i in range(1, n+1):
    rangee=[1] # Chaque rangee commence par 1
    for j in range(1, i):
        rangee.append(triangle[i-1][j-1]+triangle[i-1][j])
    rangee.append(1) # Chaque rangee termine par 1
    triangle.append(rangee)
print(triangle[n][k])"""

# 2)
"""def bino(n, k):
    if k == 0 or k == n:
        return 1
    return bino(n - 1, k - 1) + bino(n - 1, k)
print(bino(8,5))"""

# Ex 11
"""from math import sqrt
def f(a:int|float,b:int|float,c:int|float,u0:int|float,u1:int|float,n:int=None, *, value:bool=True) -> str:
    '''
    Return the value of u_n if value=True, otherwise return the general expression of u_n.
    The n parameter can be omitted if value=False.
    
        Parameters:
            a (int|float): Value of a in ax^2+bx+c=0
            b (int|float): Value of b in ax^2+bx+c=0
            c (int|float): Value of c in ax^2+bx+c=0
            u0 (int|float): Value of u_0
            u1 (int|float): Value of u_1
            n (int): Number of iterations
            value (bool): Set to True to return the value of u_n, False to return the general expression of u_n.

        Returns:
            un (str): Value of u_n if value=True, otherwise the general expression of u_n.
    '''
    delta=b**2-4*a*c
    if delta>0:
        x1=(-b+sqrt(delta))/(2*a)
        x2=(-b-sqrt(delta))/(2*a) 
        
        alpha=(u1-x2*u0)/(x1-x2)
        beta=u0-alpha
        
        un=alpha*x1**n+beta*x2**n
        return f"u_{n}={un}" if value==True else f"u_n={alpha}*{x1}^n*{beta}*{x2}^n"
        
    elif delta==0:
        x0=(-b)/(2*a) 

        alpha=(u1-x0*u0)/(x0)
        beta=u0
        
        un=(alpha*n+beta)*x0**n
        return f"u_{n}={un}" if value==True else f"u_n=({alpha}*n+{beta})*{x0}^n"
    else: return None
    
    
print(f(1,2,1,10,1,-2, value=True))
print(f(1,2,1,10,1,-2, value=False))"""

# Ex 12
"""from math import sin, log, sqrt, exp, cos

from math import pi, e
def fa(a,b,n,mode="sin",methode="rect"):
    def f(x): return sin(x) if mode=="sin" else log(x) if mode=="log" else exp(-x**2) if mode =="exp" else sqrt(1-x**2)
    Sinf=0
    if methode=="rect":
        for k in range(1,n+1):
            Sinf+=((b-a)*(f(a+((k-1)*(b-a))/n)+f(a+((k)*(b-a))/n)))/(2*n)
    else:
        for k in range(1,n+1):
            Sinf+=((b-a)/n)*f(a+(((k-1)*(b-a))/n))
    Ssup=0
    if methode=="rect":
        for k in range(1,n+1):
            Ssup+=((b-a)/n)*f(a+(((k)*(b-a))/n))
    

    def derivate_max(mode, interval, n):
        a, b = interval
        x = a
        max_abs_value = 0

        while x <= b:
            try:
                abs_value = abs(cos(x) if mode=="sin" else 1/x if mode=="log" else -2*x*exp(-x**2) if mode=="exp" else (-x)/(2*sqrt(1-x**2)))
                if abs_value > max_abs_value:
                    max_abs_value = abs_value
            except ZeroDivisionError:
                pass

            x += 1/n
            

        return max_abs_value
    
    if methode=="rect": 
        erreur = ((b-a)**2)/(2*n)*abs(derivate_max(mode, (a,b), n))
        return (Sinf, Ssup), erreur
    else:
        return Sinf

print(fa(0,pi/2,100000,"sin","rect"))
print(fa(1,e,100000,"log","rect"))
print(fa(0,1,100000,"exp","rect"))
print(fa(-1,0,100000,"sqrt","rect"))

print(fa(0,pi/2,100000,"sin","trap"))
print(fa(1,e,100000,"log","trap"))
print(fa(0,1,100000,"exp","trap"))
print(fa(-1,0,100000,"sqrt","trap"))"""

# Ex 13
"""def nb_chiffres(n):
    b = n
    m = 0
    while b >= 1:
        m = m + 1
        b = n // 10**m
    return m

n = eval(input("Entrer un entier naturel n: "))
print(nb_chiffres(n)) # Ce script renvoie le nombre de chiffre d'un nombre (Ex: 123993 est composé de 6 chiffres).
                      # Pour ce faire, le programme va compter le mobre de fois qu'on peut diviser ce nombre par 10 avant qu'il devienne inférieur à 1.
                      # Ce nombre de fois étant le nombre de chiffres composant le nombre (car on déplace la virgule de 1 vers la gauche à chaque fois).

def nb_chiffres_recursive(n):
    if n < 10:
        return 1 # Si n<10 (cas de base, arrête la recursion)
    else:
        return 1 + nb_chiffres_recursive(n // 10) # Les +1 s'additionnent seulement a la fin des appels recursifs. Ils restent en attente jusqu'a la fin de la recursion.

                                                  # Lorsque le cas de base est atteint, on commence à "remonter" dans la pile d'appels, en ajoutant le +1 de chaque appel précédent. Pour 1234 :
                                                  # Le quatrième appel (nb_chiffres_recursive(1)) retourne 1.
                                                  # Ce 1 retourne au troisième appel (nb_chiffres_recursive(12)), qui avait 1 + nb_chiffres_recursive(1). Donc, il devient 1 + 1 = 2.
                                                  # Ensuite, ce 2 retourne au deuxième appel (nb_chiffres_recursive(123)), qui devient 1 + 2 = 3.
                                                  # Enfin, ce 3 retourne au premier appel (nb_chiffres_recursive(1234)), qui devient 1 + 3 = 4.
print(nb_chiffres_recursive(n))"""

# Ex 14   => A revoir
"""def a(n):
    if n==0:
        return 1 # Valeur de u_0
    return (a(n-1)+1)/(a(n-1)+2)
print(a(10))

from math import sqrt
def b(n):
    if n==0:
        return 1
    return sqrt(b(n-1)+1)
def bbis(n): return b(n+1)
print(bbis(10)) # Demander si on a le droit d'utiliser une deuxième fonction.

def c(n):
    if n==0:
        return 1
    return c(n-1)**2-2
def cbis(n): return c(n+1)
print(cbis(10)) # De même que pour b)"""

# Ex 15
"""def u(a,n):
    if n==0:
        return 1
    return (1/2)/(u(a,n-1)+(a/u(a,n-1)))
def ubis(n): return u(n+1)
print(ubis(3,10))"""

# Ex 16
"""import random as rd
def f():
    return rd.choice(["Roger", "Monique"])
print(f())
def f():
    return ["Roger", "Monique"][rd.randint(0,1)]
print(f())

def g(n):
    l=[f() for i in range(n)]
    for i in range(n):
        print(i)
    cR = l.count("Roger")
    cM = l.count("Monique")
    print(f"Le plus tombé:", "Monique" if cM> cR else "Roger" if cR > cM else "Les deux sont tombés le même nombre de fois")
g(10)"""

# Ex 17
"""# a)
phrase = "Aujourd hui en info je fais un peu de python pour être au point le jour du concours et je m amuse beaucoup"
# b)
i=0
for k in phrase:
    i+=1
print(i) # On compte les espaces
print(len(phrase)) # On compte les espaces
# c)
print(phrase.count("e")+phrase.count("E"))
# d)
print(phrase.count("a")+phrase.count("A"))
# e)
def nombre(phrase, lettres:str, separated):
    '''letters or str, separated by |
    if separated=True, upper and lower case letters are distinguished
    else upper and lower case letters are not distinguished (use lower case letters)'''
    return sum([phrase.count(l) for l in lettres.split("|")]) if separated==True else sum([phrase.lower().count(l) for l in lettres.split("|")])
# f)
print(nombre(phrase, "a|A| |m", False))"""