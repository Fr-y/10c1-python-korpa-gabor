def feladat1():
    n = int(input("Adj meg egy valós számot: "))
    print("A szám háromszorosa:", n*3)



def feladat2():
    a = int(input("Add meg a háromszög oldalát: ")) 
    m = int(input("Add meg a háromszög magasságát: "))
    T = (a*m) / 2
    print("A háromszög területe:", T)



def feladat3():
    n = int(input("Adj meg egy számot: "))
    if n % 5 == 0:
        print("A megadott szám osztható öttel")
    else:
        print("A megadott szám nem osztható öttel")



def feladat4():
    n = int(input("Adj meg egy számot: "))
    if -50 < n < 20:
        print("A megadott szám -50 és 20 között van")
    else:
        print("A megadott szám nincs -50 és 20 között")



def feladat5():
    for i in range(1,21):
        print(i*i, end=" ")



def feladat6():
    for i in range(1,21):
        if i % 3 == 2:
            print(i, end=" ")



def feladat7():
    for i in range(1,26):
        sz = 9*i
        if sz % 4 == 0:
            print(sz, end=" ")





# -- hívások --
feladat1()
# feladat2()
# feladat3()
# feladat4()
# feladat5()
# feladat6()
# feladat7()