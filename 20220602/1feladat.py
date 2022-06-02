szoveg = input()
maganhangzok = "aáeéuúüűoöőií"

szamlalo = 0
nagybetu = False
for char in szoveg:
    if char.isupper(): nagybetu = True
    if char.lower() in maganhangzok:
        szamlalo += 1

print('A szövegben előforduló magánhangzók száma:', szamlalo)
if nagybetu:
    print('A szövegben van nagybetű.')
else:
    print('A szövegben nincs nagybetű.')