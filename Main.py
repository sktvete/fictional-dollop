import random
import time



def blackjack():
    total = 0
    dealertotal = 0
    again = "y"
    bet = 0


    kort = random.randint(1, 11)
    print("You got", kort)
    total += kort

    kort = random.randint(1, 11)
    print("You got", kort)
    total += kort

    print("Total =", total)

    while total < 21:
        inp = input("Do you want a new card? y/n ")
        if inp == "n":
            print("\n"*4 + "Dealers turn")
            break
        kort = random.randint(1, 11)
        print("You got", kort)
        total += kort
        print("Total =", total)

    if total > 21:
        print("You lost")

    else:
        while dealertotal < 17: #DEALER
            time.sleep(1)
            kort = random.randint(1, 10)
            print("Dealer got", kort)
            dealertotal += kort

        if dealertotal > 21 or total > dealertotal:
            print("Dealer ended up with", dealertotal)
            print("You won")
            return "vant"
        elif total == dealertotal:
            print("Dealer ended up with", dealertotal)
            print("Equal")
            return "likt"
        else:
            print("Dealer ended up with", dealertotal)
            print("You lost:(")
    return "tapt"


penger = 100
bet = 0

playedbefore = False

while True:
    again = input("Do you want to play a game of Blackjack? y/n ")
    if again == "y":
        print("You have",penger,"dollars left")
        bet = int(input("How much do you want to bet? "))
        while penger-bet < 0:
            bet = int(input("How much do you want to bet? "))
        penger = penger - bet
        print(penger)
        resultat = blackjack()
        if resultat == "vant":
            penger += bet * 2
        elif resultat == "likt":
            penger += bet
        print("You have", penger, "dollars left")
        time.sleep(1)
        print("\n" * 2)
    elif again == "n":
        break













