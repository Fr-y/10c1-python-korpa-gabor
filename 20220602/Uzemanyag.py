#2.feladat
class Valtozas:
    def __init__(self, sor):
        darabok=sor.strip('\n').split(';')
        datum=darabok[0].split('.')
        self.datum = darabok[0]
        self.ev=int(datum[0])
        self.honap=int(datum[1])
        self.nap=int(datum[2])
        self.benzinar=int(darabok[1])
        self.gazolajar=int(darabok[2])
        self.kulonbseg = abs(self.gazolajar - self.benzinar)


with open('uzemanyag.txt', 'r') as f:
    beolvas = f.readlines()

valtozasok = []
for sor in beolvas:
    valtozasok.append(Valtozas(sor))

#3.feladat
print('3. feladat: változások száma:', len(valtozasok))

#4.feladat
legkisebb = 0
for valtozas in valtozasok:
    if valtozas.kulonbseg > legkisebb:
        legkisebb = valtozas.kulonbseg

print('4. feladat: A legkisebb különbség:', legkisebb)

#5.feladat
szamlalo = 0
for valtozas in valtozasok:
    if valtozas.kulonbseg == legkisebb:
        szamlalo += 1

print('5. feladat: A legkisebb különbség előfordulása:', szamlalo)

#6.feladat
volte = False
for valtozas in valtozasok:
    #ha szokoev
    if valtozas.ev % 4 == 0:
        #ha szokonap
        if valtozas.honap == 2 and valtozas.nap == 24:
            volte = True

if volte:
    print('6. feladat: Volt változás szökőnapon!')
else:
    print('6. feladat: Nem volt változás szökőnapon!')

#7.feladat
with open('euro.txt', 'a') as f:
    eu = 307.7
    for valtozas in valtozasok:
        benzineu = round(valtozas.benzinar / eu, 2)
        gazolajeu = round(valtozas.gazolajar / eu, 2)
        f.write(f'{valtozas.datum};{benzineu};{gazolajeu}\n')