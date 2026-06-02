import numpy as np
def simul():
    M=np.random.randint(0,2)
    X=np.random.random(2)
    if M==0:
        XX=max(X)
        R=1
    else:
        XX=min(X)
        R=0
    XA=np.random.normal(0,1)
    if XA>=XX:
        return "Max", R==1
    else:
        return "Min", R==0
    
print(simul())



np.mean