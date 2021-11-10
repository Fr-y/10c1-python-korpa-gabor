
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
    else:
        print(szo.index(char))
#megtalal('almafa', 'l')




#Tökéletesítse az előző gyakorlat függvényét úgy, hogy egy harmadik paramétert ad hozzá : 
#azt az indexet, amelyiktől kezdve keresni kell a karakterláncban. Így például a következő 
#utasításnak : 15 öt kell kiírni (és nem 4 et!)
#print megtalal("César & Cléopâtre", "r", 5)
def megtalal2(szo, char, index):
    if char not in szo:
        print("Az adott betű nincs benne a szóba")
    else:
        print(szo.index(char, 5))
#megtalal2("César & Cléopâtre", "r", 5)



#Írjon egy karakterszam() függvényt, ami megszámolja, hogy egy karakter hányszor fordul elő 
#egy stringben. Így a következő utasításnak 4 et kell kiírni :
#print karakterszam("ananas au jus","a")
def karakterszam(szo, char):
    i = 0
    for betu in szo:
        if betu == char:
            i += 1
    print(i)
#karakterszam("ananas au jus","a")



#Egy amerikai mesében nyolc kiskacsát rendre : Jack, Kack, Lack, Mack, Nack, Oack, Pack és 
#Qacknak hívnak. Írjon egy scriptet, ami ezeket a neveket a következö két stringből állítja elő :
#prefixes = 'JKLMNOPQ' és suffixe = 'ack'
#Ha egy for ... in ... utasítást alkalmaz, akkor a scriptjének csak két sort kell tartalmazni.
def otodik():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for char in prefixes:
        print(prefixes[prefixes.index(char)] + suffix, end=', ')
#otodik()


#Határozza meg egy adott mondatban a szavak számát.
def hatodik(mondat):
    szavak = mondat.split()
    print(len(szavak))
#hatodik('Ez egy nagyon hosszú mondat sok szóval benne.')



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
#szavakkaalakitas("Ez egy nagyon hosszú mondat sok szóval benne.")



#Használja fel az előző gyakorlatokban definiált függvényeket egy olyan script írására, ami ki 
#tudja szedni egy szövegből az összes nagybetűvel kezdődő szót.
def nagybetusszo(mondat):
    szavak = szavakkaalakitas(mondat)


    nagybetusszavak = []
    for szo in szavak:
        if nagybetu(szo) == True:
            nagybetusszavak.append(szo)
        else:
            
    print(nagybetusszavak)

nagybetusszo("E szavakhoz még ha lehet is értelmes Szövegösszefüggést alkotni, jelentésük Rendszerint nem határozható meg egyértelműen tagjaikból, Képzésük pedig nemritkán szabálytalan.")
