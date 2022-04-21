class Versenyzo:
    def __init__(self, egysor):
        egysor = egysor.replace(',', '.')
        darabok = egysor.split("\t")
        self.nev = darabok[0]
        self.orszag = darabok[1]
        self.ugras1 = float(darabok[2])
        self.ugras2 = float(darabok[3])
        self.pont1 = float(darabok[4])
        self.pont2 = float(darabok[5])
        self.osszpontszam = self.pont1 + self.pont2

with open('siugras.txt', 'r') as f:
    beolvas = f.readlines()

versenyzok = []
for i in range(1,len(beolvas)):
    versenyzok.append(Versenyzo(beolvas[i]))


#masodik feladat
print(f'{len(versenyzok)}-en indultak a versenyen.')

#harmadik feladat
kanadaiak = 0
for versenyzo in versenyzok:
    if versenyzo.orszag == 'CAN':
        kanadaiak += 1
print(f'{kanadaiak} kanadai vett részt a versenyen.')

#negyedik feladat
orszagok = []
for versenyzo in versenyzok:
    if versenyzo.orszag not in orszagok:
        orszagok.append(versenyzo.orszag)
print(f'{len(orszagok)} ország vett részt a versenyen.')

for versenyzo in versenyzok:
    if versenyzo.nev == 'AMMANN Simon':
        print(f'AMMANN Simon {versenyzo.orszag}-nemzetiségü.')
        break

legnagyobb = versenyzok[0].osszpontszam
neve = versenyzok[0].nev
for versenyzo in versenyzok:
    if versenyzo.osszpontszam > legnagyobb:
        legnagyobb = versenyzo.osszpontszam
        nev = versenyzo.nev
print(f'A versenyt {nev} nyerte {legnagyobb} ponttal.')