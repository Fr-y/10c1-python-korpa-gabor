from math import sqrt

print("1. feladat: Téglatest")
a = float(input('Add meg a háromszög a oldalát: '))
b = float(input('Add meg a háromszög b oldalát: '))
c = float(input('Add meg a háromszög c oldalát: '))

f = round(sqrt(pow(a,2) + pow(b,2) + pow(c,2)), 1)

print('A testátló hossza:', f)