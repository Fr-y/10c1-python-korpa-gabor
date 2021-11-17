from math import *
import random

szoveg = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Harum debitis porro ab saepe doloremque voluptate consectetur? Sequi explicabo quibusdam temporibus, cupiditate, amet laudantium obcaecati quis provident est hic qui cumque.'

#Vágjon föl egy hosszú stringet 5 karakter hosszú darabokra. Rakja össze a darabokat fordított
#sorrendben.
def elso():
    szo = 'eltöredezettségmentesítőtlenítetthetetlenségtelenítőtlenkedhetőiteknek' 
    lista = []
    for i in range(0, len(szo), 5):
        if i+5 < len(szo):
            lista.append(szo[i:i+5])
        else:
            lista.append(szo[i:])
    lista.reverse()
    for item in lista:
        print(item, end='')
#elso()




#Próbálja megírni a megtalal() függvényt, ami az ellenkezőjét csinálja, mint amit az 
#indexoperátor (vagyis a []) tesz. Ahelyett, hogy egy megadott indexhez megtalálja az annak 
#megfelelő karaktert, ennek a függvénynek egy adott karakterhez tartozó indexet kell 
#megtalálni.
def megtalal(szo, char):
    if char not in szo:
        print("Az adott betű nincs benne a szóba")
        return -1
    else:
        return szo.index(char)
#megtalal(szoveg, 'l')



#Tökéletesítse az előző gyakorlat függvényét úgy, hogy egy harmadik paramétert ad hozzá : 
#azt az indexet, amelyiktől kezdve keresni kell a karakterláncban. Így például a következő 
#utasításnak : 15 öt kell kiírni (és nem 4 et!)
#print megtalal("César & Cléopâtre", "r", 5)
def megtalal2(szo, char, ind):
    if char not in szo:
        print("Az adott betű nincs benne a szóba")
        return -1
    else:
        print(szo.index(char, ind))
        return szo.index(char, ind)
#megtalal2("César & Cléopâtre", "r", 5)



#Írjon egy karakterszam() függvényt, ami megszámolja, hogy egy karakter hányszor fordul elő 
#egy stringben. Így a következő utasításnak 4 et kell kiírni :
#print karakterszam("ananas au jus","a")
def karakterszam(szo, char):
    i = 0
    for betu in szo:
        if betu == char:
            i += 1
    return i

    # vagy
    # return szo.count(char)
#karakterszam("ananas au jus","a")



#Egy amerikai mesében nyolc kiskacsát rendre : Jack, Kack, Lack, Mack, Nack, Oack, Pack és 
#Qacknak hívnak. Írjon egy scriptet, ami ezeket a neveket a következö két stringből állítja elő :
#prefixes = 'JKLMNOPQ' és suffixe = 'ack'
#Ha egy for ... in ... utasítást alkalmaz, akkor a scriptjének csak két sort kell tartalmazni.
def otodik():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for char in prefixes:
        print(char + suffix, end=', ')
#otodik()


#Határozza meg egy adott mondatban a szavak számát.
def hatodik(mondat):
    szavak = mondat.split()
    print(len(szavak))
#hatodik(szoveg)



# Írjon egy nagybetu() függvényt, aminek a visszatérési értéke akkor « igaz », ha az 
#argumentuma nagybetű.
def nagybetu(char):
    if char.isupper() == True:
#        print("Nagybetü")
        return True
    else:
#        print("Nem nagybetü")
        return False
#nagybetu('A')

def kisbetu(char):
    if char.islower() == True:
#        print("Kisbetü")
        return True
    else:
#        print("Nem kisbetü")
        return False
#kisbetu('a')




#Írjon egy függvényt, aminek a visszatérési értéke akkor « igaz », ha az argumentuma szám.
def kilencedik(char):
    if str(char).isdigit() == True:
#        print("szám")
        return True
    else:
#        print("nem szám")
        return False
#kilencedik(56)



#Írjon egy függvényt, ami egy mondatot szavakból álló listává alakít át.
def szavakkaalakitas(mondat):
    szavak = mondat.split()
    return szavak
#szavakkaalakitas(szoveg)



#Használja fel az előző gyakorlatokban definiált függvényeket egy olyan script írására, ami ki 
#tudja szedni egy szövegből az összes nagybetűvel kezdődő szót.
def nagybetusszo(mondat):
    szavak = szavakkaalakitas(mondat)
    nagybetusszavak = []
    for szo in szavak:
        if nagybetu(szo[0]) == True:
            nagybetusszavak.append(szo) 
    print(nagybetusszavak)
#nagybetusszo("E szavakhoz még ha lehet is Értelmes Szövegösszefüggést alkotni, jelentésük Rendszerint nem határozható meg egyértelműen tagjaikból, Képzésük pedig nemritkán szabálytalan.")


