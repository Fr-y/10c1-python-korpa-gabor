from random import *
from math import *


def feladat31():
    for i in range(10, 101):
        if i % 7 == 3:
            print(i, end=" ")


# -- 32 --
def feladat32():
    lista = []

# -- 33 --
def feladat33():
    lista = []
    lista.append("alma")
    lista.append("korte")
    lista.append("banan")
    lista.append("szilva")
    lista.append("eper")
    print("A lista elemeinek száma:", len(lista))

    for item in lista:
        print(item, end=" ")

    print()

def feladat34():
    karakterlista = []
    karakterlista.append("1")
    karakterlista.append("b")
    karakterlista.append("@")
    karakterlista.append("d")
    karakterlista.append("$")
    for item in karakterlista:
        print(item, end=" ")

    print()

def feladat36():
    egeszlista = [123,21534,2315,56723,234]
    egeszlista.append(2321)
    egeszlista.append(randint(0, 100))
    egeszlista.append(int(input("Kérek egy szamot: ")))
    for i in range(5):
        egeszlista.append(randint(0, 100))
    for item in egeszlista:
        print(item, end=" ")

    print()


def feladat40():
    veletlenek = []
    for i in range(15):
        veletlenek.append(randint(10, 51))
    for item in veletlenek:
        print(item, end=" ")

    print()

    print("Legnagyobb szám:", max(veletlenek))
    print("Legkisebb szám:", min(veletlenek))
    print("Számok osszege:", sum(veletlenek))
    print("Számok átlaga:", sum(veletlenek) / len(veletlenek))
    print("Számok terjedelme:", max(veletlenek) - min(veletlenek))

    print()

    parosok = []
    for item in veletlenek:
        if item % 2 == 0:
            parosok.append(item)

    for szam in parosok:
        print(szam, end=" ")

    print()

    print("Párosok darabszáma:", len(parosok))
    print("Párosok összege:", sum(parosok))
    print("Párosok átlaga:", sum(parosok) / len(parosok))
    print("Párosok terjedelme:", max(parosok) - min(parosok))
    print("Legnagyobb páros szám:", max(parosok))


def feladat41():
    f = open("10szam.txt", "x")
    for x in range(10):
        f.write(f'{x}')
        f.write('\n')
    f.close()


def feladat42():
    f = open("10szam2.txt", "x")
    for x in range(10):
        f.write(f'{x} ')
    f.close()

def feladat43():
    f = open("43asfeladat.txt", "x")
    for i in range(3):
        for i in range(5):
            f.write(f'{randint(0,100)} ')
        f.write('\n')
    f.close()

def feladat44():
    f = open("10szam.txt", "r")
    lista = f.read().splitlines()
    f.close()
    print(lista)

def feladat45():
    f = open("10szam2.txt", "r")
    lista = [f.read()]
    f.close()
    print(lista)

def feladat46():
    f = open("43asfeladat.txt", "r")
    lista = f.read().splitlines()
    f.close()
    print(lista)



# -- hivások --
# feladat31()
# feladat32()
# feladat33()
# feladat34()
# feladat36()
# feladat40()
feladat41()
feladat42()
feladat43()
feladat44()
feladat45()
feladat46()