# Ex 1
'''print(f"""
125*347={125*347}
4x3,52+(2,5-7,5)^3={4*3.52+(2.5-7.5)**3}
(3,25+7,8)/(1,26-0,57)={(3.25+7.8)/(1.26-0.57)}
6x((10,68-2,2786)**4)/(5**2)={6*((10.68-2.2786)**4)/(5**2)}
""")

print(f"""
a=125, b=11 : {divmod(125,11)} OU a=125, b=11 : {(125//11,125%11)}
a=689, b=17 : {divmod(689,17)} OU a=689, b=17 : {(689//17,689%17)}
a=-145, b=21 : {divmod(-145,21)} OU a=-145, b=21 : {(-145//21,-145%21)}
a=-368, b=-6 : {divmod(-368,-6)} OU a=-368, b=-6 : {(-368//-6,-368%-6)}
""")'''

# Ex 2
# a) Erreur, b) 1, c) 1, d) 0

#Ex 3
"""
# a)
a=5
b=2
a,b=b,a
print(a,b)

# b) x=x+5 revient à incrémenter x de 5"""

# Ex 4
"""# a)
a,b,c,d,e=0,2,4,6,8 # a=0, b=2, c=4, d=6 e=8
a,b,c,d,e=a,d,c,b,a # a=a=0, b=d=6, c=c=4, d=b=2, e=a=0
print(a,b,c,d,e)

# b)
a,b,c=2,3,-5
b=2
c=3*a
print(a,b,c)"""

# Ex 5
"""# Pour les nombres négatifs, int enlève la partie décimale (donc au supérieur près pour les négatifs)
# alors que floor arrondit à l'inférieur près (pour les positifs et négatifs).

from fractions import *
a=Fraction(3,5)
print(a) # Print la fraction simplifiée au maximum
p=a.numerator
print(p) # Print le numérateur
q=a.denominator
print(q) # Print le dénominateur 

from fractions import Fraction
print((1+Fraction(3,4))/(Fraction(5,2)+Fraction(7,3)))
# OU
print(Fraction((1+Fraction(3,4)),(Fraction(5,2)+Fraction(7,3))))

print((Fraction(19,15)-Fraction(3,7))/(Fraction(11,2)+Fraction(8,35)))
# OU
print(Fraction((Fraction(19,15)-Fraction(3,7)),(Fraction(11,2)+Fraction(8,35))))"""

# Ex 6
"""from math import *
a=sqrt(2) # Racine carré de 2
b=sqrt(3) # Racine carré de 3
c=5
print(a**2==2) # False car il y a une erreur d'arrondi
print((sqrt(3))**2==3) # False car il y a une erreur d'arrondi
print(a**2+b==c) # True car les erreurs d'arrondi se compensent
print(a> 1.732) # False car inférieur"""