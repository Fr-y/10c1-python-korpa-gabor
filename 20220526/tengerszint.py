#8.
class Magassag:
    def __init__(self, egysor):
        darabok=egysor.strip('\n').split('\t')
        self.orszag = darabok[0]
        self.foldrajzi_hely = darabok[1]
        self.magassag = int(darabok[2])

#9   
with open('tengerszint.txt', 'r') as f:
    sorok = f.readlines()

magassagok = []
for sor in sorok:
    magassagok.append(Magassag(sor))

#10
print(f'10. feladat: \n\t{len(magassagok)} ország legmagasabb pontja szerepel a listán')

#11
otezer = 0
for magassag in magassagok:
    if magassag.magassag > 5000:
        otezer += 1
print(f'11. feladat: \n\t{otezer} ország legnagyobb tengerszint feletti magassága haladja meg az 5000 métert')

#12
van = False
haromezer = ''
for magassag in magassagok:
    if magassag.magassag == 3000:
        van = True
        haromezer = magassag


if van:
    print(f'''12. feladat:
        {haromezer.magassag} méter tengerszint feletti magasságú {haromezer.orszag} legmagasabb pontja {haromezer.foldrajzi_hely}''')
else:
    print('''12. feladat:
        Nincs 4100 méter magasságú ország.''')