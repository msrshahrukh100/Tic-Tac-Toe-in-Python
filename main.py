
def print_board(board):
	print(
		f'''
			_{board[0]}_|_{board[1]}_|_{board[2]}_
			_{board[3]}_|_{board[4]}_|_{board[5]}_
			 {board[6]} | {board[7]} | {board[8]}

		'''
	)

def is_move_valid(move, board):
	'''
		Receives the move and the board and returns
		validity, valid move and the message
	'''

	if not move.isnumeric():
		return False, None, "Value should be numeric"

	move = int(move)

	if move not in range(9):
		return False, None, "Value should be between 0 to 8"

	elif board[move] in ["X", "O"]:
		return False, None, "The place is already taken"

	return True, move, "Boad is valid"

def is_game_over(board):
	WAYS_TO_WIN = (
		(0, 1, 2),
		(3, 4, 5),
		(6, 7, 8),
		(0, 3, 6),
		(1, 4, 7),
		(2, 5, 8),
		(0, 4, 8),
		(2, 4, 6)
	)

	for row in WAYS_TO_WIN:
		if board[row[0]] == board[row[1]] == board[row[2]]:
			return True, board[row[0]]

	for i in board:
		if i not in ["X", "O"]:
			return False, None

	return True, None

def main():
	board = [f"{i}" for i in range(9)]
	print_board(board)

	game_over, winner = False, None
	turn = "X"

	while not game_over:
		move = input(f"It's {turn}'s turn. Where will you move? ")

		is_valid, valid_move, msg = is_move_valid(move, board)
		if is_valid:
			board[valid_move] = turn
			turn = "X" if turn == "O" else "O"
		else:
			print(msg)
			continue

		game_over, winner = is_game_over(board)
		if game_over and winner:
			print(f"The winner is {winner}")
		elif game_over:
			print("There's no winner it's a draw")

		print_board(board)


if __name__ == "__main__":
	main()