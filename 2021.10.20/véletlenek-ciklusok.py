from random import *

# randint(tól, ig) random egész szám
# randrange(tól, ig)  random egész szám
# random() [0, 1] között 

#45. Generálj két véletlen, valós számot 18 és 69 között, írasd ki a hányadukat úgy, hogy a 
#nagyobbat osztod a kisebbel. 
def negyvenot():
    a, b = randint(18, 69), randint(18, 69)
    print(a, b)
    print('Hányaduk:', max(a, b) / min(a, b), 'Hányadosuk:',max(a, b) // min(a, b), )


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
    


#negyvenot()
#negyvenhet()
#negyvennyolc()