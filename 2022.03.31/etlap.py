class Etel:
    def __init__(self, egysor):
        darabok=egysor.strip('\n').split('\t')
        self.nev=darabok[0]
        self.ar=int(darabok[1])
        self.tipus=darabok[2]



f = open("etelek.txt", 'r')
beolvas = f.readlines()
f.close()
etelek = []
for item in beolvas:
    etelek.append(Etel(item))

def feladat2():
    print(f'2. feladat: Az étterem {len(etelek)} féle ételt kínál')

def feladat3():
    db = 0
    osszeg = 0
    for item in etelek:
        if item.tipus == 'Leves':
            db += 1
            osszeg += item.ar
    print(f'A levesek átlagos ára {osszeg/db} Ft.')

def feladat3maskepp():
    levesar = []
    for item in etelek:
        if item.tipus == 'Leves':
            levesar.append(item.ar)
    print(f'A levesek átlagos ára {sum(levesar)/len(levesar)} Ft.') 



def feladat4():
    db = 0
    for item in etelek:
        if item.tipus == 'Főétel':
            db += 1
    print(f'{db} db főétel közül lehet választani.')

def feladat5():
    for item in etelek:
        if 'liba' in item.nev.lower():
            print(item.nev)


# feladat2()
# feladat3()
# feladat3maskepp()
# feladat4()
feladat5()