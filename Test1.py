

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
lst1 = []
lst2 = []

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
        inp = input("which square? (1-9) ")

        if inp == "1" and one != "X" and one != "O":
            one = "X"
            board()
            lst1.append(inp)
            moved = True
        elif inp == "lst":
            print(lst1, "\n", lst2)
        elif inp == "2" and two != "X" and two != "O":
            two = "X"
            board()
            lst1.append(inp)
            moved = True
        elif inp == "3" and three != "X" and three != "O":
            three = "X"
            board()
            lst1.append(inp)
            moved = True
        elif inp == "4" and four != "X" and four != "O":
            four = "X"
            board()
            lst1.append(inp)
            moved = True
        elif inp == "5" and five != "X" and five != "O":
            five = "X"
            board()
            lst1.append(inp)
            moved = True
        elif inp == "6" and six != "X" and six != "O":
            six = "X"
            board()
            lst1.append(inp)
            moved = True
        elif inp == "7" and seven != "X" and seven != "O":
            seven = "X"
            board()
            lst1.append(inp)
            moved = True
        elif inp == "8" and eight != "X" and eight != "O":
            eight = "X"
            board()
            lst1.append(inp)
            moved = True
        elif inp == "9" and nine != "X" and nine != "O":
            nine = "X"
            board()
            lst1.append(inp)
            moved = True
        else:
            print("This is not possible, changes have not been made")
            board()

        print("You made your move")
        if ("1" and "2" and "3") in lst1:
            print("Player X won!")
            print("123")
            print(lst1)
        elif "4" and "5" and "6" in lst1:
            print("Player X won!")
            print("456")
        elif "7" and "8" and "9" in lst1:
            print("789")
            print("Player X won!")
        elif "1" and "4" and "7" in lst1:
            print("147")
            print("Player X won!")
        elif "2" and "5" and "8" in lst1:
            print("Player X won!")
            print("258")
        elif "3" and "6" and "9" in lst1:
            print("Player X won!")
        elif "1" and "5" and "9" in lst1:
            print("Player X won!")
        elif "3" and "5" and "7" in lst1:
            print("Player X won!")


    moved = False  #winning numbers 123 456 789 147 258 369 159 357

    if one != " " and two != " " and three != " " and four != " " and five != " " and six != " " and seven != " " and eight != " ":
        print("Equal")

    while moved == False: #ROBOTS TURN
        inp = input("which square? (1-9) ")
        print(inp)

        if inp == "1" and one != "X" and one != "O":
            one = "O"
            board()
            lst2.append(inp)
            moved = True
        elif inp == "2" and two != "X" and two != "O":
            two = "O"
            board()
            lst2.append(inp)
            moved = True
        elif inp == "3" and three != "X" and three != "O":
            three = "O"
            board()
            lst2.append(inp)
            moved = True
        elif inp == "4" and four != "X" and four != "O":
            four = "O"
            board()
            lst2.append(inp)
            moved = True
        elif inp == "5" and five != "X" and five != "O":
            five = "O"
            board()
            lst2.append(inp)
            moved = True
        elif inp == "6" and six != "X" and six != "O":
            six = "O"
            board()
            lst2.append(inp)
            moved = True
        elif inp == "7" and seven != "X" and seven != "O":
            seven = "O"
            board()
            lst2.append(inp)
            moved = True
        elif inp == "8" and eight != "X" and eight != "O":
            eight = "O"
            board()
            lst2.append(inp)
            moved = True
        elif inp == "9" and nine != "X" and nine != "O":
            nine = "O"
            board()
            lst2.append(inp)
            moved = True
        else:
            print(inp, "Not possible")
            board()

        if "1" and "2" and "3" in lst2:
            print("Player O won!")
        elif "4" and "5" and "6" in lst2:
            print("Player O won!")
        elif "7" and "8" and "9" in lst2:
            print("Player O won!")
        elif "1" and "4" and "7" in lst2:
            print("Player O won!")
        elif "2" and "5" and "8" in lst2:
            print("Player O won!")
        elif "3" and "6" and "9" in lst2:
            print("Player O won!")
        elif "1" and "5" and "9" in lst2:
            print("Player O won!")
        elif "3" and "5" and "7" in lst2:
            print("Player O won!")

    print("move is made")





