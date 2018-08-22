"""
Time for some fake graphics! Let’s say we want to draw game boards that look
like this:
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes
(8x8 for chess, 19x19 for Go, and many more).
Ask the user what size game board they want to draw, and draw it for them to
the screen using Python’s print statement.
Remember that in Python 3, printing to the screen is accomplished by
  print("Thing to show on screen")
"""
# Function definition is here
def size():
    width = int(input("What's the width of game board?(max 41x41)"))
    length = int(input("What's the length of game board?(max 41x41)"))
    if ((length == 0 or width == 0) or (length < 0 or width < 0) or
        (length ==42 or width ==42)):
        print("Wrong numbers.")
    elif length == 1 and width == 1:
        print("1x1")
        print(" --- \n" + "|   |\n" + " --- ")
    elif length == 1 and width !=1:
        print(" --- ",end='')
        print("--- " * (width-1))
        print("|   |", end='')
        print("   |" * (width-1))
        print(" --- ",end='')
        print("--- " * (width-1))
    elif length !=1 and width == 1:
        for i in range(length):
            print(" --- ")
            print("|   |")
        print(" --- ")
    elif length !=1 and width != 1:
        for i in range(length):
            print(" --- ",end='')
            print("--- " * (width-1))
            print("|   |", end='')
            print("   |" * (width-1))
        print(" --- ",end='')
        print("--- " * (width-1))
size()
