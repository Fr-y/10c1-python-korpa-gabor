from math import *



def feladat1():
    szamok=[]
    a=int(input("Add meg a számok számát: "))
    for i in range(a):
        szamok.append(int(input("Kérek egy számot: ")))
   
    print(szamok)
    db=0
    for item in szamok:
        if item%2==1:
            db=db+1
    if db>0:
        print("A páratlanok száma:", db)
    else:
        print("Nincsenek páratlan számok.")



def feladat2():
    szamok=[]
    a=int(input("Add meg a számok számát: "))
    for i in range(a):
        szamok.append(int(input("Kérek egy számot: ")))
   
    print(szamok)
    db=0
    for item in szamok:
        if item%2==0:
            db=db+1
    if db>0:
        print("A páros száma:", db)
    else:
        print("Nincsenek páros számok.")



def feladat3():
    szamok=[]
    a=int(input("Add meg a számok számát: "))
    for i in range(a):
        szamok.append(int(input("Kérek egy számot: ")))
   
    print(szamok)
    for item in szamok:
        if item%2==0:
            print(f'{item}: {szamok.index(item)+1}. sorszámú')



def feladat4():
    szamok=[]
    a=int(input("Add meg a számok számát: "))
    for i in range(a):
        szamok.append(int(input("Kérek egy számot: ")))
    egesz = int(input("Adj meg egy egész számot: "))

    if egesz in szamok:
        print(f" {egesz} a {szamok.index(egesz)}. indexen található")
    else:
        print("Ez a szám nincs a megadott számok között")



def feladat5():
    szamok=[]
    a=int(input("Add meg a számok számát: "))
    for i in range(a):
        szamok.append(int(input("Kérek egy számot: ")))
    egesz = int(input("Adj meg egy egész számot: "))

    db = 0
    for item in szamok:
        if egesz == item:
            db += 1
    print(db)



def feladat6():
    nevek = []
    a=int(input("Add meg a nevek számát: "))
    for i in range(a):
        nevek.append(input("Kérek egy nevet: "))
    nev = input("Adj meg egy nevet: ")

    db = 0
    for item in nevek:
        if nev == item:
            db += 1
    print(f'{db} {nev} nevű ember jár az osztalyba')



def feladat7():
    szamok=[]
    a=int(input("Add meg a számok számát: "))
    for i in range(a):
        szamok.append(int(input("Kérek egy számot: ")))
    
    print(max(szamok) - min(szamok))


# -- main --

# feladat1()
# feladat2()
# feladat3()
# feladat4()
# feladat5()
# feladat6()
feladat7()