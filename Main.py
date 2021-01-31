import random
import time


def blackjack():
    total = 0
    dealertotal = 0
    penger = 100

    kort = random.randint(1, 13)
    print("Du fikk", kort)
    total += kort

    kort = random.randint(1, 13)
    print("Du fikk", kort)
    total += kort

    print("Total =", total)

    while total < 21:
        inp = input("Vil du trekke nytt? y/n ")
        if inp == "n":
            break
        kort = random.randint(1, 13)
        print("Du fikk", kort)
        total += kort
        print("Total =", total)

    if total > 21:
        print("Du tapte")

    else:
        while dealertotal < 17:
            time.sleep(1)
            kort = random.randint(1, 13)
            print("Dealer trakk", kort)
            dealertotal += kort
            print(dealertotal)

        if dealertotal > 21 or total > dealertotal:
            print("Du vant!")
        elif total == dealertotal:
            print("Likt")
        else:
            print("Du tapte:\(")


while True:
    blackjack()
    time.sleep(1)
    print("\n"*2)










