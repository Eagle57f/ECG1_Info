from math import exp

def suite(n):
    u=1
    suite=[u]
    for k in range(1,n):
        u=1-exp(-u)
        suite.append(u)
    return suite

def somme(n):
    s=0
    for i in suite(n):
        s+=i
    return s
# n=int(input("Entrez un entier n: "))
# print(somme(n))

def exo2(n):
    Sn=sum([1/k**2 for k in range(1,n+1)])
    return Sn

def exo22(eps):
    n=1
    Sn=0
    while True:
        Sn+=1/n**2
        if 1/n**2<eps:
            break
        n+=1
    return Sn,n



import matplotlib.pyplot as plt
n=10
x=1
X=range(1,n+1)
Y=[i/x for i in X]
plt.plot(X,Y,label='y=x')
plt.legend()
plt.show()