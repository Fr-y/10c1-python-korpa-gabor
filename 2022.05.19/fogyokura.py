#elso feladat
ido = int(input('Hetek száma='))
cel = float(input('Elérni kívánt testtömeg (kg)='))

#masodik feladat
tomegek = []
for i in range(1, ido+1):
    tomegek.append(float(input(f'{i}. héten=')))

#harmadik feladat
for i, tomeg in enumerate(tomegek):
    if cel > tomeg:
        print(f'Mari néni a(z) {i+1}. héten érte el a célt.')
        break
else: print('Sajnos Mari néni nem érte el a célját')

#negyedik feladat
elozotomeg = tomegek[0]
hizas = 0
for tomeg in tomegek:
    if tomeg > elozotomeg:
        hizas += 1
    elozotomeg = tomeg
print(f'A tömege {hizas} esetben nőtt egyik hétről a másikra.')