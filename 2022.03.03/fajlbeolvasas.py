def létezikE(filenév):
    try:
        f = open(filenév, 'r')
        f.close()
        return 1
    except:
        print('A fájl nem létezik')
        return 0
# --------------------------------------------------------

def primek12ig():
    # egy sor egy adat
    filename = "primek12ig.txt"
    if létezikE(filename):
        f = open(filename, 'r')
        primek = f.readlines()
        f.close()
        print(primek)
        for i in primek:
            i = i.strip('\n')
            print(i, end=" ")


def nemek():
    # egy sor tobb adat
    filename = "nemek.txt"
    if létezikE(filename):
        f = open(filename, 'r')
        beolvas = f.readline()
        f.close()
        nemek = beolvas[:-1].split(',')
        print(f'Az elemek száma: {len(nemek)} \nFérfiak száma: {nemek.count("f")} \nNők száma: {nemek.count("n")}  ')

# cipomeret,veletlenek,sorozat,negyzetek


def cipomeret():
    # egy sor tobb adat
    filename = "cipomeret.txt"
    if létezikE(filename):
        f = open(filename, 'r')
        beolvas = f.readline()
        f.close()
        meretek = beolvas[:-1].split(' ')
        ossz = 0
        for meret in meretek:
            ossz += int(meret)
        atlag = ossz / len(meretek)
        print(f'Cipőméretek átlaga: {atlag} \nLegnagyobb cipőméret: {max(meretek)} \nLegkisebb cipőméret: {min(meretek)}')

def veletlenek():
    pass 

def sorozat():
    pass

def negyzetek():
    pass



# --main--
# primek12ig()
# nemek()
# cipomeret()
veletlenek()
# sorozat()
# negyzetek()