#Írjon egy függvényt, aminek akkor « igaz » a visszaérési értéke, ha az argumentuma egy 
#alfabetikus karakter (nagy vagy kisbetű). Alkalmazza ebben az új függvényben az előzőekben 
#definiált kisbetu() és nagybetu() függvényeket
def alfabetikus(char):
    if kisbetu(char) or nagybetu(char) == True:
        print('Alfabetikus karakter')
        return True
#alfabetikus('a')

#Írjon egy függvényt, aminek akkor « igaz » a visszaérési értéke, ha az argumentuma egy szám.
def numerikus(char):
    if char.isnumeric() == True:
        return True
#numerikus('6')



#Írjon egy függvényt, ami az argumentumaként megadott mondatban lévő nagybetűk számát 
#adja meg visszaérési értékként
def tizennegy(mondat):
    i = 0
    for char in mondat:
        if nagybetu(char) == True:
            i += 1
    print(i)
#tizennegy(szoveg)




# Írjon egy egy ASCII kódtáblát kiíró scriptet. A programnak minden karaktert ki kell írni. A 
#táblázat alapján állapítsa meg a nagybetűs és kisbetűs karaktereket összekapcsoló relációt 
#minden egyes karakterre.
def ascii():
    for i in range(256):
        print(chr(i), end=" ")
#ascii()


# Az előző gyakorlatban megtalált reláció alapján írjon egy függvényt, ami egy mondat 
#valamennyi karakterét kisbetűre írja át.
def kisbetusites(mondat):
    kisbetusitett = ""
    szoveg = list(mondat)
    a = []
    i = 0
    for char in mondat:
        if nagybetu(char) == True:
            a.append(i)
            kisbetusitett += chr(ord(char) + 32)
        i += 1

    for i in range(len(a)):
        n = a[i]
        szoveg[n] = kisbetusitett[i]
    for i in szoveg:
        print(i, end="")
#kisbetusites(szoveg)




# Ugyanennek a relációnak az alapján írjon egy függvényt, ami valamennyi kisbetűt nagybetűvé 
#alakít át és viszont (az argumentumként megadott mondatban).
def nagybetusites(mondat):
    nagybetusitett = ""
    szoveg = list(mondat)
    a = []
    i = 0
    for char in mondat:
        if kisbetu(char) == True:
            a.append(i)
            nagybetusitett += chr(ord(char) - 32)
        i += 1

    for i in range(len(a)):
        n = a[i]
        szoveg[n] = nagybetusitett[i]
    for i in szoveg:
        print(i, end="")
#nagybetusites(szoveg)





#Írjon egy függvényt, ami megszámolja, hogy az argumentumként megadott karakter hányszor 
#fordul elő egy adott mondatban.
def char_in_sentence(char, mondat):
    n = 0
    for i in mondat:
        if char == i:
            n += 1
    print(n)
#char_in_sentence('a', 'almafa')

#Írjon egy függvényt, ami visszatérési értékként megadja egy adott mondatban a 
#magánhangzók számát.
def vowels_in_sentence(mondat):
    vowels = ["a","A","á","Á","e","E","é","É","i","I","í","Í","o","O","ó","Ó","ö","Ö","ő","Ő","u","U","ú","Ú","ü","Ü","ű","Ű"]
    n = 0
    for char in mondat:
        if char in vowels:
            n += 1
    print(n)
    return n
#vowels_in_sentence(szoveg)



#Írjon egy scriptet, ami a 20 tól 40 ig terjedő számok négyzeteit és köbeit állítja elő.
def huszadik():
    for i in range(20, 40):
        print(i * i, i * i * i)
#huszadik()



#Írjon egy scriptet, ami 5°onként automatikusan előállítja a 0° és 90° közé eső szögek sinusait.
#Figyelem : a math modul sin() függvénye úgy tekinti, hogy a szögek radiánban vannak 
#megadva 
#(360° = 2 p radián)
def szinusz():
    for i in range(0, 95, 5):
        print(sin(i * (pi/180)))
#szinusz()





#Írjon egy scriptet, ami a 2, 3, 5, 7, 11, 13, 17, 19 es szorzótáblák első 15 tagját állítják elő a 
#képernyőn a következő táblázathoz hasonlóan (ezeket a számokat egy listába fogjuk 
#elhelyezni):
def szorzotabla(szam):
    a = ""
    for i in range(1, 16):
        a += f' {str((i * szam))}'
    return a[1:]

def huszonketto():
    b = []
    primes = [2,3,5,7,11,13,17,19]
    for x in primes:
        b.append(szorzotabla(x))
    for i in b:
        print(i)
#huszonketto()




