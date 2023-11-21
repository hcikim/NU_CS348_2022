# Student Name: Taewook Kim

QUEENS = 10

def get_rows(board):

	q_rows = []
	queens = []

	row = len(board)
	col = len(board[0])

	for j in range(col):
		for i in range(row):
			if board[i][j] == 1:
				q_rows.append(i)

	for i in range(len(q_rows)):
		queens.append((q_rows[i], i))

	return q_rows, queens


def attack(board):
	
	attacks = 0

	queen_rows, queens_rc = get_rows(board)
	col = len(board[0])
	del queen_rows

	for queen in queens_rc:

		# row attack
		for i in range(col):
			if board[queen[0]][i] == 1 and (queen[0], i) != queen:
				attacks += 1

		# pos_diag
		for i in range(col):
			pos_diag = queen[0] - queen[1] + i # row - col
			if 0 <= pos_diag and pos_diag < col:
				if board[pos_diag][i] == 1 and (pos_diag, i) != queen:
					attacks += 1

		# neg_diag
		for i in range(col):
			neg_diag = queen[0] + queen[1] - i # row + col
			if 0 <= neg_diag and neg_diag < col:
				if board[i][neg_diag] == 1 and (i, neg_diag) != queen:
					attacks += 1

	return attacks


def copy_board(board):
	return list(map(list, board))


def gradient_search(board):
	
	rows = len(board)
	cols = len(board[0])

	old_board = copy_board(board)
	best_board = old_board
	init_attack = attack(old_board)
	
	print("Init_attack:", init_attack)
		
	while QUEENS:

		queen_rows, queens_rc = get_rows(old_board)
		current = 0
		del queen_rows

		for q in queens_rc:
			for r in range(rows):

				new_board = copy_board(old_board)
				new_board[q[0]][q[1]] = 0
				new_board[r][q[1]] = 1

				if attack(new_board) < attack(best_board):
					best_board = new_board
					current = attack(new_board)
				
		old_board = copy_board(best_board)

		if current >= init_attack:
			break
		else:
			init_attack = current

	for r in range(rows):
		for c in range(cols):
			board[r][c] = best_board[r][c]
	
	if attack(board) == 0:
		return True
	else:
		return False

