from random import randint

def feladat26():
    f = open('fogyasztas.txt', 'w')
    for i in range(12):
        km = randint(480,540)
        l = randint(367, 398) / 10
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
            csoport += " +"
        else:
            csoport += " -"
        
        f.write(f'{csoport}\n')

    f.close()

def feladat27masik():
    f = open("vercsoportok2.txt", 'w')
    vercsoportok = ["A", "B", "AB", "0", "+", "-"]
    for i in range(100):
        r = randint(0,3)
        r2 = randint(4,5)
        f.write(f'{vercsoportok[r]} {vercsoportok[r2]}\n')


    f.close()


def feladat28():
    f = open('kopapirollo.txt', 'w')
    kpo = ["k","p","o"]
    for i in range(10):
        tomi = randint(0,2)
        zoli = randint(0,2)
        f.write(f'{kpo[tomi]} {kpo[zoli]} \n')

    f.close()

def feladat29():
    f = open("tarsas.txt", "w")
    for i in range(100):
        dobas = [randint(1,6) for x in range(3)]
        for item in range(len(dobas)):
            f.write(f'{dobas[item]} ')
        f.write("\n")

    f.close()


def feladat30():
    f = open("skandinyerő.txt", "w")
    for i in range(2):
        for i in range(7):
            f.write(f'{randint(1,35)} ')
        f.write('\n')
    
    f.close()


# feladat26()
# feladat27()
# feladat27masik()
# feladat28()
# feladat29()
feladat30()