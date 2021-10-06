

a = int(input("Adj meg egy számot: "))
b = int(input("Adj meg mégegy számot: "))

if a > b:
    print(a, "nagyobb mint", b)
if a < b:
    print(b, "nagyobb mint", a)
if a == b:
    print("A két szám egyenlő")
# egyirányú  elágazás

if a > b:
    print(a, "nagyobb mint", b)
elif b > a:
    print(b, "nagyobb mint", a)
else:
    print("A két szám egyenlő")

#többirányú
if a != b:
    print(max(a,b), "nagyobb, mint", min(a,b))
else:
    print("a két szám egyenlő")