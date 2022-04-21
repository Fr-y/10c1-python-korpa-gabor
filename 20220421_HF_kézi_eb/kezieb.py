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
        self.csapat = egysor[9]


with open('kezieb.txt', 'r') as f:
    beolvas = f.readlines()

jatekosok = []
for i in range(len(beolvas)):
    jatekosok.append(Jatekos(beolvas[i]))

print(jatekosok[0].nev)