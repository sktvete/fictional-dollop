import random
import time

lstLower = [100]
lstHigher = [0]

guess = 0
#inp = int(input("Your number? "))
inp = random.randint(1, 100) # max(lstLower)
print("Your number is", inp) # min(lstLower)

while True:

    guess = ((min(lstLower) + max(lstHigher))/2)

    time.sleep(1)
    if guess < inp:
        lstHigher.append(guess)
    elif guess < inp:
        lstLower.append(guess)




