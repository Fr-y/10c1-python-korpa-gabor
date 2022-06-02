class Valtozas:
    def __init__(self, sor):
        darabok=sor.strip('\n').split(';')
        datum=darabok[0].split('.')
        self.ev=int(datum[0])
        self.honap=int(datum[1])
        self.nap=int(datum[2])
        self.benzinar=int(darabok[1])
        self.gazolajar=int(darabok[2])