def huszonharom():
#Legyen adott a következő lista :
    a = ['JeanMichel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'AlexandreBenoît', 'Louise']
#Írjon egy scriptet, ami kiírja a neveket és a nevekben lévő karakterek számát
    for i in a:
        print(i, len(i))
#huszonharom()


#Van egy egész számokat tartalmazó lista, amiben egyes számok többször is előfordulnak. 
#Írjon egy scriptet, ami a listát úgy másolja át egy másik listába, hogy figyelmen kívül hagyja a 
#többszöri előfordulásokat. A végső listának rendezettnek kell lenni.
def huszonnegy():
    a = [1,3,34,6,5,3,235,47,3,2,3,5,7678,3]
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    b.sort()
    print(b)
#huszonnegy()




# Írjon egy scriptet, ami megkeresi egy adott mondatban a leghosszabb szót (a program 
#felhasználójának be kell tudnia írni egy általa választott mondatot).
def longest_word():
    szavak = str(input()).split()
    leghosszabb = 0
    leghosszabbszo = ""
    for szo in szavak:
        if len(szo) > leghosszabb:
            leghosszabb = len(szo)
            leghosszabbszo = szo
    print(leghosszabbszo)
#longest_word()




#Írjon egy scriptet, ami kiíratja egy csütörtöki nappal kezdődő képzeletbeli év napjainak a 
#listáját. A scriptben három lista lesz : az egyik a hét napjainak a neveit fogja tartalmazni, a 
#másik a hónapok neveit, a harmadik pedig hogy hány naposak a hónapok (a szökőéveket nem 
#vesszük figyelembe).
def naptar():
    napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]
    honapok = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június', 'Július', 'Augusztus', 'Szeptember', 'Október', 'November', 'December']
    honapnapok = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    nap = 3
    for n in range(len(honapok)):
        for i in range(1, honapnapok[n]+1):
            print(honapok[n], i, napok[nap])
            if 6 > nap:
                nap += 1
            else:
                nap = 0
#naptar()



def huszonhet():
#Legyenek adottak a következő listák :
    t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
    t2 = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június', 'Július', 'Augusztus', 'Szeptember', 'Október', 'November', 'December']
#Írjunk egy kis programot, ami a második listába úgy szúrja be az első lista összes elemét, hogy
#mindegyik hónap nevét az illető hónap napjainak száma követi : 
    t3 = []
    i = 0
    for item in t1:
        t3.append(t2[i])
        t3.append(t1[i])
        i += 1
    print(t3)
#huszonhet()




#Hozzunk létre egy A listát, ami tartalmaz néhány elemet. Hozzuk létre ennek egy valódi 
#másolatát az új B változóban. Ötlet : először hozzunk létre egy csupa nullákat tartalmazó B 
#listát, aminek a mérete megegyezik az A lista méretével. Ezután helyettesítsük a nullákat az A 
#elemeivel.
def huszonnyolc():
    A = random.sample(range(0,100),10)
    B = [0,0,0,0,0,0,0,0,0,0]

    i = 0
    for elem in A:
        B[i] = elem
        i += 1
    print(A,B)
#huszonnyolc()


#Ugyanaz a probléma, de más az ötlet : először hozzunk létre egy üres B listát. Ezután töltsük 
#azt fel az A elemeinek segítségével.
def huszonkilenc():
    B = []
    A = random.sample(range(0,100),10)
    for elem in A:
        B.append(elem)
    print(B,A)
#huszonkilenc()


#Ugyanaz a probléma, de megint más az ötlet : a B lista létrehozásához az A listában vágjunk 
#egy olyan szeletet, ami az összes elemet tartalmazza (a [:] operátor segítségével.)
def harminc():
    A = random.sample(range(0,100),10)
    B = A[:]
    print(A,B)
#harminc()





#Egy prímszám olyan szám, aminek pontosan két osztója van, egy és önmaga. Írjon programot, 
#ami az eratosztenészi szita módszerének alkalmazásával az összes 1 és 1000 közötti 
#prímszámot előállítja :
#Hozzon létre egy 1000 elemből álló listát, minden listaelem kezdőértéke 1 legyen.
#Járja be ezt a listát a 2 indexű elemtől kezdve :
#ha a vizsgált elem értéke 1, akkor tegye nullává a lista azon elemeit, melyeknek indexe egész 
#számú többszöröse az aktuális indexnek amikor így bejárta az egész listát, akkor azoknak az 
#elemeknek az indexei lesznek a keresett prímszámok, mely elemek értéke 1 maradt.
def szita():
    A = [1 for x in range(1000)]
    for i in range(2, len(A)+1):
        for j in range(i, len(A)):
            if j % i == 0 and j != i:
                A[j] = 0
    return A

def primek():
    b = []
    A = szita()
    n = 0
    for i in A:
        if i == 1:
            b.append(n)
        n += 1
    print(b[2:])
#primek()


#Írjon egy scriptet, ami véletlen szerűen húz kártyalapokat. A kihúzott kártya nevét korrekten 
#kell, hogy megadja. A program például kiírja :
#Nyomjon <Enter>t egy lap húzásához :
#Treff 1
def kartyahuzas():
    tipusok = ["Pikk", "Káró", "Treff", "Kőr"]
    kartyak = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Bubi", "Dáma", "Király", "Ász"]
    input('Nyomjon <Enter>t egy lap húzásához        ')
    print(random.choice(tipusok), random.choice(kartyak))
#kartyahuzas()