from random import *


def prim(szam):
    osztok = 0
    for i in range(1, szam+1):
        if szam % i == 0:
            osztok += 1
    if osztok == 2:
        return True
    else:
        return False

def kiirprim():
    szam = int(input("Kérek egy pozitiv egész számot: "))
    f = open("primek"+str(szam)+"ig.txt", 'w')
    for i in range(1, szam+1):
        if prim(i):
            f.write(str(i) + "\n")
    f.close


# for i in range(256):
#         print(chr(i), end=" ")

def feladat12():
    f = open('karakterek.txt', 'w')
    for i in range(150):
        if randint(0,1) == 1:
            n = randint(65, 90)
        else:
            n =  randint(97, 122)
        f.write(f'{chr(n)}\n')
    f.close()



def feladat13():
    f = open('gyumolcsok.txt', 'w')
    for i in range(20):
        gyumolcs = input("Adj meg egy gyümölcsöt: ")
        f.write(gyumolcs + "\n")
    f.close()



def feladat14():
    f = open('veradas.txt', 'w')
    for i in range(150):
        if randint(0,4) == 0:
            f.write("A ")
        elif randint(0,4) == 1:
            f.write("B ")
        elif randint(0,4) == 2:
            f.write("AB ")
        elif randint(0,4) == 3:
            f.write("0 ")
    f.close()



# def feladat15():
#     f = open('forma1.txt', 'w')
#     for i in range(12):
#         szam = randint(6369985, 6455127)
#         f.write(str(TimeSpan.FromSeconds(szam/1000)))


def feladat16():
    f = open('sorozat.txt', 'w')
    for x in [18+x + 4 for x in range(10)]: f.write(f'{x} ')
    f.close()

def feladat17():





# -- main --
# kiirprim()
# feladat12()
# feladat13()
# feladat14()
feladat16()