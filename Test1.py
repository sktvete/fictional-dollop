

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

inp = input("which square? (1-9)")
if inp == "1":
    one = "X"
elif inp == "2":
    two = "X"
elif inp == "3":
    three = "X"
elif inp == "4":
    four = "X"
elif inp == "5":
    five = "X"
elif inp == "6":
    six = "X"
elif inp == "7":
    seven = "X"
elif inp == "8":
    eight = "X"
elif inp == "9":
    nine = "X"


board()




