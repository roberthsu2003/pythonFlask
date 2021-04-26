from random import randint

def getLot():
    '''
    產生8組1,49不重覆的亂數值,
    傳出tuple
    '''

    lot = set()
    while (len(lot) <= 7):
        lot.add(randint(1, 49))
    lotlist = list(lot)
    specialNum = lotlist.pop()
    return (lotlist, specialNum)