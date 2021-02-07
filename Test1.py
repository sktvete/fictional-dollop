

#TictacToe

import time
import random



def board(): #Print board
    print\
    (f"""  
    {one}|{two}|{three}
    -----
    {four}|{five}|{six}
    -----
    {seven}|{eight}|{nine}
    """)

one = " "
two = " "
three = " "
four = " "
five = " "
six = " "
seven = " "
eight = " "
nine = " "

#XorOisTaken
while True:
    inp = input("which square? (1-9)")

    if inp == "1" and one != "X" and one != "O":
        one = "X"
        board()
    elif inp == "2" and two != "X" and one != "O":
        two = "X"
        board()
    elif inp == "3" and three != "X" and one != "O":
        three = "X"
        board()
    elif inp == "4" and four != "X" and one != "O":
        four = "X"
        board()
    elif inp == "5" and five != "X" and one != "O":
        five = "X"
        board()
    elif inp == "6" and six != "X" and one != "O":
        six = "X"
        board()
    elif inp == "7" and seven != "X" and one != "O":
        seven = "X"
        board()
    elif inp == "8" and eight != "X" and one != "O":
        eight = "X"
        board()
    elif inp == "9" and nine != "X" and one != "O":
        nine = "X"
        board()
    else:
        print("This is taken, changes have not been made")
        board()


board()




