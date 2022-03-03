def létezikE(filenév):
    try:
        f = open(filenév, 'r')
        f.close()
        return 1
    except:
        return 0




    if létezikE(filenév):
        utasítások
    else:
        print(’A fájl nem létezik’)













# --main--
