"""#1. Írasd ki a számokat 1-től 20-ig!

#a. egymás mellé 
for i in range(1, 21):
    print(i, end=" ")

print('')

#b. egymás alá
for i in range(1, 21):
    print(i)


"""

"""#2. Írasd ki a számokat ciklussal 15-92-ig egymás mellé!

for i in range(15, 93):
    print(i, end=" ")"""

"""#3. Írasd ki a páros számokat 1 és 30 között!

#a. egymás mellé
for i in range(1,31):
    if i%2 == 0:
        print(i, end=" ")

print('')

#b. egymás alá    
for i in range(1,31):
    if i%2 == 0:
        print(i)"""

"""#4. Írj programot, mely beolvas egy pozitív egész számot, és kiírja az egész számokat a 
#képernyőre eddig a számig, egymástól szóközzel elválasztva!

a = int(input("Adj meg egy egész számot"))
for i in range(a+1):
    print(i, end=" ")"""

"""#5. Írj programot, mely beolvas egy pozitív egész számot, és kiírja az egész számokat egymás 
#alá a képernyőre eddig a számig!

a = int(input("Adj meg egy egész számot"))
for i in range(a+1):
    print(i)"""

"""#6.Írasd ki az első tizenöt szám négyzetét!

for i in range(1, 16):
    print(i * i, end=" ")"""

"""#7.Írasd ki a 4-el osztható számokat 100 és 400 között

for i in range(100, 401):
    if i%4 == 0:
        print(i, end=" ")  """

"""#8.Írasd ki a számokat 30 és 100 között kilencesével (30, 39, 48…)

for i in range(30, 101, 9):
    print(i)"""

"""#9.Írasd ki a számokat 150 és 40 között tizenkettesével lefelé (150, 138, 126…)!

for i in range(150, 40, -12):
    print(i)
"""

"""#10.Írasd ki 100-tól visszafelé -100-ig a kilenccel osztható számokat
for i in range(100, -101, -1):
    if i%9 == 0:
        print(i)
"""