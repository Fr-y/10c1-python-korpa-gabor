def szamitas():

    router = int(input("Egy router ára: ")) * int(input("A routerek száma: "))
    laptop = int(input("Egy laptop ára: ")) * int(input("A laptopok száma: "))
    szerver = int(input("Egy szerver ára: ")) * int(input("A szerverek száma: "))
    pc = int(input("Egy pc ára: ")) * int(input("A pc-k száma: "))
    mobil = int(input("Egy mobil ára: ")) * int(input("A mobilok száma: "))
    nyomtato = int(input("Egy nyomtató ára: ")) * int(input("A nyomtatók száma: "))

    osszertek = router + laptop + szerver + pc + mobil + nyomtato
    print(osszertek, "Ft")


szamitas()