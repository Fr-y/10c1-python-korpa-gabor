'''
1.
Írjon egy scriptet, ami lehetővé teszi egy szövegfile kényelmes olvasását.
A program először kérje a felhasználótól a file nevét. Ezután ajánlja föl a
következő választást : vagy új szövegsorokat rögzít, vagy kiírja a file
tartalmát. A felhasználónak be kell tudnia írni az egymást követő
szövegsorokat, az <Enter>-t használva a sorok elválasztására. A beírás
befejezéseként elég egy üres sort bevinni (vagyis elég magában megnyomni az
<Enter> t) A tartalom kiírásakor a soroknak természetes módon kell egymás
után következni (a sorvége kódoknak nem kell megjelenni).
'''

def elso():

    #fajlnev (jelenesetben 'szoveg')
    fn = input()
    #valasztas
    choice = int(input("Szövegsorok rögzitése (1) | File tartalmának kiírása (2) \n"))

    if choice == 1:
        while input() != '':
            #ha filenotfound error van nemjo mappaba teccik lenni
            file = open(f"{fn}.txt", 'a')
            nc = input()
            file.write(f'{nc}\n')
            file.close
    elif choice == 2:
        file = open(f"{fn}.txt", 'r')
        print(file.read())
    else:
        print("Légyszives a két opció közül válassz")


'''
2.
Tegyük fel, hogy rendelkezésére áll egy szövegfile, ami különböző hosszúságú
mondatokat tartalmaz. Írjon egy scriptet, ami megkeresi és kiírja a
leghosszabb mondatot.
'''

def masodik():
    file = open("szoveg2.txt", "r")
    #mondatokra osztas
    mondatok = file.read().splitlines()
    #leghoszabb mondat
    print(max(mondatok, key = len))


'''
3.
Írjon egy scriptet, ami automatikusan létrehoz egy szövegfilet, ami a
2 – 30 as szorzótáblákat tartalmazza (20-20 tagot tartalmazzon).
'''

def harmadik():
    f = open("szorzotablak.txt", "x")

    for x in range(2, 31):
        for n in range(1, 21):
             f.write(f'{x * n}, ')
        f.write('\n')



'''
4.
Írjon egy scriptet, ami úgy másol át egy filet, hogy a szavak között
megháromszorozza a szóközök számát.
'''

def negyedik():
    f = open("szoveg3.txt", "r")
    string = f.read()
    haromszor = ''
    for character in string:
        if character == ' ':
            haromszor += character * 3
        else:
            haromszor += character
    fmasolat = open("szoveg3masolat.txt", "x")
    fmasolat.write(haromszor)



'''
5.
Rendelkezésére áll egy szövegfile, aminek minden sora egy valós típusú
numerikus érték reprezentációja (exponens nincs). Például:
14.896
7894.6
123.278 stb.
Írjon egy scriptet, ami ezeket az értékeket egész számra kerekítve egy másik
fileba másolja (a kerekítésnek korrektnek kell lenni)
'''

def otodik():
    f = open("szamok.txt", "r")
    szamok = f.read().splitlines()
    kerekitett = []
    for szam in szamok:
        kerekitett.append(round(float(szam)))
    fkerek = open("szamokkerekitett.txt", "x")
    for szam in kerekitett:
        fkerek.write(f'{str(szam)} \n')
    

'''
6.
Írjon egy scriptet, ami összehasonlítja két file tartalmát és jelzi az első
eltérést.
'''

def hatodik():
    f = open("szoveg2.txt", "r")
    f2 = open("szoveg3.txt", "r")

    z = zip(f, f2)

    for tuple in z:
        for word in tuple[0]:
            print(tuple)
            if word[0] == word[1]:
                print("asd")



'''
7.
Az A és B már létező fileokból konstruáljon egy harmadik C filet, ami
felváltva tartalmaz egyegy elemet az A illetve B fileból. Amikor elérte az
egyik eredeti file végét, akkor egészítse ki a C filet a másik file maradék
elemeivel.
'''

# def hetedik():
#     print(asd)

# -- meghivások --
#elso()
#masodik()
#harmadik()
#negyedik()
#otodik()
hatodik()