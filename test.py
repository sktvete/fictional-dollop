import random
import time

listLower = [100]
listHigher = [0]

guess = 0
#inp = int(input("Your number? "))
inp = random.randint(1, 100)
print("Your number is", inp)
time.sleep(1)



while True:
    guess =