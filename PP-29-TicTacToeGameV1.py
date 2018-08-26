"""
In 3 previous exercises, we built up a few components needed to build a Tic Tac
Toe game in Python:
    Draw the Tic Tac Toe game board
    Checking whether a game board has a winner
    Handle a player move from user input
The next step is to put all these three components together to make a two-player
 Tic Tac Toe game! Your challenge in this exercise is to use the functions from
 those previous exercises all together in the same program to make a two-player
 game that you can play with a friend. There are a lot of choices you will have
 to make when completing this exercise, so you can go as far or as little as you
  want with it.
"""
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def check_board():
    """Keeps track of free space and stops game when board is full"""
    count = 0
    for i in range(3):
        if game[0][i] == 0:
            count += 1
        if game[1][i] == 0:
            count += 1
        if game[2][i] == 0:
            count += 1
    return count


def winner(game):
    """Defines the winner"""
    # Rows
    for i in range(3):
        row = set(game[i])
        if len(row) == 1 and game[i][0] != 0:
            if game[i][i] == 'X':
                return "Player number 1 wins"
            elif game[i][i] == 'O':
                return "Player number 2 wins"
    # Columns
    for i in range(3):
        column = set([game[0][i], game[1][i], game[2][i]])
        if len(column) == 1 and game[0][i] != 0:
            if game[0][i] == 'X':
                return "Player number 1 wins"
            elif game[0][i] == 'O':
                return "Player number 2 wins"

    # Diagonals
    diag1 = set([game[0][0], game[1][1], game[2][2]])
    diag2 = set([game[0][2], game[1][1], game[2][0]])
    if len(diag1) == 1 and game[0][0] != 0:
        if game[0][0] == 'X':
            return "Player number 1 wins"
        elif game[0][0] == 'O':
            return "Player number 2 wins"
    elif len(diag2) == 1 and game[0][2] != 0:
        if game[0][2] == 'X':
            return "Player number 1 wins"
        elif game[0][2] == 'O':
            return "Player number 2 wins"
    else:
        return("Playing...\n")


def draw_xo():
    """Ask user for coordinates and draws 'X' or 'O' on the board"""

    # Show gameboard:
    print(str(game[0])+'\n'+str(game[1])+'\n'+str(game[2])+'\n')

    validInput = True
    while validInput == True:
        # When winner is found breaks the loop
        print(winner(game))
        if (winner(game) == "Player number 1 wins" or
                winner(game) == "Player number 2 wins"):
            break
        # Keeps track of space on the game board:
        if check_board() == 0:
            print("No more space to play the game.")
            break


        print("Free space: " + str(check_board()))
        # User number 1:
        user = input("Player one: Please input coordinates(in form row,column): ")
        user = user.split(",")
        user_row = int(user[0])
        user_column = int(user[1])
        if game[user_row-1][user_column-1] == 0:
            game[user_row-1][user_column-1] = 'X'
        elif game[user_row-1][user_column-1] != 0:
            print("This coordinate is already taken. Try again.")
            continue

        # Show gameboard:
        print(str(game[0])+'\n'+str(game[1])+'\n'+str(game[2])+'\n')
        # When winner is found breaks the loop
        print(winner(game))
        if (winner(game) == "Player number 1 wins" or
                winner(game) == "Player number 2 wins"):
            break
        # Keeps track of space on the game board:
        if check_board() == 0:
            print("No more space to play the game.")
            break


        # User number 2:
        user2Input = True
        while user2Input == True:
            print("Free space: " + str(check_board()))
            user2 = input("Player two: Please input coordinates(in form row,column): ")
            user2 = user2.split(",")
            user2_row = int(user2[0])
            user2_column = int(user2[1])
            if game[user2_row-1][user2_column-1] == 0:
                game[user2_row-1][user2_column-1] = 'O'
                user2Input = False
            elif game[user2_row-1][user2_column-1] != 0:
                print("This coordinate is already taken. Try again.")
                continue

        # Show gameboard:
        print(str(game[0])+'\n'+str(game[1])+'\n'+str(game[2])+'\n')

    print("Congratulations.")
draw_xo()
