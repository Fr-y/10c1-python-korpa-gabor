"""#11. Írasd ki a számokat -30 és 30 között ötösével (-30, -25, -20…)! 
i = -30
while i<31:
    print(i, end=" ")
    i+=5"""

"""#12. Írasd ki a 3 első tizenhét többszörösét! (3, 6, 9..) 
i = 1
while i<18:
    print(3*i, end=" ")  
    i+=1"""

"""#13. Írasd ki 2 első tizenhat pozitív egész kitevőjű hatványát (2, 4, 8, 16, 32,…) 14.
i = 1
while i<17:
    print(pow(2, i), end=" ")
    i += 1  
"""

"""#14. Írasd ki a 7-es szorzótábla első 25 eleméből azokat, amik 4-gyel oszthatók. 
i = 1
while i<26:
    n = i * 7
    if n % 4 == 0:
        print(n, end=" ")
    i += 1
"""


"""#15. Írasd ki a 144 osztóit! 
i = 1
while i<145:
    if 144 % i == 0:
        print(i, end=" ")
    i+=1"""

"""#16. Írj programot, mely beolvas egy pozitív egész számot, és kiírja az osztóit! 
n = int(input())
i = 1
while i<n+1:
    if n % i == 0:
        print(i, end=" ")
    i += 1"""

"""#17. Írj programot, mely beolvas egy pozitív egész számot, és kiírja az osztóinak az összegét!
n = int(input())
i = 1
ossz = 0
while i<n+1:
    if n % i == 0:
        ossz += i
    i += 1
print(ossz)"""


"""#18. Írasd ki azokat a kétjegyű számokat, amelyek számjegyeinek összege 10 (19 28 37 ...)
i = 10
while i<100:
    tizes = int(i / 10) #megkapjuk a tizesek helyen álló számot
    egyes = i - tizes * 10 #megkapjuk az egyesek helyén álló számot
    if tizes + egyes == 10: #ha a számjegyek összege 10
        print(i, end=" ")
    i += 1"""


"""#19. Írasd ki azokat a számpárokat, amelyek összege 18 (1 -17, 2 -16, …) 
n1 = 1
n2 = 17
while n1<51: #nemtudom meddig kell szoval 50ig
    print('|', n1, '-', n2, '|')
    n1 +=1
    n2 -=1"""

"""
#20. Írasd ki a nyolcas szorzótábla első tíz tagját egymás mellé! 

i = 1
while i<11:
    n = i * 8
    print(n, end=" ")
    i += 1"""