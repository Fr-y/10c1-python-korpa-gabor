"""Írj programot, mely beolvas két pozitív egész számot, és kiírja a számtani és mértani 
közepüket! A gyökvonáshoz használd a beépített gyökfüggvényt!"""

from math import *

a = int(input("Adj meg egy pozitiv egesz szamot:"))
b = int(input("Adj meg egy pozitiv egesz szamot:"))

#számtani közép
szk = (a + b) / 2
print('Számtani közepük:', szk)

#mértani közép
mk = sqrt(a * b)
print('Mértani közepük:', mk)