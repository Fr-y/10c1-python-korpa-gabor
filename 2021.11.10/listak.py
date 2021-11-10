#Írjon egy kis programot, ami egy új t3 listát hoz létre. Ennek felváltva kell tartalmazni 
#a két lista minden elemet úgy, hogy minden hónap nevét követnie kell a megfelelő 
#napok számának : ['Januar',31,'Februar',28,'Marcius',31, stb...].
def elso():
    t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    t2 = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június', 'Július',   'Augusztus', 'Szeptember', 'Október', 'November', 'December']
    t3 = []
    i = 0
    for item in t1:
        t3.append(t2[i])
        t3.append(t1[i])
        i += 1
    print(t3)

#Írjon egy programot, ami kiíratja egy lista összes elemét. Ha például a fenti gyakorlat 
#t2 listájára alkalmaznánk, akkor a következőt kellene kapnunk :
#Január Február Március Április Május Június Július Augusztus Szeptember Október 
#November December
def masodik():
    t1 = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június', 'Július',   'Augusztus', 'Szeptember', 'Október', 'November', 'December']
    for item in t1:
        print(item, end=" ")


#Írjon egy programot, ami megkeresi egy adott lista legnagyobb elemet. Például, ha a 
#[32, 5, 12, 8, 3, 75, 2, 15], listára alkalmaznánk, akkor a következőt kellene kiírnia: 
# a lista legnagyobb elemének az érteké 75.
def harmadik():
    t1 = [32, 5, 12, 8, 3, 75, 2, 15]
    print('a lista legnagyobb elemének az értéke', max(t1))


#Írjon egy programot, ami megvizsgálja egy számlista minden elemet (például az előző 
#példa listáját) azért, hogy két új listát hozzon létre. Az egyik csak az eredeti lista páros 
#számait tartalmazza, a másik a páratlanokat. Például, ha a kiindulási lista az előző 
#gyakorlat listája, akkor a programnak egy páros listát kell létrehoznia, ami a [32, 12, 8, 
#2] t tartalmazza es egy páratlan listát ami [5, 3, 75, 15] t tartalmazza. Trükk : 
#Gondoljon az előzőekben említett modulo (%) operátor használatára !
def negyedik():
    t1 = [32, 5, 12, 8, 3, 75, 2, 15]
    paratlan = []
    paros = []
    for item in t1:
        if item % 2 == 0:
            paros.append(item)
        else:
            paratlan.append(item)
    print(paratlan, paros)


#Írjon egy programot, ami egy szavakból álló lista elemeit egyenkent megvizsgálja
#azért, hogy két új listát hozzon létre. (például: ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 
#'JeanPierre','Sandra'] Az egyikben 6 karakternél rövidebb szavakat legyenek, a 
#másikban 6, vagy annál több karaktert tartalmazó szavak legyenek
def otodik():
    t1 = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'JeanPierre', 'Sandra']
    t2 = []
    t3 = []
    for item in t1:
        if len(item) < 6:
            t2.append(item)
        else:
            t3.append(item)
    print(t2, t3)



#elso()
#masodik()
#harmadik()
#negyedik()
otodik()