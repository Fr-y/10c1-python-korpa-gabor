from random import *

def alapok():
    lista = [0,1,2,3,4,5,7,8,9,10]
    print(lista[0])
    print(lista[-1]) #utolsó elem
    print(lista[0:4]) # 0,1,2,3 indexű elemeket
    print(lista[2:5]) # 3,4,5
    print(lista[7:]) # 8tól végéig
    print(lista[:5])
    lista[5] = 'alma'
    print(lista)
    for item in lista:
        print(item, end=" ")
    print()
    print(len(lista)) # elemek száma
    print(lista.index('alma')) # hanyadik indexen található
    lista.pop() # utolso elem eltávolitása
    for item in lista:
        print(item, end=" ")
    lista.remove('alma') # adott elem eltávolitása
    print(lista)
    lista.pop(3) #adott index eltavolitasa
    print(lista)
#    lista.clear() # minden elem törlese
#    del lista # teljes lista törlese
    lista.reverse() # sorrend forditasa
    print(lista)
    lista.sort() # novekvo sorrendbe rendezés
    print(lista)
    lista.insert(3, 'körte') # adott indexbe való beszúrás
    print(lista)

#1. Olvass be pár számot (ha kell, a darabszámot is kérje be a program), majd írd 
#ki a páratlanok számát!
def elso():
    lista = []
    elem = int(input('Add meg az elemek számát: '))
    for i in range(0, elem):
        lista.append(randint(1,100))
    i = 0
    for item in lista:
        if item % 2 != 0:
            i += 1
    print('Páratlanszámok száma:',i)


#2. Olvass be egy pár számot (ha kell, a darabszámot is kérje be a program), majd 
#írd ki a párosok összegét!
def masodik():
    lista = []
    elem = int(input('Add meg az elemek számát: '))
    for i in range(0, elem):
        lista.append(randint(1,100))
    i = 0
    for item in lista:
        if item % 2 == 0:
            i += item
    print('Párosszámok összege:',i)


#3. Olvass be egy pár számot (ha kell, a darabszámot is kérje be a program), majd 
#írd ki a párosokat a képernyőre, a sorszámukkal együtt, vagyis hogy hányadiknak 
#olvastad be őket!
def harmadik():
    lista = []
    elem = int(input('Add meg az elemek számát: '))
    for i in range(0, elem):
        lista.append(randint(1,100))
    for item in lista:
        if item % 2 == 0:
            print(item, '|', lista.index(item) + 1, '-ik elem')
    print(lista)


#4. Olvass be egész számokat egy tömbbe/listába (ha kell, a darabszámot is kérje 
#be a program), majd kérj be egy egész számot. Keresd meg a tömbben az első 
#ilyen egész számot, majd írd ki a tömbindexét. Ha a tömbben nincs ilyen szám, 
#írd ki, hogy a beolvasott szám nincs a tömbben.
def negyedik():
    lista = []
    elem = int(input('Add meg az elemek számát: '))
    for i in range(0, elem):
        lista.append(randint(1,100))
    szam = int(input('Adj meg egy egész számot: '))
    if szam in lista:
        print('A megadott szám a', lista.index(szam), '-es indexen van a listában')
    else:
        print('A megadott szám nincs a listában:', lista)


#5. Olvass be egész számokat egy tömbbe/listába (ha kell, a darabszámot is kérje 
#be a program), majd kérj be egy egész számot, és mondd meg, hogy hányszor 
#szerepel a tömbben.
def otodik():
    lista = []
    elem = int(input('Add meg az elemek számát: '))
    for i in range(0, elem):
        lista.append(randint(1,100))
    szam = int(input('Adj meg egy egész számot: '))
    i = 0
    for item in lista:
        if item == szam:
            i += 1
    print('A szám', i, 'szer szerepel a listában')


#6. Olvasd be egy tömbbe/listába az osztály tanulóinak keresztneveit (ha kell, a 
#darabszámot is kérje be a program). Mondd meg, hogy egy adott keresztnevű 
#tanulóból hány jár az osztályba (a keresett nevet is kérje be a program).
def hatodik():
    nevek = ['balázs', 'gergő', 'zoltán', 'milán', 'zalán', 'gergő', 'gábor', 'bálint', 'martin', 'marci']
    nev = str(input('Adj meg egy nevet: '))
    i = 0
    for item in nevek:
        if item == nev:
            i += 1
    print(i, nev, 'nevű ember jár az osztályba')

#alapok()
#elso()
#masodik()
#harmadik()
#negyedik()
#otodik()
hatodik()
#hetedik()
#nyolcadik()
#kilencedik()


