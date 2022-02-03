from pyautogui import *

def szamitas():


    router = int(prompt(text="Egy router ára: ")) * int(prompt(text="A routerek száma: "))
    laptop = int(prompt(text="Egy laptop ára: ")) * int(prompt(text="A laptopok száma: "))
    szerver = int(prompt(text="Egy szerver ára: ")) * int(prompt(text="A szerverek száma: "))
    pc = int(prompt(text="Egy pc ára: ")) * int(prompt(text="A pc-k száma: "))
    mobil = int(prompt(text="Egy mobil ára: ")) * int(prompt(text="A mobilok száma: "))
    nyomtato = int(prompt(text="Egy nyomtató ára: ")) * int(prompt(text="A nyomtatók száma: "))

    osszertek = router + laptop + szerver + pc + mobil + nyomtato
    alert(text=f"Az eszközök összege: {osszertek}")



szamitas()