from random import *
# randint(tól, ig) random egész szám
# randrange(tól, ig)  random egész szám
# random() [0, 1] között 


#41. Generálj 10 véletlenszámot és írasd ki a képernyőre vesszővel elválasztva! 

def negyvenegy():
    for i in range(10):
        print(randint(1, 100), end=", ")


#42. Generálj 20 véletlenszámot 0 és 20 között, és írasd ki a képernyőre vesszővel elválasztva! 

def negyvenketto():
    for i in range(20):
        print(randint(0, 20), end=", ")


#43. Generálj 15 véletlenszámot 25 és 50 között, és írasd ki a képernyőre vesszővel elválasztva! 

def negyvenharom():
    for i in range(15):
        print(randint(25, 50), end=", ")


#44. Generálj két egész véletlen számot 10 és 50 között, írasd ki a szorzatát! 

def negyvennegy():
    a, b = randint(10, 50), randint(10, 50)
    print(a * b)


#45. Generálj két véletlen, valós számot 18 és 69 között, írasd ki a hányadukat úgy, hogy a 
#nagyobbat osztod a kisebbel. 

def negyvenot():
    a, b = randint(18, 69), randint(18, 69)
    print(a, b)
    print('Hányaduk:', max(a, b) / min(a, b), 'Hányadosuk:',max(a, b) // min(a, b), )


#46. Generálj 7 véletlen számot, add össze őket és írasd ki a végeredményt! 

def negyvenhat():
    ossz = 0
    i = 1
    while i < 8:
        a = randint(1, 100)
        ossz += a
        i += 1
    print(ossz)


#47. Generálj 10db páros számot, szorozd össze őket. Minden szorzatot írass ki! 

def negyvenhet():
    szorzat = 1
    i = 1
    while i < 10 or i == 10:
        gen = randint(1, 10)
        if gen % 2 == 0:
            i += 1
            szorzat *= gen
            print(gen, end=" ")
    print(szorzat)


#48. Generálj számokat 10 és 50 között, amíg a generált érték 25 nem lesz! A generált 
#számokat írd ki egymás mellé (…, …, …, …….25)! 

def negyvennyolc():
    gen = randint(10, 50)
    print(gen, end=" ")
    while gen != 25:
        gen = randint(10, 50)
        print(gen, end=" ")
    

#49. A 'keresztül-kasul' szóból véletlenszerűen válasz ki 5 elemet(betűt),fűzd össze őket és 
#írasd ki a végeredményt! 

def negyvenkilenc():
    a = ''
    while len(a) != 5:
        b = choice('keresztül-kasul')
        a += b
    print(a)
    


#negyvenegy()
#negyvenketto()
#negyvenharom()
#negyvennegy()
#negyvenot()
#negyvenhat()
#negyvenhet()
#negyvennyolc()
#negyvenkilenc()