n=2 # Mettre n=int(input("Entrez un nombre entier : ")) pour demander à l'utilisateur

def a(n):
    if n==0:
        return 0
    return 2*a(n-1) + b(n-1)

def b(n):
    if n==0:
        return 1
    return 2*a(n-1) + 3*b(n-1)

print(a(n), b(n))


"""def note(LQ,LR):
    n=0
    for i in range(len(LQ)):
        if LR[i]==LQ[i]:
            n+=1
    return n


def reussite(LQ,LR):
    return "Réussite" if note(LQ,LR)>=10 else "Echec"


def notebonus(LQ,LR):
    n=0
    for i in range(len(LQ)):
        if LR[i]==LQ[i]:
            n+=1
            if n==4:
                if note(LQ,LR) + 2 <= 20:
                    return note(LQ,LR) + 2
                else:
                    return 20
        else:
            n=0
    return note(LQ,LR)
        
print(notebonus([1,3,2,4,3,2,1,3,2,4,4,4,3,2,2,1,2,3,4,3],
                [1,3,2,4,2,2,1,2,2,4,2,4,3,3,2,1,3,3,4,3]))




from random import *

x=random()
if x<1/3:
    piece="PILE"
else:
    piece="FACE"
print("Le résultat du lancer de la pièce est :", piece)


def simulX():
    i=0
    for _ in range(3):
        x=random()
        if x<1/3:
            i+=1
    return i
print(simulX())


def simul2X():
    for i in range(1, 5):
        if random() < 1/3:
            return i
    return 4
print(simul2X())

def simultipleX(n):
    return sum([simul2X() for _ in range(n)])/n
print(simultipleX(10))


"""