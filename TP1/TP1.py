# Ex 1
print(f"""
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
""")

# Ex 2
print("Erreur, 1, 1, 0")

#Ex 3
a=5
b=2
a,b=b,a
print(a,b)

# Voir sujet

# Ex 4
# Voir sujet

a,b,c=2,3,-5
b=2
c=3*a
print(a,b,c)

# Ex 5
# Voir sujet

from fractions import Fraction
print((1+Fraction(3,4))/(Fraction(5,2)+Fraction(7,3)))
# OU
print(Fraction((1+Fraction(3,4)),(Fraction(5,2)+Fraction(7,3))))

print((Fraction(19,15)-Fraction(3,7))/(Fraction(11,2)+Fraction(8,35)))
# OU
print(Fraction((Fraction(19,15)-Fraction(3,7)),(Fraction(11,2)+Fraction(8,35))))

# Ex 6
# Voir sujet