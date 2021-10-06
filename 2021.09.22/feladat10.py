"""Írj programot, ami beolvassa a háromszög oldalainak hosszát, és megmondja, hogy ilyen 
oldalakkal szerkeszthető-e háromszög!"""

#háromszög akkor szerkezthető ha a kisebb két oldal összege nagyobb a harmadiknál


a = float(input("Add meg a háromszög a oldalának a hosszát: "))
b = float(input("Add meg a háromszög b oldalának a hosszát: "))
c = float(input("Add meg a háromszög c oldalának a hosszát: "))

ln = max(a,b,c)

if a == ln:
    if a < b + c:
        print("A háromszög szerkeszthető")
    else:
        print("Nem szerkeszthető")
elif b == ln:
    if b < a + c:
        print("A háromszög szerkeszthető")
    else:
        print("Nem szerkeszthető")
else: 
    if c < b + a:
        print("A háromszög szerkeszthető")
    else:
        print("Nem szerkeszthető")

#masik megoldas

if a == ln:
    if a < b + c:
        print("A háromszög szerkeszthető")
    else:
        print("Nem szerkeszthető")
if b == ln:
    if b < a + c:
        print("A háromszög szerkeszthető")
    else:
        print("Nem szerkeszthető")
if c == ln:
    if c < b + a:
        print("A háromszög szerkeszthető")
    else:
        print("Nem szerkeszthető")

#harmadik megoldas

szamok = [a,b,c]

print(szamok)
szamok.sort()
print(szamok)
if szamok[2] < szamok[0] + szamok[1]:
    print("Szerkeszthető")
else:
    print("Nem szerkeszthető")