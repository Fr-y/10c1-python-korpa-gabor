from math import *
from random import *

#1
szoveg = "alma"
#2
egesz = 12
#3
valos = 5.6
'''
#4
szo = input("Adj meg egy szót: ")
#5
mondat = input("Adj meg egy mondatot: ")
#6
karakter = input("Adj meg egy karaktert: ")
#7
egeszszam = int(input("Adj meg egy egész számot: "))
#15
egeszszam2 = int(input("Adj meg egy egész számot: "))
#8
valosszam  = float(input("Adj meg egy valós számot: "))'''
szo = "bicikli"
mondat = "Ez egy nagyon hosasdszú mondat sok szóval"
karakter = "a"
egeszszam = 324
egeszszam2 = 32525
valosszam = 32.432


#10
print(valosszam * 2)
print(valosszam * pi)
print(valosszam ** 3)
print(pow(valosszam, 3))
print(sqrt(valosszam))
print(valosszam**(1/2))
print(round(sqrt(valosszam), 3))
#11
veletlen = randint(10,50)
#12
if egeszszam % 2 == 0:
    print("páros")
else:
    print("páratlan")

#13
if egeszszam > 0:
    print("pozitiv")
elif egeszszam < 0:
    print("negativ")
else:
    print("a szam 0")

#14
if egeszszam > 30:
    print(egeszszam, "nagyobb mint 30")

#15
print(max(egeszszam, egeszszam2)," a nagyobb szám")

#16
print(min(egeszszam, egeszszam2)," a kisebb szám")


#17
print(len(szo), "karakterből áll a", szo, "szó")

#18

e = 0
for char in szo:
    if char == 'e':
        e += 1
print(e,'e betü van benne')

#19
maganhangzok = "aáeéoóöőüűuúií"
mhangzokszama = 0
for char in szo:
    if char.lower() in maganhangzok:
        mhangzokszama += 1
print(mhangzokszama, 'maganhangzó van a szóban')

#20
print(len(mondat), "karakterből áll a mondat")
#21
n = 0
for char in mondat:
    if char == ' ':
        n += 1
print(n,'szóköz van benne')

#22
eszam = 0
for char in mondat:
    if char == 'e':
        eszam += 1
print(eszam,'e betü van benne')

#23
szavak = mondat.split()
print(len(szavak),' szóbol áll')

#24
for szo in szavak:
    print(len(szo), end=" ")

print()

#25
leghosszabb = 0
for szo in szavak:
    if len(szo) > leghosszabb:
        leghosszabb = len(szo)
print(leghosszabb)

#26
# ---||---

#27
for i in range(10):
    print(i, end=" ")
print()

#28
for i in range(1, 11):
    print(i*2, end=" ")
print()


    