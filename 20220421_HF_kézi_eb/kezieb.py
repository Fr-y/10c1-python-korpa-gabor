from audioop import avg


class Jatekos:
    def __init__(self,egysor):
        egysor = egysor.split(";")
        self.nev = egysor[0]
        self.gol = int(egysor[1])
        self.loves = int(egysor[2])
        self.sikeres_hetmeteres = int(egysor[3])
        self.probalt_hetmeteres = int(egysor[4])
        self.kiallitas = int(egysor[5])
        self.poszt = egysor[6]
        self.szuletes = egysor[7]
        self.magassag = int(egysor[8])
        self.csapat = egysor[9].strip('\n')


#beolvasas
with open('kezieb.txt', 'r', encoding='utf8') as f:
    beolvas = f.readlines()

#masodik feladat
jatekosok = []
for sor in beolvas:
    jatekosok.append(Jatekos(sor))
print(f'2. feladat: A magyar csapatban {len(jatekosok)} mezőnyjátékos szerepelt.')

#harmadik feladat
beallok = []
for jatekos in jatekosok:
    if jatekos.poszt == 'beálló':
        beallok.append(jatekos)
print('3. feladat: Beállók:')
for beallo in beallok:
    print(f'\t {beallo.nev}')

#negyedik feladat
csapatok = []
for jatekos in jatekosok:
    if jatekos.csapat not in csapatok:
        csapatok.append(jatekos.csapat)
csapatok.sort()
print('4. feladat: A játékosokat adó csapatok:')
for csapat in csapatok:
    print(f'\t {csapat}')

#otodik feladat
otgol = []
for jatekos in jatekosok:
    if jatekos.gol > 5:
        otgol.append(jatekos.nev)
otgol.sort()
print('5. feladat: Öt gólnál többet dobtak:')
for jatekos in otgol:
    print(f'\t {jatekos}')

#hatodik feladat
osszgol = 0
for jatekos in jatekosok:
    osszgol += jatekos.gol
print(f'6. feladat: A magyar csapat összesen {osszgol} gólt lőtt.')

#hetedik feladat
hetmeteresjatekosokszama = 0
for jatekos in jatekosok:
    if jatekos.sikeres_hetmeteres > 0:
        hetmeteresjatekosokszama += 1
print(f'7. feladat: {hetmeteresjatekosokszama} dobott hétméterest.')

#nyolcadik feladat
osszkiallitas = 0
for jatekos in jatekosok:
    if jatekos.kiallitas > 0:
        osszkiallitas += jatekos.kiallitas * 2 #mivel ket perces kiallitasok
print(f'8. feladat: {osszkiallitas} perc büntetést kapott a csapat.')

#tizenegyedik feladat
magassagok = []
for jatekos in jatekosok:
    if jatekos.magassag not in magassagok:
        magassagok.append(jatekos.magassag)
atlag_magassag = round(sum(magassagok) / len(magassagok))
print(f'9. feladat: A csapat átlagmagassága {atlag_magassag} cm.')

#tizenharmadik feladat
KSE = 0
for jatekos in jatekosok:
    if jatekos.csapat == 'Balatonfüredi KSE':
        KSE += 1
print(f'13. feladat: A Balatonfüredi KSE {KSE} játékost adott a válogatottnak.')

#tizennegyedik feladat
for jatekos in jatekosok:
    if jatekos.nev == 'Lékai Máté':
        print(f'14. feladat: Lékai Máté a {jatekos.csapat}-ben jatszik')

#tizenötödikfeladat:
vane = False
for magassag in magassagok:
    if magassag > 200:
        vane = True
if vane:
    print(f'15. feladat: Van olyan játkos, aki 200 cm magas.')
else:
    print(f'15. feladat: Nincs olyan játkos, aki 200 cm magas.')
