

#TictacToe

import time
import random

#TicTacToe

def board(): #Print board
    print\
    (f"""  
    {one}|{two}|{three}
    -----
    {four}|{five}|{six}
    -----
    {seven}|{eight}|{nine}
    """)

moved = False
game = True


one = " "
two = " "
three = " "
four = " "
five = " "
six = " "
seven = " "
eight = " "
nine = " "


while game == True:
    moved = False
    while not moved:
        inp = input("which square? (1-9)")

        if inp == "1" and one != "X" and one != "O":
            one = "X"
            board()
            moved = True
        elif inp == "2" and two != "X" and two != "O":
            two = "X"
            board()
            moved = True
        elif inp == "3" and three != "X" and three != "O":
            three = "X"
            board()
            moved = True
        elif inp == "4" and four != "X" and four != "O":
            four = "X"
            board()
            moved = True
        elif inp == "5" and five != "X" and five != "O":
            five = "X"
            board()
            moved = True
        elif inp == "6" and six != "X" and six != "O":
            six = "X"
            board()
            moved = True
        elif inp == "7" and seven != "X" and seven != "O":
            seven = "X"
            board()
            moved = True
        elif inp == "8" and eight != "X" and eight != "O":
            eight = "X"
            board()
            moved = True
        elif inp == "9" and nine != "X" and nine != "O":
            nine = "X"
            board()
            moved = True
        else:
            print("This is not possible, changes have not been made")
            board()

        print("You made your move")
    moved = False

    while moved == False: #ROBOTS TURN
        inp = input("which square? (1-9)")
        print(inp)

        if inp == "1" and one != "X" and one != "O":
            one = "O"
            board()
            moved = True
        elif inp == "2" and two != "X" and two != "O":
            two = "O"
            board()
            moved = True
        elif inp == "3" and three != "X" and three != "O":
            three = "O"
            board()
            moved = True
        elif inp == "4" and four != "X" and four != "O":
            four = "O"
            board()
            moved = True
        elif inp == "5" and five != "X" and five != "O":
            five = "O"
            board()
            moved = True
        elif inp == "6" and six != "X" and six != "O":
            six = "O"
            board()
            moved = True
        elif inp == "7" and seven != "X" and seven != "O":
            seven = "O"
            board()
            moved = True
        elif inp == "8" and eight != "X" and eight != "O":
            eight = "O"
            board()
            moved = True
        elif inp == "9" and nine != "X" and nine != "O":
            nine = "O"
            board()
            moved = True
        else:
            print(inp, "Not possible")
            board()

    if one != " " and two != " " and three != " " and four != " " and five != " " and six != " " and seven != " " and eight != " " and nine != " ":
        print("Equal")
    print("move is made")




