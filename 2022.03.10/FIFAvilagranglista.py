class Csapat:
    def __init__(self, egysor): # konstruktor: kezdőértékek beállitása
        darabok = egysor.split(';')

        self.csapat = darabok[0]
        self.helyezes = int(darabok[1])
        self.valtozas = int(darabok[2])
        self.pontszam = int(darabok[3])

# --main--
f = open("fifa.txt", 'r')
beolvas = f.readlines()
minden = f.readline()
f.close()
csapatok = []
for i in range(1, len(beolvas)):
    csapatok.append(Csapat(beolvas[i]))
print(f'3. feladat: A világranglistán {len(csapatok)} csapat szerepel')

osszeg = 0
for item in csapatok:
    osszeg += item.pontszam
print(f'4. feladat: A csapatok átlagos pontszáma: {round(osszeg/len(csapatok), 2)} pont')

valtozasok = []
for item in csapatok:
    valtozasok.append(item.valtozas)
maxvaltozas = max(valtozasok)
valtozasindex = valtozasok.index(maxvaltozas)
print(f'5. feladat: A legtöbbet javító csapat:\n \tHelyezés: {csapatok[valtozasindex].helyezes}\n \tCsapat: {csapatok[valtozasindex].csapat}\n \tPontszám: {csapatok[valtozasindex].pontszam}')

f = open("fifa.txt", 'r')
minden = f.read()
f.close()
if "Magyarország" in minden:
    print('6. feladat: A csapatok között van Magyarország')
else:
    print('6. feladat: A csapatok között nincs Magyarország')
