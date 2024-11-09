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
