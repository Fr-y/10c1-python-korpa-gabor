print("3. feladat: Mondat")
mondat = input("kérek egy mondatot: ")
karakter = input("Kérek egy karaktert: ")

print(f"5. feladat: \n\tA mondat {mondat.count(karakter)} helyen tartalmaz e karaktert.")
leghoszabb = ''
for szo in mondat.split(' '):
    if len(szo) > len(leghoszabb):
        leghoszabb = szo
print(f"7. feladat: \n\tA leghosszabb szó: {leghoszabb}")