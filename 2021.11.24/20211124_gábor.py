from random import *

maganhangzok = "aáeéoóöőüűuúií"

def elso():  
    a = [x * n for x in range(20, 41)]
    print(a)


    # //vagy

    # a = []
    # for x in range(20, 41):
    #     a.append(x * x)

    # print(a)

def masodik():
    a = "Az ősz annyira szereti a naplementéket, hogy minden egyes levélre egyet fest."


    #a feladat
    print(len(a), 'karakterből áll')


    #b feladat
    b = a.split()
    print(len(b), 'szóbol áll')


    #c feladat
    e = 0
    for char in a:
        if char == 'e':
            e += 1
    print(e,'e betü van benne')


    #d feladat
    mhangzokszama = 0
    for char in a:
        if char.lower() in maganhangzok:
            mhangzokszama += 1
    print(mhangzokszama, 'maganhangzó van a mondatba')



def harmadik():
    a = [randint(0, 100) for x in range(15)]
    print(a)
    
    #a feladat
    print(sum(a), "a listában lévő számok összege")


    #b feladat
    print(sum(a) / 15, 'a számok átlaga')


    #c faleadat
    print(max(a) - min(a), 'a számok terjedelme')


    #d fealdat
    oszthato = []
    for szam in a:
        if szam % 3 == 0:
            oszthato.append(szam)
    print(len(oszthato), 'hárommal osztható szám van amelyek:', oszthato)


# elso()
#masodik()
harmadik()