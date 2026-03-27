import numpy as np
import numpy.random as rd

#feuille 6

#ex 1



def norcentreereduite():
    u=rd.random(12)   #une matrice ligne à 12 composantes
    x=np.sum(u)-6
    return x
    
def norcentreereduite1():
    s=0
    for k in range (12):
        s+=rd.random()
    x=s-6
    return x
    
    
def normale(m,s):
    x=norcentreereduite()
    y=s*x+m
    return y

def normaleN(m,s,N):
    X=np.zeros(N)
    for k in range(N):
        X[k]=normale(m,s)
        return X
        
#ex 2

def exponentielle(lambd):
    u=rd.random()
    x=-(1/lambd)*np.log(1-u) #suit la loi exp d apres le theoreme
    return
    
def exponentielleN(lambd,N):
    X=np.zeros(N)
    for k in range (N):
        X[k]=exponentielle(lambd)
        return X
        
def gamma(n):
    X=exponentielleN(1,n)
    y=sum(X)
    return y
    
def gamma1(n):
    X=exponentielleN(1,n)
    y=0
    for k in range(n):
        y=y+X[k]
    return y
    
def gammaN(n,N):
    X=np.zeros(N)
    for k in range(N):
        X[k]=gamma(n)
    return X
    
#ex 2
def cauchy():
    U=rd.random()
    x=np.arctan(np.pi*U-np.pi/2)
    return x
    
def cauchyN(N):
    C=np.zeros(N)
    for k in range (N):
        C[k]=cauchy()
        return C
        
        
#ex 4
def simule_pareto(k,xmin):
    X=rd.random(k)
    Y=xmin/np.max(X)
    return Y
    
def simule_paretoN(k,xmin,N):
    P=np.zeros(N)
    for i in range(N):
        P[i]=simule_pareto(k,xmin)
        return P