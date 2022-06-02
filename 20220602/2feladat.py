from random import randint
szamok = []
for i in range(50):
    szamok.append(randint(10, 100))

def prime(szam):
    osztok = 0
    for i in range(1, szam+1):
        if szam % i == 0:
            osztok += 1
    if osztok == 2:
        return True
    else:
        return False

primszamok = []
osszetettszamok = []

def primek(szamok):
    for szam in szamok:
        if prime(szam):
            primszamok.append(szam)
        else:
            osszetettszamok.append(szam)
        
primek(szamok)

print("Prímek:")
for szam in primszamok:
    print(szam, end=', ')
print("\nÖsszetett számok:")
for szam in osszetettszamok:
    print(szam, end=', ')