#elso feladat
ut = input("Kérem a robot parancsait: ")

#szamolas
E, D, N, K = 0, 0, 0, 0
x, y = 0, 0
for lepes in ut:
    if lepes == 'E':
        y += 1
        E += 1
    elif lepes == 'D':
        y -= 1
        D += 1
    elif lepes == 'N':
        x -= 1
        N += 1
    elif lepes == 'K':
        x += 1
        K += 1

#feladat
print('E betűk száma:: ', E)
print('D betűk száma:: ', D)
print('N betűk száma:: ', N)
print('K betűk száma:: ', K)

#legrovidebb ut kiszamolasa
legrovidebb = ''
if x >= 0:
    legrovidebb += 'K' * x
else:
    legrovidebb += 'N' * abs(x)

if y >= 0:
    legrovidebb += 'E' * y
else:
    legrovidebb += 'D' * abs(y)

#harmadik feladat
print('Egy legrövidebb út parancsszava:', legrovidebb)