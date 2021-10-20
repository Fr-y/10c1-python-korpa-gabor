#1.
def elso():
    a = int(input('Adj meg egy számot: '))
    print(3 * a)


#2.
def masodik():
    a = float(input('Add meg a háromszög oldalát: '))
    m = float(input('Add meg a magasságot: '))
    T = (a * m) / 2
    print(T)


#3.
def harmadik():
    a = int(input('Adj meg egy számot: '))
    if a % 5 == 0:
        print('osztható')


#4.
def negyedik():
    a = int(input('Adj meg egy számot: '))
    if -50 < a and a < 20:
        print('A szám -50 és 20 között van')
    else:
        print('A szám nincs -50 és 20 között')


#5.
def otodik():
    i = 1
    while i<21:
        print(pow(i, 2), end=" ")
        i += 1


#6.
def hatodik():
    i = 1
    while i < 21:
        if i % 3 == 2:
            print(i, end=" ")
        i += 1


#7.
def hetedik():
    i = 1
    while i < 25:
        if i * 9 % 4 == 0:
            print(i * 9, end=" ")
        i += 1


#elso()
#masodik()
#harmadik()
#negyedik()
#otodik()
#hatodik()
#hetedik()