class Jatekos:
    def __init__(self, egysor):
        egysor = egysor.split(";")
        self.helyezes = egysor[0]
        self.nev = egysor[1]
        self.orszag = egysor[2]
        self.nyeremeny = int(egysor[3].strip('\n'))

with open('snooker.txt', 'r') as f:
    sorok = f.readlines()

jatekosok = []
for i in range(1, len(sorok)):
    jatekosok.append(Jatekos(sorok[i]))

#harmadik feladat
print(f'3. feladat: A világranglistán {len(jatekosok)} versenyző szerepel')

#negyedik feladat
nyeremenyek = []
for jatekos in jatekosok:
    nyeremenyek.append(jatekos.nyeremeny)
atlagnyeremeny = sum(nyeremenyek) / len(nyeremenyek)
print(f'4. feladat: A versenyzők átlagosan {atlagnyeremeny} fontot kerestek')


# #ötödik feladat
legnagyobb = 0
lnjatekos = []
for jatekos in jatekosok:
    if jatekos.orszag == 'Kína':
        if jatekos.nyeremeny > legnagyobb:
            legnagyobb = jatekos.nyeremeny
            lnjatekos = jatekos

print(f'5. feladat: A legjobban kereső kínai versenyző:\n\tHelyezés: {lnjatekos.helyezes}')
print(f'\tNév: {lnjatekos.nev}')
print(f'\tOrszág: {lnjatekos.orszag}')
print(f'\tNyeremény: {lnjatekos.nyeremeny * 380} Ft')


#hatodik feladat
van = False
for jatekos in jatekosok:
    if jatekos.orszag == 'Norvégia':
        van = True
if van:
    print(f'6. feladat: A versenyzők között van norvég versenyző')
else:
    print(f'6. feladat: A versenyzők között nincs norvég versenyző')


# hetedik feladat
with open('snooker.txt', 'r') as f:
    beolvas = f.read()
orszagok = []
for jatekos in jatekosok:
    if jatekos.orszag not in orszagok:
        orszagok.append(jatekos.orszag)
orszagfok = []
for orszag in orszagok:
    if beolvas.count(orszag) > 5:
        orszagfok.append(f'{orszag} - {beolvas.count(orszag)} fő')
print('7. feladat: Statisztika')
for orszag in orszagfok:
    print(f'\t {orszag}')


