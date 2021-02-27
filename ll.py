import random

tries = 0
success = 0
successOnFirst = 0

nmbr = 5


while True:
    num = random.randint(1, 1000)

    tries += 1

    if num == nmbr:
        success += 1

        if tries == 1:

            successOnFirst += 1

        tries = 0

    if successOnFirst == 100:
        print("successOnFirst", successOnFirst)
        print("success", success)
        print("Percentage of getting number between  it on first is", successOnFirst/success*100, )
        break