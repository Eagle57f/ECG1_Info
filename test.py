"""n=eval(input("Donnez un nombre entier naturel: "))
S=0
for i in range(0,n+1):
    for j in range(0,n+1):
        S+=(2*i+j)**3
print(S)"""



"""n=eval(input("Donnez un nombre entier naturel: "))
P=1
if n>0:
    for i in range(2,n+1):
        P*=i
print(P)"""

"""from math import log
n=eval(input("Donnez un nombre entier naturel: "))
S=0
for i in range(1,n+1):
    S+=log(1+1/i)
print(S)

S=0
i=1
while i<=n:
    S+=log(1+1/i)
    i+=1
print(S)"""







"""from random import randint
n=randint(1,12)
if n<5:
    print(n**3)
elif n==8:
    print(n*3)
else:
    print(0)"""
    
    
"""n = eval(input("Donnez un nombre entier naturel: "))
nbin = ""
if n == 0:
    nbin = "0"
else:
    while n > 0:
        nbin += str(n % 2)
        n //= 2
print(nbin[::-1])"""


p=eval(input("Précision: "))
a=eval(input("Valeur de a: "))
b=eval(input("Valeur de b: "))
while abs(b-a)>p:
    m=(a+b)/2
    if (a**3+3*a-5)*(m**3+3*m-5)<0:
        b=m
    else:
        a=m
print([a,m,b])