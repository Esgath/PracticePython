"""
In a previous exercise we explored the idea of using a list of lists as a
“data structure” to store information about a tic tac toe game. In a tic tac
toe game, the “game server” needs to know where the Xs and Os are in the
board, to know whether player 1 or player 2 (or whoever is X and O won).
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


def draw_xo():
	"""Ask user for coordinates and draws 'X' or 'O' on the board"""

	# Show gameboard:
	print(str(game[0])+'\n'+str(game[1])+'\n'+str(game[2]))

	validInput = True
	while validInput == True:
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
		print(str(game[0])+'\n'+str(game[1])+'\n'+str(game[2]))

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
		print(str(game[0])+'\n'+str(game[1])+'\n'+str(game[2]))

draw_xo()
