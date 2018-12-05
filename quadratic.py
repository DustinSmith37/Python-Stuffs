import math
#gathers info from user on variables

a = float(input("a = "))
print('Coeffecient a is', a)

b = float(input("b = "))
print('Coeffecient a is', b)

c = float(input("c = "))
print('Coeffecient a is', c)

#calculates the two possibilities

quad1 = (-(b) + ((b**2-4*a*c)**.5))/(2*a)

quad2 = (-(b) - ((b**2-4*a*c)**.5))/(2*a)

#prints answer

print("""
The possible solutions are""", quad1, quad2)
