from random import *


# Egy sornyi adat


def feladat16():
    # egy sorba:
    # f = open('sorozat.txt', 'w')
    # for x in [18+x + 4 for x in range(10)]: f.write(f'{x} ')
    # f.close()

    a = 22
    f = open('sorozat.txt', 'w')
    for i in range(10):
        f.write(str(a) + ' ')
        a += 4

    f.close()



def feladat17():
    f = open('dobokocka.txt', 'w')
    for i in range(50):
        f.write(str(randint(1,6)) + ' ')
        
    f.close



def feladat18():
    mondat = ""
    f = open('mondat.txt', 'w')
    while True:
        mondat += input()
        mondat += " "
        if mondat[-2] == '.':
            f.write(mondat)
            break

    f.close()



def feladat19():
    f = open('kicsik.txt', 'w')
    generaltak = []
    for i in range(10):
        gen = randint(1,50)
        if gen in generaltak:
            i -= 1
        else:
            generaltak.append(gen)
            f.write(str(gen) + ' ')

        

def feladat20():
    f = open('orszagok.txt', 'w')
    orszagok = []
    while "Magyarország" not in orszagok:
        orszag = input()
        orszagok.append(orszag)
        f.write(orszag + '*')


    f.close()
   


def feladat21():
    f = open('toto.txt', 'w')
    for i in range(14):
        tipp = randint(0,2)
        if tipp == 0:
            f.write("1, ")
        elif tipp == 1:
            f.write("2, ")
        else:
            f.write("x, ")

    f.close()



def feladat22():
    f = open('tengerszint.txt', 'w')
    for i in range(8):
        f.write(str(randint(100,146)) + ' ')
    f.close()



def feladat23():
    f = open('skanditipp.txt', 'w')
    for i in range(7):
        f.write(str(randint(1, 35)) + ' ')



def feladat24():
    f = open('tavol.txt', 'w')
    for i in range(6):
        r = randint(550,830)
        if r < 600:
            f.write("0 ")
        else:
            f.write(str(r) + ' ')

    f.close()



def feladat25():
    f = open('futas.txt', 'w')
    #800m
    for i in range(3):
        f.write(str(randint(165, 210)) + 's ')
    #60m
    for i in range(10):
        f.write(str(randint(9, 12)) + 's ')
    f.close



# Több sor, soronként több adat



def feladat26():
    f = open('fogyasztas.txt', 'w')
    for i in range(12):
        km = randint(480,540)
        l = randint(367, 398) / 100
        f.write(str(km) + ' '+ str(l) + ' \n')

    f.close()



def feladat27():
    f = open('vercsoportok.txt', 'w')
    for i in range(100):
        r = randint(1,4)
        r2 = randint(1,2)
        csoport = ""
        if r == 1:
            csoport += "A"
        elif r == 2:
            csoport += "B"
        elif r == 3:
            csoport += "AB"
        elif r == 4:
            csoport += "0"
        
        if r2 == 1:
            csoport += "+"
        else:
            csoport += "-"
        
        f.write(csoport + '\n')


    f.close()



def feladat28():
    f = open('kopapirollo.txt', 'w')
    for i in range(10):
        tomi = randint(0,2)
        zoli = randint(0,2)
        if tomi == 0:
            tomi = "k "
        elif tomi == 1:
            tomi = "p "
        else:
            tomi = "o "

        if zoli == 0:
            zoli = "k "
        elif zoli == 1:
            zoli = "p "
        else:
            zoli = "o "

        f.write(tomi + zoli + '\n')


    f.close()





# -- meghivások --
# feladat16()
# feladat17()
# feladat18()
# fealadt19()
# feladat20()
# feladat21()
# feladat22()
# feladat23()
# feladat24()
# feladat25()
# feladat26()
# feladat27()
feladat28()





