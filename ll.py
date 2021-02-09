import random
nmbr = 5
tries = 0
success = 0
successOnFirst = 0


while True:
    num = random.randint(1, 100)
    print(num)
    tries += 1

    if num == nmbr and tries == 1:
        print("Finally guessed", nmbr, "on the first try after", success, "tries")
        successOnFirst += 1


    if num == nmbr:
        success += 1
        print("Guessed in", tries + 1, "tries")
        tries = 0

    if successOnFirst == 10000:
        print("successOnFirst", successOnFirst)
        print("success", success)
        print("Percentage of getting it on first is", successOnFirst/success*100, )
        break