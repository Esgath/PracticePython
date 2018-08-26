"""
Your task this week: given a 3 by 3 list of lists that represents a Tic Tac
Toe game board, tell me whether anyone has won, and tell me which player won,
if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a
diagonal. Don’t worry about the case where TWO people have won -
assume that in every board there will only be one winner.
"""
game = [[1, 2, 0],
	    [2, 1, 0],			    	# winner_is_1
	    [2, 1, 1]]

game2 = [[2, 2, 0],                 # winner_is_2
	     [2, 1, 0],
	     [2, 1, 1]]

game3 = [[1, 2, 0],                 # winner_is_1
        [2, 1, 0],
        [2, 1, 1]]

game4 = [[0, 1, 0],                 # winner_is_also_1
        [2, 1, 0],
        [2, 1, 1]]

game5 = [[1, 2, 0],                 # no_winner
        [2, 1, 0],
        [2, 1, 2]]

game6 = [[1, 2, 0],                #  no_winner
        [2, 1, 0],
        [2, 1, 0]]


def winner(game):
	# Rows
	for i in range(len(game)):
		row = set(game[i])
		if len(row) == 1 and game[i][0] != 0:
			return "Player number {} wins".format(game[i][i])

	# Columns
	for i in range(len(game)):
		column = set([game[0][i], game[1][i], game[2][i]])
		if len(column) == 1 and game[0][i] != 0:
			return "Player number {} wins".format(game[0][i])

	# Diagonals
	diag1 = set([game[0][0], game[1][1], game[2][2]])
	diag2 = set([game[0][2], game[1][1], game[2][0]])
	if len(diag1) == 1 and game[0][0] != 0:
		return "Player number {} wins.".format(game[0][0])
	elif len(diag2) == 1 and game[0][2] != 0:
		return "Player number {} wins.".format(game[0][2])

	return "It's a draw"


print(winner(game))
print(winner(game2))
print(winner(game3))
print(winner(game4))
print(winner(game5))
print(winner(game6))
