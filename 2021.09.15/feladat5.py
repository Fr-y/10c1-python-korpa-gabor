"""Írj programot, ami beolvas két számot, majd kiírja:
a. az összegüket;
b. különbségüket;
c. szorzatukat;
d. hányadosukat, ha lehet!
e. mennyi maradékot kapunk, ha az első bekért számot osztjuk a másikkal!
"""


a = int(input("Adj meg egy számot: "))
b = int(input("Adj meg mégegy számot: "))
print("A számok összege: ", a + b)
# print(a, "+", b, '=',  a + b)
print("A számok szorzata: ", a * b)
print("A számok különbsége: ", a - b)
print("A számok hányadosa: ", a // b)
print("A számokkal elvégzett osztás maradéka: ", a % b)



