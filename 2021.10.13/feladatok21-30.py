#21. Írasd ki a szorzótáblát 1-5-szorzótáblák első tizenöt tagját

def huszonegy():
    n = 1
    while n<6:
        i = 1
        while i<16:
            a = i * n
            print(a, end=" ")
            i += 1
        print()
        n += 1

#22. Írasd ki öt olyan téglatestnek az oldalai nagyságát és térfogatát, aminek a oldala 1cm-rel, 
#b oldala 2cm-rel, c oldala 3cm-rel nő. Kezdőértékek : a = 2cm, b = 3cm, c = 5cm. 

def huszonketto():
    a, b, c = 2, 3, 5
    i = 1
    while i < 6:
        print(a * b *c)
        a += 1
        b += 2
        c += 3
        i += 1

#23. Írasd ki tíz kocka felszínét, aminek kezdő élhossza 5cm, és lépésenként 2cm-el növekszik. 
#A= 6*a*a.

def huszonharom():
    a, i = 5, 1
    while i < 11:
        print(6*a*a)
        a += 2
        i += 1


#24. Kérjünk be számokat, amíg 0-t nem írunk! 
def huszonnegy():
    i = int(input())
    while i != 0:
        i = int(input())

#25. Írj programot, ami csak pozitív számot hajlandó beolvasni!

def huszonot():
    i = int(input())
    while i > 0:
        i = int(input())



#26. Írj programot, mely addig olvas be számokat a billentyűzetről, ameddig azok kisebbek, 
#mint tíz. Írja ki ezek után a beolvasott számok összegét!

def huszonhat():
    i = float(input())
    a = []
    while i < 10:
        a.append(i)
        i = float(input())
    print(sum(a))


#27. Írj programot, ami csak az "alma" szót hajlandó beolvasni, ha ez sikerült, akkor kiírja, 
#hogy az "Az alma gyümölcs!"!

def huszonhet():
    i = str(input())
    while i.lower() != "alma":
        i = str(input())
    print("Az alma gyümölcs!")


#28. Írasd ki az első 30 egész szám összegét. 

def huszonnyolc():
    i, a = 1, 0
    while i < 31:
        a = a + i
        i += 1
    print(a)

#29. Írj programot, amely kiírja az első n szám összegét! 

def huszonkilenc():
    i, a = 1, 0
    while i < 31:
        a = a + i
        i += 1
    print(a)
#huszonegy()
#huszonketto()
#huszonharom()
#huszonnegy()
#huszonot()
#huszonhat()
#huszonhet()
huszonnyolc()
#huszonkilenc()
#harminc()