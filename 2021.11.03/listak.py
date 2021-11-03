from random import *

#1. Olvass be pár számot (ha kell, a darabszámot is kérje be a program), majd írd 
#ki a páratlanok számát!
def elso():
    lista = []
#    elem = int(input('Add meg az elemek számát: '))
    elem = 10
    for i in range(0, elem):
        lista.append(randint(1,100))
    print(lista)
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

elso()
#masodik()
#harmadik()
#negyedik()
#otodik()
#hatodik()
#hetedik()
#nyolcadik()
#kilencedik()


