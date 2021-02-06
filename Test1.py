

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




board()




