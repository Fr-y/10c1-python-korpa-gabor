from random import *
from math import *



def feladat1():
    f = open('novekvo.txt', 'w')
    for i in range(1,11):
        if i == 10:
            f.write(str(i))
        else:
            f.write(str(i) + ' ')
    f.close()



def feladat2():
    f = open('negyzetek.txt', 'w')
    for i in range(1,16):
        if i == 15:
            f.write(str(i*i))
        else:
            f.write(str(i*i) + ' ')
    f.close()



def feladat3():
    f = open('veletlenek.txt', 'w')
    for i in range(10):
        f.write(f'{randint(100,200)} ')
    f.close()



def feladat4():
    f = open('matek.txt', 'w')
    for i in range(15):
        f.write(f'{randint(1,5)} ')
    f.close()



def feladat5():
    f = open('cipomeret.txt', 'w')
    for i in range(28):
        f.write(f'{randint(35,45)} ')
    f.close()



def feladat6():
    f = open('parosak.txt', 'w')
    for i in range(1,21):
        if i % 2 == 0:
            f.write(f'{i} ')
    f.close()



def feladat7():
    f = open('bitek.txt', 'w')
    for i in range(100):
        f.write(f'{randint(0,1)}')
    f.close()



def feladat8():
    f = open('nemek.txt', 'w')
    for i in range(100):
        gen = randint(1,2)
        if gen == 1:
            f.write(",F")
        if gen == 2:
            f.write(",N")
    f.close()



def feladat9():
    f = open('penzdobas.txt', 'w')
    for i in range(500):
        gen = randint(1,2)
        if gen == 1:
            f.write("fej \n")
        if gen == 2:
            f.write("iras \n")
    f.close()



def feladat10():
    f = open('intelligencia.txt', 'w')
    for i in range(120):
        f.write(f'{randint(110,145)} \n')
    f.close()



def feladat11():
    f = open('legnyomas.txt', 'w')
    for i in range(30):
        f.write(f'{randint(993 , 1041)} hPa \n')
    f.close()


# for i in range(256):
#         print(chr(i), end=" ")

def feladat12():
    f = open('karakterek.txt', 'w')
    for i in range(30):
        f.write(f'{randint(993 , 1041)} hPa \n')
    f.close()





# -- main --
# feladat1()
# feladat2()
# feladat3()
# feladat4()
# feladat5()
# feladat6()
# feladat7()
# feladat8()
# feladat9()
# feladat10()
feladat11()