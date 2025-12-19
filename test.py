import random, numpy
def N():
    b=1
    while random.random()>b/(b+1):
        b+=1
    return b+1

def X():
    return random.random()

def T():
    return max(numpy.random.random(N()))
print(T())


def EML(m):
    E=numpy.zeros(3)
    for k in range(3):
        echantillon = []
        for i in range(m):
            echantillon.append(T())
        E[k] = numpy.mean(echantillon)
    return E

def jeu(p):
    i, v = 1, 1
    s, j = 1, 1
    a=1
    while random.random() > p:
        i = i+1
        if v == 1:
            a = a+1
        j = j+1
        if j > s:      # changement de main
            v=-v
            s = s+2
            j = 1
    if v == 1:
        vainqueur = 'A vainqueur'
    else:
        vainqueur = 'B vainqueur'
    return vainqueur, a

def EA(p, n):
    a=0
    for i in range(n):
        a+=1 if jeu(p)[0]=='A vainqueur' else 0
    return a/n
print(EA(0.6,10000))




def s(n):
    u, v= 0,1
    for k in range(2, n+1):
        u, v = v, u+v
    return v


L=[]
random.sample()