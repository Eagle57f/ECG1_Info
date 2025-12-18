# Ex 8 2025
import math
n=1
S=0
while 1/((math.e-1)*math.exp(n))>10**-4:
    S+=1/((n**3)*math.exp(n))
    n+=1
S+=1/((n**3)*math.exp(n))
print(S, n)


# OU

n=1
S=0

for i in range(1, math.floor(-math.log(math.e-1)*0.0001)):
    S+=1/(n**3*math.exp(n))
    
    

