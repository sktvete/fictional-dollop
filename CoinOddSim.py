from random import randint as random
whiles = 0

head = 0
heads = 0
doubleHeads = 0

coind = 0

tail= 0
tails = 0
doubleTails = 0

while True:
    coin = random(1, 2)
    whiles += 1

    if coin == 1:
        head += 1
        coind = coin
        tails = 0
        if coind == 1:
            heads += 1


    if coin == 2:
        tail += 1
        coind = coin
        heads = 0
        if coind == 2:
            tails += 1


    if heads == 2:
        doubleHeads += 1

    if whiles == 100000:
        print("throwes =", whiles)
        print("heads", head)
        print("doubleHeads", doubleHeads)
        break
