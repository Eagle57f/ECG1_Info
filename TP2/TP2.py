# Ex 1
# input sert à demander une valeur à l'utilisateur pendant l'exécution du programme.

# Ex 2
# Le script 1 ne fonctionne pas car type(input(""))==Str
# Le script 2 fonctionne car eval permet de transformer ici un chiffre en Str en Float

# Ex 3
"""l=[eval(input("Note 1 et coeff: ")), eval(input("Note 2 et coeff: ")), eval(input("Note 3 et coeff: "))]
print(sum([i[0]*i[1] for i in l])/sum([i[1] for i in l]))"""

# Ex 4
"""from math import pi
r=float(input("Rayon de la sphère: "))
print(f"Aire: {4*pi*(r**2)}, Volume: {(4/3)*pi*(r**3)}")"""

# Ex 5
"""p=[float(input("Prix: ")), float(input("Pourcentage: "))]
print(p[0]*(1-p[1]/10020))"""

# Ex 6
"""AB=[eval(input("Coos de A")),
    eval(input("Coos de B"))]

Vdir=((AB[1][0])-(AB[0][0]), (AB[1][1])-(AB[0][1]))

c=-((AB[1][0])*(-Vdir[1])+(AB[1][1])*Vdir[0])
print(f"{-Vdir[1]}*x+{Vdir[0]}*y+{c}=0")"""



# Ex 7
# Le script 1 fonctionne, mais pas le 2 car il manque une tabulation avant print, la boucle est donc vide

# Ex 8
# d=16, d=12, d=9, d=5
# En enlevant la tabulation, on sort une instruction de la boucle, qui ne sera donc exécuté qu'une seule fois après  fin de boucle

# Ex 9
# range(borne de départ inclue, borne d'arrivée exclue, pas)
# renvoie un objet range que l'on peut parcourir et qui, transformé en liste, donne une liste de chiffres allant de Binf à Bsup exclue avec un pas donné (1 par defaut)
"""print(list(range(1,20,2)))"""

# Ex 10
# Le script 1 print qu'une seule fois à la fin du programme, alors que le script 2 print à chaque itération de la boucle

# Ex 11
"""for i in range(21):
    print(i**2)"""

# Ex 12
# a) Car il faut sommer pour tout k allant de 1 à n. Or la borne sup est exlue en python, donc il faut aller jusqu'à n+1
# b) L'erreur est le manque de tabulation avant S=S+1/k**2

# Ex 13 
"""def f(n):
    s=0
    for i in range(1,n+1):
        s+=1/i**3
    return s
print(f(100000))"""

'''def f(n):
    s=0
    for i in range(1,n+1):
        s+=1/i**4
    return s
print(f(100000))'''

"""def f(n):
    s=0
    for i in range(n+1):
        s+=(1/2)**i
    return s
print(f(1000))"""

"""def f(n):
    s=0
    for i in range(1,n+1):
        s+=(1/i*(i+1))
    return s
print(f(1000))"""

# Ex 14
"""def f(n:int):
    \"""n>=1\"""
    p=1
    for i in range(1,n+1):
        p*=(1+1/i)
    return p
print(f(10))"""

"""def f(n:int):
    p=1
    for i in range(1,n+1):
        p*=(i/(1+i))
    return p
print(f(10))"""

"""def f(n:int):
    p=1
    for i in range(2,n+1):
        p*=(1-(1/(i**2)))
    return p
print(f(10))"""

"""def f(n:int):
    p=1
    for i in range(1,n+1):
        p*=i
    return p
print(f(10))"""

# Ex 15
"""def f1(n):
    s=0
    for i in range(n+1):
        s+=2*i+1
    return s
print(f1(11))

def bonus1(n):
    s=0
    i=0
    while 2*i+1<=2*n+1:
        s+=2*i+1
        i+=1
    return s
print(bonus1(11))

def f1(n):
    s=0
    for i in range(2*n+2):
        if not i%2:
            s+=i+1
    return s
print(f1(11))

def f1(n):
    s=0
    for i in range(0, 2*n+2, 2):
        s+=i+1
    return s
print(f1(11))"""

"""def f1(n):
    s=0
    for i in range(n+1):
        s+=2*i
    return s
print(f1(11))

def bonus1(n):
    s=0
    i=0
    while 2*i<=2*n:
        s+=2*i
        i+=1
    return s
print(bonus1(11))

def f1(n):
    s=0
    for i in range(2*n+1):
        if i%2:
            s+=i+1
    return s
print(f1(11))

def f1(n):
    s=0
    for i in range(0, 2*n+2, 2):
        s+=i
    return s
print(f1(11))"""

# Ex 16
'''def f(n):
    s=0
    for i in range(1,n+1):
        s+=(1/i**2)
    return s
print(f(1000))

def f(n):
    s=0
    for i in range(1,n+1):
        s+=(1/(2*i)**2)
    return s
print(f(1000))

def f(n):
    s=0
    for i in range(1,n+1):
        s+=(1/(2*i-1)**2)
    return s
print(f(1000))'''

# Ex 17
"""from math import sqrt
def f(n):
    s=0
    for i in range(1,n+1):
        s+=(1/sqrt(i))
    return s
print(f(10))"""

#Ex 18
"""u=1
x=eval(input("Valeur de x: "))
while u>x:
    u=(u**2)/(u**2+1)
    print(u)"""
# Renvoye la premiere valeur de la suite u(n) a partir de laquelle u<=x

# Ex 19
"""from math import log
x=eval(input("Valeur de x: "))
n=1
while log(n)<x:
    n+=1
print(n)"""

# Ex 20

"""from math import exp
def f(n):
    for i in range(n,n+11):
        print((exp(i)-i)/(exp(i)+2*i))
f(0)
                  
def f(n):
    i=n
    while i<n+11:
        print((exp(i)-i)/(exp(i)+2*i))
        i+=1
f(100) #Limit = 1"""


# Ex 21

"""from math import log
def f(a):
    u=0
    for i in range(1,a+1):
        u+=(1/i)
    v=u
    u-=log(a)
    v-=log(a+1)
    print((u+v)/2)
    
f(100)"""


# Ex 23
"""def f(a):
    k=1
    s=0
    while k<a:
        s+=(1/k**3)
        k+=1
    print(s)
    
f(1000)

def f(a):
    k=1
    s=0
    while k<a:
        s+=(1/k**4)
        k+=1
    print(s)
f(1000)

def f(a):
    k=1
    s=0
    while k<a:
        s+=(0.5**k)
        k+=1
    print(s)
f(1000)

def f(a):
    k=1
    s=0
    while k<a:
        s+=(1/(k*(k+1)))
        k+=1
    print(s)
f(1000)"""

# Ex 24

"""def f(a):
    s=0
    i=1
    while s<a:
        s+=i
        i+=1
    print(s)
f(11)"""

# Ex 25 
"""from math import factorial
def f(a):
    if a==0:
        print(1)
    elif a<0:
        print("Existe pas")
    else:
        p=1
        for i in range(2,a+1):
            p*=i
        print(p)
f(-1)

def f(a):
    print(factorial(a) if a>=0 else "Existe pas")
f(-1)"""

# Ex 26
"""def f(a:float|int):
    print(a if a>=0 else -a)
    
f(-5)
f(5)
f(0)
"""
# Ex 27
"""def f(a,b):
    print(max(a,b))
f(2,-5)
    
def f(a,b):
    print(a if a>=b else b)
f(2,-5)"""

# Ex 28
"""import fractions
def f(a,b):
    print(fractions.Fraction(-b,a) if a!=0 else "x inexistant")
f(3,26)
f(0,5)"""

# Ex 30